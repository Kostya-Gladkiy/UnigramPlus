import ast
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"

sys.path.insert(0, str(ROOT / "addon" / "appModules"))

from message_header import (  # noqa: E402
	move_message_header_after_content,
	move_profile_header_after_content,
)


def _app_class_ast():
	module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
	return next(node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule")


def _load_app_method(name, namespace):
	method = next(
		node for node in _app_class_ast().body if isinstance(node, ast.FunctionDef) and node.name == name
	)
	method.decorator_list = []
	exec(
		compile(ast.Module(body=[method], type_ignores=[]), str(SOURCE_PATH), "exec"),
		namespace,
	)
	return namespace[name]


@pytest.mark.parametrize("separator", ["\n", "\r\n"])
def test_ordinary_message_header_moves_after_content(separator):
	name = separator.join(("Sender", "Forwarded from Source", "message body"))

	assert move_message_header_after_content(name, "message body") == separator.join(
		("message body", "Sender", "Forwarded from Source")
	)


@pytest.mark.parametrize(
	"name",
	["message without a separator", "\nbody", "header\n", "\r\nbody", "header\r\n"],
)
def test_ordinary_message_header_edge_cases_are_unchanged(name):
	assert move_message_header_after_content(name, "body") == name


def test_multiline_message_content_is_kept_together_and_transform_is_idempotent():
	name = "Sender\r\nline 1\r\nline 2"
	moved = move_message_header_after_content(name, "line 1\r\nline 2")

	assert moved == "line 1\r\nline 2\r\nSender"
	assert move_message_header_after_content(moved, "line 1\r\nline 2") == moved
	assert move_message_header_after_content("line 1\r\nline 2", "line 1\r\nline 2") == ("line 1\r\nline 2")


def test_message_focus_maps_normalized_multiline_content_back_to_crlf_summary():
	conf = SimpleNamespace(get=lambda key: key == "messageHeaderAtTheEnd")
	namespace = {
		"Role": SimpleNamespace(LINK="link", TOGGLEBUTTON="toggleButton", PROGRESSBAR="progressBar"),
		"State": SimpleNamespace(SELECTED="selected"),
		"conf": conf,
		"_": lambda text: text,
		"phrase_administrator_in_message": {"en": ("administrator", "owner")},
		"re": __import__("re"),
		"move_message_header_after_content": move_message_header_after_content,
		"extract_message_text": lambda obj: "line 1\nline 2",
	}
	method = _load_app_method("action_message_focus", namespace)
	obj = SimpleNamespace(
		name="Sender\r\nline 1\r\nline 2",
		keywords=("seen", "not seen", "sent", "received"),
		firstChild=None,
		childCount=0,
		children=[],
		index_last_part_in_message=0,
		states=set(),
	)
	instance = SimpleNamespace(
		sender_message="",
		end_text="",
		saved_items=SimpleNamespace(get=lambda key: False),
	)

	assert method(instance, obj) == "line 1\r\nline 2\r\nSender"


def test_profile_file_name_is_announced_before_sender_from_feedback():
	name = "Ken🇹🇼 Chang: unigramPlus-5.6.1.nvda-addon"

	assert move_profile_header_after_content(name, "unigramPlus-5.6.1") == (
		"unigramPlus-5.6.1.nvda-addon, Ken🇹🇼 Chang"
	)


def test_profile_header_supports_colons_in_sender_and_split_file_titles():
	name = "ACME: Support: release.archive.tar.gz, 3 MB"

	assert move_profile_header_after_content(name, "release.archive.tar") == (
		"release.archive.tar.gz, 3 MB, ACME: Support"
	)


def test_profile_header_fallback_uses_the_first_sender_separator():
	assert move_profile_header_after_content("Sender: Photo") == "Photo, Sender"
	assert move_profile_header_after_content("Not a profile row") == "Not a profile row"


def test_message_focus_keeps_selected_first_and_respects_disabled_mode():
	state = {"messageHeaderAtTheEnd": True}
	conf = SimpleNamespace(get=lambda key: state.get(key, False))
	namespace = {
		"Role": SimpleNamespace(LINK="link", TOGGLEBUTTON="toggleButton", PROGRESSBAR="progressBar"),
		"State": SimpleNamespace(SELECTED="selected"),
		"conf": conf,
		"_": lambda text: text,
		"phrase_administrator_in_message": {"en": ("administrator", "owner")},
		"re": __import__("re"),
		"move_message_header_after_content": move_message_header_after_content,
		"extract_message_text": lambda obj: obj.content_anchor,
	}
	method = _load_app_method("action_message_focus", namespace)
	obj = SimpleNamespace(
		name="Sender\r\nmessage body",
		keywords=("seen", "not seen", "sent", "received"),
		firstChild=None,
		childCount=0,
		children=[],
		index_last_part_in_message=0,
		states={"selected"},
		content_anchor="message body",
	)
	instance = SimpleNamespace(
		sender_message="",
		end_text="",
		saved_items=SimpleNamespace(get=lambda key: False),
	)

	assert method(instance, obj) == "Selected. message body\r\nSender"
	assert method(instance, obj) == "Selected. message body\r\nSender"
	state["messageHeaderAtTheEnd"] = False
	obj.name = "Sender\r\nmessage body"
	obj.states = set()
	assert method(instance, obj) == "Sender\r\nmessage body"


def test_profile_media_detection_uses_media_frame_or_file_signature():
	method = _load_app_method("_profile_media_content_anchor", {})
	title = SimpleNamespace(UIAAutomationId="Title", name="report")
	subtitle = SimpleNamespace(UIAAutomationId="Subtitle", name="3 MB")
	button = SimpleNamespace(UIAAutomationId="Download", name="Download")
	media_frame = SimpleNamespace(
		UIAAutomationId="MediaFrame",
		UIAClassName="ProfileFilesTabPage",
		parent=None,
	)
	scrolling_host = SimpleNamespace(
		UIAAutomationId="ScrollingHost",
		UIAClassName="ListView",
		parent=media_frame,
	)
	row = SimpleNamespace(parent=scrolling_host)

	def find(obj, role=None, automation_id=None, max_depth=5):
		return {
			"Title": title,
			"Subtitle": subtitle,
			"Download": button,
		}.get(automation_id, False)

	instance = SimpleNamespace(_find_descendant=find)

	assert method(instance, row) == "report"

	plain_parent = SimpleNamespace(
		UIAAutomationId="ScrollingHost",
		UIAClassName="ListView",
		parent=None,
	)
	plain_row = SimpleNamespace(parent=plain_parent)
	instance._find_descendant = (
		lambda *args, **kwargs: title if kwargs.get("automation_id") == "Title" else False
	)
	assert method(instance, plain_row) is None


def test_profile_media_detection_supports_russian_mod_uia_structure():
	method = _load_app_method("_profile_media_content_anchor", {})
	title = SimpleNamespace(UIAAutomationId="Title", name="unigramPlus-5.6.")
	subtitle = SimpleNamespace(UIAAutomationId="Subtitle", name="1 MB")
	button = SimpleNamespace(UIAAutomationId="Button", name="Download")
	tab_title = SimpleNamespace(UIAAutomationId="Title")
	first = SimpleNamespace(next=SimpleNamespace(next=tab_title))
	container = SimpleNamespace(firstChild=first, parent=None)
	scrollbar = SimpleNamespace(UIAAutomationId="VerticalScrollBar")
	scrolling_host = SimpleNamespace(
		UIAAutomationId="ScrollingHost",
		UIAClassName="ListView",
		parent=container,
		next=scrollbar,
	)
	row = SimpleNamespace(parent=scrolling_host)

	def find(obj, role=None, automation_id=None, max_depth=5):
		return {
			"Title": title,
			"Subtitle": subtitle,
			"Button": button,
		}.get(automation_id, False)

	instance = SimpleNamespace(_find_descendant=find)

	assert method(instance, row) == "unigramPlus-5.6."


def test_generic_media_frame_with_file_like_controls_is_not_profile_media():
	method = _load_app_method("_profile_media_content_anchor", {})
	settings_frame = SimpleNamespace(
		UIAAutomationId="MediaFrame",
		UIAClassName="SettingsPage",
		parent=None,
	)
	parent = SimpleNamespace(
		UIAAutomationId="ScrollingHost",
		UIAClassName="ListView",
		parent=settings_frame,
	)
	row = SimpleNamespace(parent=parent)
	controls = {
		"Title": SimpleNamespace(name="Theme"),
		"Subtitle": SimpleNamespace(name="Current"),
		"Button": SimpleNamespace(name="Choose"),
	}
	instance = SimpleNamespace(
		_find_descendant=lambda obj, role=None, automation_id=None, max_depth=5: controls.get(
			automation_id, False
		)
	)

	assert method(instance, row) is None


def test_header_toggle_persists_and_announces_both_states():
	state = {"messageHeaderAtTheEnd": False}
	messages = []
	conf = SimpleNamespace(
		get=lambda key: state[key],
		set=lambda key, value: state.__setitem__(key, value),
	)
	method = _load_app_method(
		"script_toggleMessageHeaderAtTheEnd",
		{"conf": conf, "message": messages.append, "_": lambda text: text},
	)

	assert method(SimpleNamespace(), None) is True
	assert state["messageHeaderAtTheEnd"] is True
	assert messages.pop() == "Message headers will be announced after the message content"
	assert method(SimpleNamespace(), None) is False
	assert state["messageHeaderAtTheEnd"] is False
	assert messages.pop() == "Message headers will be announced before the message content"


def test_header_toggle_binds_latin_and_russian_keyboard_layouts():
	method = next(
		node
		for node in _app_class_ast().body
		if isinstance(node, ast.FunctionDef) and node.name == "script_toggleMessageHeaderAtTheEnd"
	)
	gestures = next(
		keyword.value
		for decorator in method.decorator_list
		for keyword in decorator.keywords
		if keyword.arg == "gestures"
	)

	assert [item.value for item in gestures.elts] == ["kb:ALT+[", "kb:ALT+Х"]


def test_header_order_setting_is_exposed_and_defaults_to_headers_first():
	config_source = (ROOT / "addon" / "appModules" / "cnf.py").read_text(encoding="utf-8")
	settings_source = (
		ROOT / "addon" / "GlobalPlugins" / "UnigramPlus" / "__init__.py"
	).read_text(encoding="utf-8-sig")

	assert '"messageHeaderAtTheEnd = boolean(default=False)"' in config_source
	assert '_("Announce message headers after the message content")' in settings_source
	assert 'conf.set("messageHeaderAtTheEnd", self.messageHeaderAtTheEnd.IsChecked())' in settings_source
