"""Ctrl+Space and the message keys in Unigram 13.1.1's selection mode.

Unigram enters selection mode from Select in a message's context menu
(DialogViewModel.SelectMessage). In selection mode a message is a toggle
button: Space runs MessageSelector.OnToggle, which selects or unselects it, and
unselecting the last selected message ends the mode. The context menu of a
selected message then lists the commands for the selection and no Select, so
the add-on's menu lookup for Select never found anything there. While the mode
lasts, ChatView shows ManagePanel below the chat, with ButtonForward and
ButtonDelete, or ButtonReport when the messages are picked for a report.
"""

import ast
import sys
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"
class _SelectedState:
	"""controlTypes.State.SELECTED: a set member that knows NVDA's labels."""

	displayString = "selected"
	negativeDisplayString = "not selected"


SELECTED = _SelectedState()


def _module():
	return ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))


def _exec(nodes, namespace):
	for node in nodes:
		if isinstance(node, ast.FunctionDef):
			node.decorator_list = []
	exec(compile(ast.Module(body=nodes, type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace


def _load_functions(names, namespace):
	nodes = [
		node for node in _module().body
		if isinstance(node, ast.FunctionDef) and node.name in names
	]
	return _exec(nodes, namespace)


def _class_methods(class_name, names):
	cls = next(
		node for node in _module().body
		if isinstance(node, ast.ClassDef) and node.name == class_name
	)
	return [node for node in cls.body if isinstance(node, ast.FunctionDef) and node.name in names]


def _load_app_methods(names, namespace):
	_exec(_class_methods("AppModule", names), namespace)
	return [namespace[name] for name in names]


def _message(selected=False):
	return SimpleNamespace(states={SELECTED} if selected else set())


def _namespace(**extra):
	namespace = {"State": SimpleNamespace(SELECTED=SELECTED)}
	_load_functions(["_is_selected"], namespace)
	namespace.update(extra)
	return namespace


class _RawElement:
	def __init__(self, automation_id, children=()):
		self.automation_id = automation_id
		self.children = list(children)
		self.parent = None
		for child in self.children:
			child.parent = self

	def findFirst(self, scope, condition):
		assert scope == "children"
		return next((child for child in self.children if condition(child)), None)


def _fake_uia_handler(monkeypatch):
	client = SimpleNamespace(
		CreatePropertyCondition=lambda property_id, value: (
			lambda element: property_id == "automationId" and element.automation_id == value
		),
		CreateOrCondition=lambda first, second: (lambda element: first(element) or second(element)),
	)
	handler = SimpleNamespace(
		clientObject=client,
		baseTreeWalker=SimpleNamespace(getParentElement=lambda element: element.parent),
	)
	monkeypatch.setitem(
		sys.modules,
		"UIAHandler",
		SimpleNamespace(
			handler=handler,
			UIA=SimpleNamespace(UIA_AutomationIdPropertyId="automationId"),
			TreeScope_Children="children",
		),
	)


def _bar_lookup():
	namespace = {"_MESSAGE_SELECTION_BAR_AUTOMATION_IDS": ("ButtonForward", "ButtonReport")}
	return _load_functions(["_is_message_selection_bar_shown"], namespace)["_is_message_selection_bar_shown"]


def _messages_list_beside(*automation_ids):
	messages = _RawElement("Messages")
	_RawElement("", [messages, *(_RawElement(automation_id) for automation_id in automation_ids)])
	return SimpleNamespace(UIAElement=messages)


def test_the_chat_selection_bar_is_found_beside_the_message_list(monkeypatch):
	_fake_uia_handler(monkeypatch)
	shown = _bar_lookup()

	assert shown(_messages_list_beside("TextField", "ButtonManage", "ButtonForward", "ButtonDelete"))
	# Picking messages for a report collapses Forward and Delete and shows Report.
	assert shown(_messages_list_beside("ButtonManage", "ButtonReport"))


def test_the_chat_list_selection_bar_does_not_count(monkeypatch):
	# MainPage's bar for selecting chats also has a ButtonManage.
	_fake_uia_handler(monkeypatch)

	assert not _bar_lookup()(_messages_list_beside("TextField", "ChatsList", "ButtonManage", "ManageMute"))


def test_an_unreadable_message_list_means_no_selection_bar(monkeypatch):
	_fake_uia_handler(monkeypatch)
	shown = _bar_lookup()

	class Gone:
		@property
		def UIAElement(self):
			raise RuntimeError("element went away")

	assert not shown(Gone())
	assert not shown(SimpleNamespace(UIAElement=_RawElement("Messages")))


def _selection_mode(bar_shown, queries):
	namespace = _namespace(
		_is_message_selection_bar_shown=lambda messages: queries.append(messages) or bar_shown,
	)
	(method,) = _load_app_methods(["_is_message_selection_mode"], namespace)
	messages = SimpleNamespace(UIAAutomationId="Messages")
	instance = SimpleNamespace(_get_current_message_row_and_list=lambda obj: (obj, messages))
	return lambda obj: method(instance, obj), messages


def test_a_selected_message_means_selection_mode_without_a_query():
	queries = []
	is_selection_mode, _ = _selection_mode(False, queries)

	assert is_selection_mode(_message(selected=True))
	assert queries == []


def test_an_unselected_message_asks_for_the_selection_bar_of_its_chat():
	queries = []
	is_selection_mode, messages = _selection_mode(True, queries)

	assert is_selection_mode(_message())
	assert queries == [messages]

	is_selection_mode, _ = _selection_mode(False, [])
	assert not is_selection_mode(_message())


def _is_chat_selected(chat):
	"""Stands in for the chat list's reader of a chat's selection."""


def _ctrl_space(focus, selection_mode, is_message=True, is_chat=False):
	calls = []
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"icons_from_context_menu": {"select": ""},
		"_is_chat_list_item": lambda obj: is_chat,
		"_is_chat_list_selection_mode": lambda obj: selection_mode,
		"_is_chat_selected": _is_chat_selected,
	}
	(method,) = _load_app_methods(["script_selectMessage"], namespace)
	instance = SimpleNamespace(
		is_message_object=lambda obj: is_message,
		_is_message_selection_mode=lambda obj: selection_mode,
		_toggle_selection=lambda obj, *reader: calls.append(("toggle", obj, *reader)),
		activate_option_for_menu=lambda icons, list_name: calls.append(("menu", icons, list_name)),
	)
	method(instance, None)
	return calls


def test_ctrl_space_starts_selection_mode_from_the_context_menu():
	assert _ctrl_space(_message(), selection_mode=False) == [("menu", "", "Messages")]


def test_ctrl_space_selects_or_unselects_a_message_in_selection_mode():
	"""The menu of a selected message has no Select, so it toggles like Unigram."""
	focus = _message(selected=True)

	assert _ctrl_space(focus, selection_mode=True) == [("toggle", focus)]


def test_ctrl_space_starts_chat_selection_from_the_chat_context_menu():
	"""Select in a chat's menu runs ChatListViewModel.SelectChat."""
	assert _ctrl_space(_message(), selection_mode=False, is_message=False, is_chat=True) == [
		("menu", "", "ChatsList")
	]


def test_ctrl_space_selects_or_unselects_a_chat_in_selection_mode():
	"""In selection mode a chat's menu has no Select, and a click toggles it."""
	focus = _message(selected=True)

	assert _ctrl_space(focus, selection_mode=True, is_message=False, is_chat=True) == [
		("toggle", focus, _is_chat_selected)
	]


def test_ctrl_space_does_nothing_outside_messages_and_chats():
	assert _ctrl_space(SimpleNamespace(), selection_mode=True, is_message=False) == []


class _Toggle:
	"""Run _toggle_selection with a fake Unigram and NVDA scheduler."""

	def __init__(self, focus, applies_after_polls=0, selects=None):
		self.focus = focus
		self.scheduled = []
		self.spoken = []
		self.sent = []
		self.applies_after_polls = applies_after_polls
		self.selects = selects
		namespace = _namespace(
			core=SimpleNamespace(callLater=lambda delay, function, *args: self.scheduled.append((function, args))),
			api=SimpleNamespace(getFocusObject=lambda: self.focus),
			message=self.spoken.append,
			_SELECTION_POLL_DELAY_MS=50,
			_SELECTION_POLL_LIMIT=10,
		)
		toggle, report = _load_app_methods(
			["_toggle_selection", "_report_selection"],
			namespace,
		)
		self.instance = SimpleNamespace(
			_selection_toggle=None,
			keys={"space": SimpleNamespace(send=lambda: self.sent.append("space"))},
			_same_uia_element=lambda first, second: first is second,
		)
		self.instance._report_selection = lambda pending: report(self.instance, pending)
		self.toggle = lambda obj: toggle(self.instance, obj)

	def run(self, obj):
		self.toggle(obj)
		polls = 0
		while self.scheduled:
			function, args = self.scheduled.pop(0)
			if polls == self.applies_after_polls and self.selects is not None:
				obj.states = {SELECTED} if self.selects else set()
			function(*args)
			polls += 1
		return polls


def test_toggling_a_message_presses_space_and_announces_the_new_state():
	focus = _message()
	toggle = _Toggle(focus, applies_after_polls=2, selects=True)

	polls = toggle.run(focus)

	assert toggle.sent == ["space"]
	assert toggle.spoken == ["selected"]
	assert polls == 3
	assert toggle.instance._selection_toggle is None


def test_unselecting_a_message_is_announced_with_nvdas_negative_state():
	focus = _message(selected=True)
	toggle = _Toggle(focus, selects=False)

	toggle.run(focus)

	assert toggle.spoken == ["not selected"]


def test_nothing_is_announced_when_unigram_does_not_change_the_message():
	focus = _message()
	toggle = _Toggle(focus)

	polls = toggle.run(focus)

	assert toggle.spoken == []
	assert polls == 10
	assert toggle.instance._selection_toggle is None


def test_the_announcement_is_dropped_when_the_focus_moves_on():
	focus = _message()
	toggle = _Toggle(focus, applies_after_polls=1, selects=True)
	toggle.toggle(focus)
	toggle.focus = _message()

	while toggle.scheduled:
		function, args = toggle.scheduled.pop(0)
		focus.states = {SELECTED}
		function(*args)

	assert toggle.spoken == []
	assert toggle.instance._selection_toggle is None


def _message_item_class(app):
	class Base:
		def event_stateChange(self):
			app.reported.append(self)

	namespace = {"Base": Base, "icons_from_context_menu": {"edit": "edit", "reply": "reply"}}
	methods = _class_methods(
		"Message_list_item",
		["script_edit_message", "script_reply_to_message", "event_stateChange"],
	)
	for method in methods:
		method.decorator_list = []
	# The methods call super(), so they have to be compiled inside a class body.
	module = ast.parse("class MessageItem(Base):\n\tpass\n")
	module.body[0].body = methods
	exec(compile(module, str(SOURCE_PATH), "exec"), namespace)
	item = namespace["MessageItem"]()
	item.appModule = app
	return item


def _app(selection_mode):
	app = SimpleNamespace(calls=[], reported=[], _selection_toggle=None)
	app._same_uia_element = lambda first, second: first is second
	app._is_message_selection_mode = lambda obj: selection_mode
	app._toggle_selection = lambda obj: app.calls.append(("toggle", obj))
	app.activate_option_for_menu = lambda icons, list_name: app.calls.append(("menu", icons))
	return app


def test_enter_and_backspace_keep_reply_and_edit_outside_selection_mode():
	app = _app(selection_mode=False)
	item = _message_item_class(app)
	sent = []

	item.script_reply_to_message(SimpleNamespace(send=lambda: sent.append("enter")))
	item.script_edit_message(SimpleNamespace(send=lambda: sent.append("backspace")))

	assert app.calls == [("menu", "reply"), ("menu", "edit")]
	assert sent == []


def test_enter_and_backspace_do_not_open_the_context_menu_in_selection_mode():
	app = _app(selection_mode=True)
	item = _message_item_class(app)
	sent = []

	item.script_reply_to_message(SimpleNamespace(send=lambda: sent.append("enter")))
	item.script_edit_message(SimpleNamespace(send=lambda: sent.append("backspace")))

	assert app.calls == [("toggle", item)]
	assert sent == ["backspace"]


def test_nvda_does_not_repeat_a_selection_the_add_on_announces():
	app = _app(selection_mode=True)
	item = _message_item_class(app)

	app._selection_toggle = {"object": item}
	item.event_stateChange()
	assert app.reported == []

	app._selection_toggle = None
	item.event_stateChange()
	assert app.reported == [item]


def test_other_messages_keep_their_state_announcements_during_a_toggle():
	app = _app(selection_mode=True)
	toggled = _message_item_class(app)
	other = _message_item_class(app)

	app._selection_toggle = {"object": toggled}
	other.event_stateChange()

	assert app.reported == [other]
