"""Shift+Alt+M: open Unigram's settings from the bar below the chat list.

Unigram 13.1 (commit 8db8d29de, "Add bottom navigation bar") replaced the side
pane with a TopNavView named "Navigation" below the chat list: Chats first,
Settings last. Selecting an item switches MainPage between the chat list and
the settings page, which is built the first time it is shown. Unigram 13.1 also
lists the other accounts and Add account at the top of the settings (commit
458f34234), which is where the Russian UnigramPlus mod puts the focus.
"""

import ast
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"
ROLE = SimpleNamespace(PANE="pane", LIST="list", LISTITEM="listItem", BUTTON="button")
METHODS = (
	"_get_settings_page",
	"get_settings_list",
	"_get_settings_tab",
	"_get_settings_start",
	"script_openSettings",
	"_focus_settings_start",
)


class Element:
	def __init__(self, automation_id="", role="", name="", states=(), children=(), log=None):
		self.UIAAutomationId = automation_id
		self.role = role
		self.name = name
		self.states = set(states)
		self.children = list(children)
		self.next = None
		self.log = log if log is not None else []
		for previous, following in zip(self.children, self.children[1:]):
			previous.next = following

	@property
	def firstChild(self):
		return self.children[0] if self.children else None

	@property
	def lastChild(self):
		return self.children[-1] if self.children else None

	def doAction(self):
		self.log.append(("select", self.name))

	def setFocus(self):
		self.log.append(("focus", self.name))


