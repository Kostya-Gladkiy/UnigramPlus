"""Shortcuts must survive a missing UIA link instead of dying silently.

Unigram rebuilds its templates constantly, so firstChild, next, parent and even
location are routinely absent. Written out inline, one missing link raises
inside a script, and NVDA announces nothing at all: the shortcut simply looks
broken.
"""

import ast
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"


def _module():
	return ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))


def _load(names, namespace):
	members = [
		node
		for node in _module().body
		if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names
	]
	for member in members:
		if isinstance(member, ast.FunctionDef):
			member.decorator_list = []
	exec(compile(ast.Module(body=members, type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace


def _app_method(name, namespace):
	app = next(
		node for node in _module().body
		if isinstance(node, ast.ClassDef) and node.name == "AppModule"
	)
	method = next(
		node for node in app.body
		if isinstance(node, ast.FunctionDef) and node.name == name
	)
	method.decorator_list = []
	exec(compile(ast.Module(body=[method], type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace[name]


def _helpers():
	return _load({"_relative", "_is_on_screen"}, {})


def test_following_relations_stops_at_the_first_missing_link():
	helpers = _helpers()
	relative = helpers["_relative"]
	leaf = SimpleNamespace(name="leaf", next=None)
	node = SimpleNamespace(firstChild=leaf)

	assert relative(node, "firstChild", "name") == "leaf"
	assert relative(node, "firstChild", "next", "name") is None
	assert relative(None, "firstChild") is None


def test_following_relations_survives_a_provider_that_raises():
	helpers = _helpers()

	class Angry:
		@property
		def firstChild(self):
			raise RuntimeError("the provider went away")

	assert helpers["_relative"](Angry(), "firstChild", "name") is None


def test_on_screen_tolerates_a_missing_location():
	is_on_screen = _helpers()["_is_on_screen"]

	assert is_on_screen(SimpleNamespace(location=SimpleNamespace(width=200)))
	assert not is_on_screen(SimpleNamespace(location=None))
	assert not is_on_screen(SimpleNamespace(location=SimpleNamespace(width=0)))
	assert not is_on_screen(None)


def test_unread_message_lookup_skips_rows_without_that_layout():
	"""ALT+3 raised on the first row that had no button with two children."""
	namespace = _helpers()
	namespace.update({
		"Role": SimpleNamespace(BUTTON="button"),
		"message": lambda text: namespace.setdefault("said", []).append(text),
		"_": lambda text: text,
	})
	method = _app_method("script_goToTheLastUnreadMessage", namespace)

	marker = SimpleNamespace(name="")
	glyph_holder = SimpleNamespace(firstChild=SimpleNamespace(next=marker), role="button")
	unread_row = SimpleNamespace(firstChild=glyph_holder, previous=None)
	unread_row.setFocus = lambda: namespace.setdefault("focused", []).append(unread_row)
	# A plain text row: no firstChild at all, which used to raise here.
	plain_row = SimpleNamespace(firstChild=None, previous=unread_row)
	last_row = SimpleNamespace(firstChild=SimpleNamespace(firstChild=None, role="text"), previous=plain_row)
	messages = SimpleNamespace(lastChild=last_row)

	instance = SimpleNamespace(getMessagesElement=lambda: messages)
	method(instance, None)

	assert namespace.get("focused") == [unread_row]
	assert namespace.get("said") is None


def test_unread_message_lookup_is_bounded():
	"""A long history was walked to its very first message, one UIA call a row."""
	namespace = _helpers()
	visited = []

	class Row:
		firstChild = None
		def __init__(self, index):
			self.index = index
		@property
		def previous(self):
			visited.append(self.index)
			return Row(self.index + 1)

	namespace.update({
		"Role": SimpleNamespace(BUTTON="button"),
		"message": lambda text: None,
		"_": lambda text: text,
	})
	method = _app_method("script_goToTheLastUnreadMessage", namespace)
	instance = SimpleNamespace(getMessagesElement=lambda: SimpleNamespace(lastChild=Row(0)))

	method(instance, None)

	assert len(visited) <= 500
