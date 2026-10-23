"""Ctrl+Space in Unigram 13.1.1's chat list.

Select in a chat's context menu (ChatListViewModel.SelectChat) switches
ChatsList, a WinUI ListView, to ListViewSelectionMode.Multiple. There a click
on a chat, or Space or Enter on it, raises ItemClick, where
MainPage.ListView_ItemClick adds or removes the chat, and the ListView toggles
the row's own selection. Unselecting the last chat switches the list back to
Single (None in a narrow window). WinUI then keeps that chat as the single
selection, and the open chat is the selected one outside selection mode, so a
chat's SELECTED state only counts while the list reports CanSelectMultiple.
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


class _RawElement:
	"""A raw UIA element: its AutomationId, parent and CanSelectMultiple."""

	def __init__(self, automation_id, parent=None, can_select_multiple=None):
		self.CurrentAutomationId = automation_id
		self.parent = parent
		self.can_select_multiple = can_select_multiple
		self.reads = 0

	def GetCurrentPropertyValue(self, property_id):
		assert property_id == "canSelectMultiple"
		self.reads += 1
		return self.can_select_multiple


def _fake_uia_handler(monkeypatch, walked=None):
	def parent_of(element):
		if walked is not None:
			walked.append(element)
		return element.parent

	monkeypatch.setitem(
		sys.modules,
		"UIAHandler",
		SimpleNamespace(
			handler=SimpleNamespace(baseTreeWalker=SimpleNamespace(GetParentElement=parent_of)),
			UIA=SimpleNamespace(UIA_SelectionCanSelectMultiplePropertyId="canSelectMultiple"),
		),
	)


def _selection_mode_reader():
	namespace = {"_CHAT_LIST_ANCESTOR_DEPTH": 8}
	return _load_functions(["_is_chat_list_selection_mode"], namespace)["_is_chat_list_selection_mode"]


def _chat_in(chat_list, wrappers=0):
	parent = chat_list
	for _ in range(wrappers):
		parent = _RawElement("", parent)
	return SimpleNamespace(UIAElement=_RawElement("", parent), states=set())


def test_a_chat_list_that_can_select_multiple_is_in_selection_mode(monkeypatch):
	_fake_uia_handler(monkeypatch)
	is_selection_mode = _selection_mode_reader()
	chat_list = _RawElement("ChatsList", can_select_multiple=True)

	assert is_selection_mode(_chat_in(chat_list))
	assert chat_list.reads == 1


def test_a_single_selection_chat_list_is_not_in_selection_mode(monkeypatch):
	_fake_uia_handler(monkeypatch)
	is_selection_mode = _selection_mode_reader()

	assert not is_selection_mode(_chat_in(_RawElement("ChatsList", can_select_multiple=False)))
	# UIA answers an unsupported property with a COM object, which is truthy.
	assert not is_selection_mode(_chat_in(_RawElement("ChatsList", can_select_multiple=object())))


def test_the_chat_list_is_found_through_template_wrappers(monkeypatch):
	_fake_uia_handler(monkeypatch)
	is_selection_mode = _selection_mode_reader()

	assert is_selection_mode(_chat_in(_RawElement("ChatsList", can_select_multiple=True), wrappers=3))


def test_the_walk_up_to_the_chat_list_is_bounded(monkeypatch):
	walked = []
	_fake_uia_handler(monkeypatch, walked)
	is_selection_mode = _selection_mode_reader()
	chat_list = _RawElement("ChatsList", can_select_multiple=True)

	assert not is_selection_mode(_chat_in(chat_list, wrappers=8))
	assert len(walked) == 8
	assert chat_list.reads == 0
	assert not is_selection_mode(SimpleNamespace(UIAElement=_RawElement("")))


def test_an_unreadable_chat_is_not_in_selection_mode(monkeypatch):
	_fake_uia_handler(monkeypatch)
	is_selection_mode = _selection_mode_reader()

	class Gone:
		@property
		def UIAElement(self):
			raise RuntimeError("element went away")

	assert not is_selection_mode(Gone())


def _selected_reader(selection_mode, queries):
	namespace = {
		"State": SimpleNamespace(SELECTED=SELECTED),
		"_is_chat_list_selection_mode": lambda chat: queries.append(chat) or selection_mode,
	}
	return _load_functions(["_is_selected", "_is_chat_selected"], namespace)["_is_chat_selected"]


def _chat(selected=False):
	return SimpleNamespace(states={SELECTED} if selected else set())


def test_an_unselected_chat_is_not_picked_without_a_query():
	queries = []

	assert _selected_reader(True, queries)(_chat()) is False
	assert queries == []


def test_a_selected_chat_is_picked_only_in_selection_mode():
	chat = _chat(selected=True)

	assert _selected_reader(True, [])(chat) is True
	# Outside selection mode the open chat is the selected one.
	assert _selected_reader(False, [])(chat) is False


def test_an_unreadable_chat_state_stays_unknown():
	class Gone:
		@property
		def states(self):
			raise RuntimeError("element went away")

	assert _selected_reader(True, [])(Gone()) is None


class _Toggle:
	"""Run _toggle_selection on a chat with a fake Unigram and NVDA scheduler."""

	def __init__(self, focus, chat_list):
		self.focus = focus
		self.chat_list = chat_list
		self.scheduled = []
		self.spoken = []
		self.sent = []
		namespace = {
			"State": SimpleNamespace(SELECTED=SELECTED),
			"_is_chat_list_selection_mode": lambda chat: self.chat_list["multiple"],
			"core": SimpleNamespace(callLater=lambda delay, function, *args: self.scheduled.append((function, args))),
			"api": SimpleNamespace(getFocusObject=lambda: self.focus),
			"message": self.spoken.append,
			"_SELECTION_POLL_DELAY_MS": 50,
			"_SELECTION_POLL_LIMIT": 10,
		}
		_load_functions(["_is_selected", "_is_chat_selected"], namespace)
		self.is_chat_selected = namespace["_is_chat_selected"]
		_exec(_class_methods("AppModule", ["_toggle_selection", "_report_selection"]), namespace)
		toggle, report = namespace["_toggle_selection"], namespace["_report_selection"]
		self.instance = SimpleNamespace(
			_selection_toggle=None,
			keys={"space": SimpleNamespace(send=lambda: self.sent.append("space"))},
			_same_uia_element=lambda first, second: first is second,
		)
		self.instance._report_selection = lambda pending: report(self.instance, pending)
		self.toggle = lambda obj: toggle(self.instance, obj, self.is_chat_selected)

	def run(self, obj, unigram):
		self.toggle(obj)
		polls = 0
		while self.scheduled:
			function, args = self.scheduled.pop(0)
			if polls == 1:
				unigram()
			function(*args)
			polls += 1
		return polls


def test_picking_a_chat_presses_space_and_announces_it():
	focus = _chat()
	chat_list = {"multiple": True}
	toggle = _Toggle(focus, chat_list)

	toggle.run(focus, lambda: setattr(focus, "states", {SELECTED}))

	assert toggle.sent == ["space"]
	assert toggle.spoken == ["selected"]
	assert toggle.instance._selection_toggle is None


def test_unpicking_the_last_chat_is_announced_although_it_stays_selected():
	"""Selection mode ends, and WinUI keeps the chat as its single selection."""
	focus = _chat(selected=True)
	chat_list = {"multiple": True}
	toggle = _Toggle(focus, chat_list)

	toggle.run(focus, lambda: chat_list.update(multiple=False))

	assert focus.states == {SELECTED}
	assert toggle.spoken == ["not selected"]


def _chat_item_class(app):
	class Base:
		def event_stateChange(self):
			app.reported.append(self)

	methods = _class_methods("ChatListItem", ["event_stateChange"])
	# The method calls super(), so it has to be compiled inside a class body.
	module = ast.parse("class ChatItem(Base):\n\tpass\n")
	module.body[0].body = methods
	namespace = {"Base": Base}
	exec(compile(module, str(SOURCE_PATH), "exec"), namespace)
	item = namespace["ChatItem"]()
	item.appModule = app
	return item


def test_nvda_does_not_repeat_a_chat_selection_the_add_on_announces():
	app = SimpleNamespace(reported=[], _selection_toggle=None)
	app._same_uia_element = lambda first, second: first is second
	toggled = _chat_item_class(app)
	other = _chat_item_class(app)

	app._selection_toggle = {"object": toggled}
	toggled.event_stateChange()
	other.event_stateChange()
	assert app.reported == [other]

	app._selection_toggle = None
	toggled.event_stateChange()
	assert app.reported == [other, toggled]


class _UIA:
	"""Stands in for NVDAObjects.UIA.UIA."""


class _FocusedChat(_UIA):
	role = "listItem"
	UIAAutomationId = ""

	def __init__(self, name, selected):
		self.name = name
		self.states = {SELECTED} if selected else set()


def _focus_chat(chat, selection_mode):
	"""Run the real focus handler on a chat row and return its spoken name."""
	queries = []
	namespace = {
		"UIA": _UIA,
		"Role": SimpleNamespace(LISTITEM="listItem", EDITABLETEXT="editableText"),
		"State": SimpleNamespace(SELECTED=SELECTED),
		"conf": SimpleNamespace(get=lambda key: False),
		"is_recording_button": lambda obj: False,
		"File_transfer_progress_tracking": SimpleNamespace(active=True),
		"speech": SimpleNamespace(cancelSpeech=lambda: None),
		"_": lambda text: text,
		"_is_chat_list_item": lambda obj: True,
		"_is_chat_list_selection_mode": lambda obj: queries.append(obj) or selection_mode,
	}
	_load_functions(["_is_selected", "_is_chat_selected"], namespace)
	_exec(_class_methods("AppModule", ["event_gainFocus"]), namespace)
	saved = {}
	app = SimpleNamespace(
		isUnigramWindow=True,
		_restore_focus_after_record_button=lambda obj: False,
		_remember_messages_button=lambda obj: None,
		_classify_window_surface=lambda obj: None,
		isSkipName=0,
		isOpenProfile=False,
		execute_context_menu_option=False,
		isRecord=False,
		isDelete=False,
		is_message_object=lambda obj: False,
		saved_items=SimpleNamespace(save=saved.__setitem__),
		actionChatElementInFocus=lambda obj: obj.name,
	)
	handled = []
	namespace["event_gainFocus"](app, chat, lambda: handled.append(True))
	assert handled == [True]
	assert saved["last focused chat"] is chat
	return chat.name, queries


def test_a_focused_chat_is_said_to_be_selected_in_selection_mode():
	name, _queries = _focus_chat(_FocusedChat("Alice", selected=True), selection_mode=True)

	assert name == "Selected. Alice"


def test_the_open_chat_is_not_said_to_be_selected_outside_selection_mode():
	"""Outside selection mode the chat list's single selection is the open chat."""
	name, queries = _focus_chat(_FocusedChat("Alice", selected=True), selection_mode=False)

	assert name == "Alice"
	assert len(queries) == 1


def test_an_unselected_chat_keeps_its_name_without_a_query():
	for selection_mode in (True, False):
		name, queries = _focus_chat(_FocusedChat("Alice", selected=False), selection_mode)

		assert name == "Alice", selection_mode
		assert queries == [], selection_mode


def test_a_selected_chat_is_not_marked_twice():
	name, _queries = _focus_chat(_FocusedChat("Selected. Alice", selected=True), selection_mode=True)

	assert name == "Selected. Alice"