class Unigram:
	"""Runs the add-on's methods against a UIA tree that the test can change."""

	def __init__(self, elements=()):
		self.elements = list(elements)
		self.messages = []
		self.pending = []
		module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
		relative = next(
			node for node in module.body if isinstance(node, ast.FunctionDef) and node.name == "_relative"
		)
		constants = [
			node
			for node in module.body
			if isinstance(node, ast.Assign)
			and isinstance(node.targets[0], ast.Name)
			and node.targets[0].id.startswith("_SETTINGS_FOCUS_POLL_")
		]
		app_module = next(
			node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule"
		)
		methods = [
			node for node in app_module.body if isinstance(node, ast.FunctionDef) and node.name in METHODS
		]
		assert {node.name for node in methods} == set(METHODS)
		for method in methods:
			method.decorator_list = []
		namespace = {
			"Role": ROLE,
			"State": SimpleNamespace(SELECTED="selected"),
			"message": self.messages.append,
			"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
			"_": lambda text: text,
			"core": SimpleNamespace(callLater=lambda delay, function, *args: self.pending.append((delay, function, args))),
		}
		body = [*constants, relative, *methods]
		exec(compile(ast.Module(body=body, type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
		self.namespace = namespace
		self._settings_focus_request = None
		for name in METHODS:
			setattr(self, name, namespace[name].__get__(self))

	def getElements(self):
		return list(self.elements)

	def run_pending(self):
		"""Run the next delayed call, as NVDA's core.callLater would."""
		delay, function, args = self.pending.pop(0)
		assert delay == self.namespace["_SETTINGS_FOCUS_POLL_DELAY_MS"]
		function(*args)


def _bar(log):
	return Element(
		automation_id="Navigation",
		role=ROLE.LIST,
		children=[
			Element(role=ROLE.LISTITEM, name="Chats", states=("selected",), log=log),
			Element(role=ROLE.LISTITEM, name="Settings", log=log),
		],
	)


def _settings_page(accounts=(), add_account=True, log=None):
	log = log if log is not None else []
	header = [
		Element(role="link", name="Profile picture"),
		Element(automation_id="Title", role="staticText", name="Ken"),
		Element(automation_id="Identity", role="graphic"),
		Element(automation_id="Subtitle", role="staticText", name="online"),
		Element(role=ROLE.BUTTON, name="QR code"),
	]
	account_list = Element(
		automation_id="Accounts",
		role=ROLE.LIST,
		children=[Element(role=ROLE.LISTITEM, name=name, log=log) for name in accounts],
	)
	rest = [Element(automation_id="AddAccount", role=ROLE.BUTTON, name="Add account", log=log)] if add_account else []
	profile = Element(automation_id="Profile", role=ROLE.BUTTON, name="My profile", log=log)
	categories = Element(
		automation_id="Navigation",
		role=ROLE.LIST,
		children=[Element(role=ROLE.LISTITEM, name="My profile", children=[profile])],
	)
	return Element(
		automation_id="ScrollingHost",
		role=ROLE.PANE,
		children=[*header, account_list, *rest, categories],
	)


def test_shift_alt_m_selects_the_settings_tab_and_focuses_add_account():
	log = []
	chats = Element(automation_id="ChatsList", role=ROLE.LIST)
	app = Unigram([chats, _bar(log)])

	app.script_openSettings(None)
	assert log == [("select", "Settings")]
	assert app.messages == []

	# Unigram builds the settings page after the tab is selected.
	app.run_pending()
	assert log == [("select", "Settings")]
	app.elements = [_settings_page(log=log), _bar(log)]
	app.run_pending()

	assert log == [("select", "Settings"), ("focus", "Add account")]
	assert app.pending == []
	assert app.messages == []


def test_shift_alt_m_focuses_the_first_other_account():
	log = []
	app = Unigram([_settings_page(accounts=("Work", "Family"), log=log), _bar(log)])

	app.script_openSettings(None)
	app.run_pending()

	assert log == [("select", "Settings"), ("focus", "Work")]


def test_shift_alt_m_focuses_the_open_category_when_there_is_no_add_account():
	log = []
	app = Unigram([_settings_page(add_account=False, log=log), _bar(log)])

	app.script_openSettings(None)
	app.run_pending()

	assert log == [("select", "Settings"), ("focus", "My profile")]


def test_shift_alt_m_uses_the_bar_after_the_open_chat():
	"""The chat comes first in UIA order, and its sticker panel has a "Navigation" list too."""
	log = []
	stickers = Element(
		automation_id="Navigation",
		role=ROLE.LIST,
		children=[Element(role=ROLE.LISTITEM, name=name, log=log) for name in ("Emoji", "GIFs", "Stickers")],
	)
	app = Unigram([stickers, Element(automation_id="ChatsList", role=ROLE.LIST), _bar(log)])

	app.script_openSettings(None)

	assert log == [("select", "Settings")]


def test_shift_alt_m_reports_when_there_is_no_settings_tab():
	"""Unigram 13.0 has no bar; its side pane "Navigation" is not a list."""
	log = []
	side_pane = Element(
		automation_id="Navigation",
		role="pane",
		children=[Element(role=ROLE.LISTITEM, name="Settings", log=log)],
	)

	for elements in ([], [Element(automation_id="ChatsList", role=ROLE.LIST)], [side_pane]):
		app = Unigram(elements)
		app.script_openSettings(None)
		assert app.messages == ["Settings not available"]
		assert app.pending == []
	assert log == []


def test_shift_alt_m_reports_when_the_tab_cannot_be_selected():
	app = Unigram([_bar([])])

	def fail():
		raise NotImplementedError

	app.elements[0].lastChild.doAction = fail
	app.script_openSettings(None)

	assert app.messages == ["Settings not available"]
	assert app.pending == []


def test_shift_alt_m_stops_waiting_for_a_settings_page_that_never_appears():
	log = []
	app = Unigram([_bar(log)])

	app.script_openSettings(None)
	polls = 0
	while app.pending:
		app.run_pending()
		polls += 1

	assert polls == app.namespace["_SETTINGS_FOCUS_POLL_LIMIT"]
	assert log == [("select", "Settings")]
	assert app._settings_focus_request is None
	assert app.messages == []


def test_shift_alt_m_retries_when_the_page_is_rebuilt_while_it_is_read():
	log = []
	app = Unigram([_bar(log)])
	app.script_openSettings(None)

	def rebuilt():
		raise OSError("element is no longer available")

	app.getElements = rebuilt
	app.run_pending()
	assert app._settings_focus_request is not None
	assert len(app.pending) == 1

	del app.getElements
	app.elements = [_settings_page(log=log), _bar(log)]
	app.run_pending()

	assert log == [("select", "Settings"), ("focus", "Add account")]
	assert app._settings_focus_request is None
	assert app.pending == []


def test_shift_alt_m_keeps_waiting_when_the_focus_cannot_move_yet():
	log = []
	page = _settings_page(log=log)
	add_account = next(item for item in page.children if item.UIAAutomationId == "AddAccount")
	app = Unigram([page, _bar(log)])
	app.script_openSettings(None)

	def fail():
		raise OSError("element is no longer available")

	add_account.setFocus = fail
	app.run_pending()
	assert app._settings_focus_request is not None
	assert len(app.pending) == 1

	del add_account.setFocus
	app.run_pending()

	assert log == [("select", "Settings"), ("focus", "Add account")]
	assert app._settings_focus_request is None
	assert app.pending == []


def test_shift_alt_m_stops_retrying_errors_at_the_poll_limit():
	app = Unigram([_bar([])])
	app.script_openSettings(None)

	def rebuilt():
		raise OSError("element is no longer available")

	app.getElements = rebuilt
	polls = 0
	while app.pending:
		app.run_pending()
		polls += 1

	assert polls == app.namespace["_SETTINGS_FOCUS_POLL_LIMIT"]
	assert app._settings_focus_request is None


def test_a_second_shift_alt_m_replaces_the_first_wait():
	log = []
	app = Unigram([_bar(log)])

	app.script_openSettings(None)
	app.script_openSettings(None)
	app.elements = [_settings_page(log=log), _bar(log)]
	app.run_pending()
	app.run_pending()

	assert log == [("select", "Settings"), ("select", "Settings"), ("focus", "Add account")]
	assert app.pending == []


def test_shift_alt_m_is_bound_and_documented():
	source = SOURCE_PATH.read_text(encoding="utf-8")
	assert '@script(description=_("Open Unigram settings"), gesture="kb:shift+alt+M")' in source
	for manual in (ROOT / "readme.md", ROOT / "addon" / "doc" / "en" / "readme.md"):
		assert "| **ALT+Shift+M** | UnigramPlus | Open Unigram settings |" in manual.read_text(encoding="utf-8")
