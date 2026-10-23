"""Unigram 13.0 settings categories: native Enter/Space, Alt+1 focus target.

Unigram 13.0 (commit fab889d04, "Improve settings keyboard navigation") set
IsTabStop to False on the TopNavViewItem rows of the settings page's
"Navigation" list. The focus now lands on the SettingsButton inside each row,
which opens its category with Enter or Space natively.
"""

import ast
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"


class Element:
	"""A UIA element with the relations get_settings_list walks."""

	def __init__(self, automation_id="", role="", name="", states=(), children=()):
		self.UIAAutomationId = automation_id
		self.role = role
		self.name = name
		self.states = set(states)
		self.children = list(children)
		self.next = None
		for previous, following in zip(self.children, self.children[1:]):
			previous.next = following

	@property
	def firstChild(self):
		return self.children[0] if self.children else None


def _module():
	return ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))


def _load_settings_list_finder():
	module = _module()
	relative = next(
		node for node in module.body if isinstance(node, ast.FunctionDef) and node.name == "_relative"
	)
	app_module = next(
		node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule"
	)
	methods = [
		node
		for node in app_module.body
		if isinstance(node, ast.FunctionDef) and node.name in ("_get_settings_page", "get_settings_list")
	]
	namespace = {
		"Role": SimpleNamespace(PANE="pane"),
		"State": SimpleNamespace(SELECTED="selected"),
	}
	exec(compile(ast.Module(body=[relative, *methods], type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)

	def get_settings_list(app):
		app._get_settings_page = lambda: namespace["_get_settings_page"](app)
		return namespace["get_settings_list"](app)

	return get_settings_list


def _category(name, selected=False):
	"""A TopNavViewItem row holding its SettingsButton, as in Unigram 13.0."""
	button = Element(automation_id=name, role="button", name=name)
	row = Element(role="listItem", name=name, states=("selected",) if selected else (), children=[button])
	return row, button


def _settings_page(categories):
	# SettingsPage.xaml: the profile header comes first, then the category list.
	return Element(
		automation_id="ScrollingHost",
		role="pane",
		children=[
			Element(role="link", name="Profile picture"),
			Element(automation_id="Title", role="staticText", name="Ken"),
			Element(automation_id="Identity", role="graphic"),
			Element(automation_id="Subtitle", role="staticText", name="online"),
			Element(role="button", name="QR code", children=[Element(role="staticText", name="")]),
			Element(automation_id="Navigation", role="list", children=categories),
			Element(role="button", name="Telegram Premium"),
		],
	)


def _app(*elements):
	return SimpleNamespace(getElements=lambda: list(elements))


def test_alt_1_focuses_the_button_of_the_open_settings_category():
	profile_row, _profile = _category("Profile")
	appearance_row, appearance = _category("Appearance", selected=True)
	page = _settings_page([profile_row, appearance_row])
	chats = Element(automation_id="ScrollingHost", role="pane", children=[Element(name="Archive")])

	assert _load_settings_list_finder()(_app(chats, page)) is appearance


def test_alt_1_focuses_the_first_category_button_when_none_is_open():
	"""Premium, Stars and the other pages outside the list leave nothing selected.

	The previous fixed walk (five siblings from the profile picture, then its
	first child) landed inside the QR code button on this layout.
	"""
	profile_row, profile = _category("Profile")
	appearance_row, _appearance = _category("Appearance")

	assert _load_settings_list_finder()(_app(_settings_page([profile_row, appearance_row]))) is profile


def test_alt_1_settings_fallback_gives_up_without_a_category_list():
	finder = _load_settings_list_finder()
	empty_page = _settings_page([])

	assert finder(_app(empty_page)) is False
	assert finder(_app(Element(automation_id="ScrollingHost", role="pane"))) is False
	assert finder(_app()) is False


def test_alt_1_settings_fallback_survives_a_list_rebuilt_while_it_is_read():
	"""A failed UIA read returns False, so Alt+1 still speaks its fallback."""

	class Replaced(Element):
		@property
		def states(self):
			raise OSError("element is no longer available")

		@states.setter
		def states(self, value):
			pass

	profile_row, _profile = _category("Profile")
	page = _settings_page([Replaced(role="listItem", name="Profile"), profile_row])

	assert _load_settings_list_finder()(_app(page)) is False


def test_settings_categories_have_no_enter_or_space_override():
	"""Enter and Space on the category buttons are Unigram's own since 13.0."""
	module = _module()
	classes = {node.name for node in module.body if isinstance(node, ast.ClassDef)}
	assert "SettingsPanelListItem" not in classes
	source = SOURCE_PATH.read_text(encoding="utf-8")
	assert "SettingsPanelListItem" not in source
