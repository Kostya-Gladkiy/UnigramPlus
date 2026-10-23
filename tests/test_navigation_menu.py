"""Alt+M: the navigation menu button in Unigram 13.1 and earlier versions.

Unigram 13.1 (commit d44bbf060, "Simplify navigation menu") replaced the
NavigationButton named Photo, a ToggleButton that opened the side pane, with a
MoreButton of the same name. MoreButton derives from SettingsButton, whose
automation peer is a ButtonAutomationPeer, so the menu button is now reported
as a plain button, and clicking it opens a MenuFlyout.
"""

import ast
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"
ROLE = SimpleNamespace(BUTTON="button", TOGGLEBUTTON="toggleButton", LINK="link")


def _load_show_menu(messages):
	module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
	app_module = next(
		node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule"
	)
	method = next(
		node
		for node in app_module.body
		if isinstance(node, ast.FunctionDef) and node.name == "script_showMenu"
	)
	method.decorator_list = []
	namespace = {"Role": ROLE, "message": messages.append, "_": lambda text: text}
	exec(compile(ast.Module(body=[method], type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace["script_showMenu"]


def _element(automation_id, role, actions=None):
	element = SimpleNamespace(UIAAutomationId=automation_id, role=role)
	element.doAction = lambda: actions.append(element)
	return element


def _press(*elements):
	messages = []
	_load_show_menu(messages)(SimpleNamespace(getElements=lambda: list(elements)), None)
	return messages


def test_alt_m_opens_the_unigram_13_1_menu_button():
	actions = []
	menu = _element("Photo", ROLE.BUTTON, actions)
	chats = _element("ChatsList", "list", actions)

	assert _press(chats, menu) == []
	assert actions == [menu]


def test_alt_m_still_opens_the_side_pane_toggle_before_unigram_13_1():
	actions = []
	pane_toggle = _element("Photo", ROLE.TOGGLEBUTTON, actions)

	assert _press(pane_toggle) == []
	assert actions == [pane_toggle]


def test_alt_m_leaves_other_photo_elements_alone():
	"""The profile page's photo shares the name but is a link."""
	actions = []
	profile_photo = _element("Photo", ROLE.LINK, actions)

	assert _press(profile_photo) == ["Navigation menu not available"]
	assert actions == []


def test_alt_m_reports_when_the_menu_button_is_hidden():
	# MainPage collapses the button when the chat list is hidden in a narrow window.
	messages = []
	show_menu = _load_show_menu(messages)

	show_menu(SimpleNamespace(getElements=lambda: []), None)

	def fail():
		raise RuntimeError("UIA element went away")

	show_menu(SimpleNamespace(getElements=fail), None)
	assert messages == ["Navigation menu not available"] * 2
