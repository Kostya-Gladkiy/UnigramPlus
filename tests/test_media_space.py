"""Space on a message in Unigram 13.1.1, which has no Space action of its own.

Unigram 13.0 turned the content of photo, video, GIF, file, music and voice
messages into the FileButton that opens, plays or downloads it (commits
559a87080, bdbacff06, ed3b7004e, 8aeecd6d3 and 2890366d4), so these messages
lost their "Button" child. 13.0.1 (652d267b0) set AutomationId "Button" on the
content styles again, except that in VoiceNoteContent.xaml it went on the
voice-to-text toggle's style: the voice message's own FileButton has no
AutomationId and the "Button" inside it is that toggle. The same commit named
stickers and link previews "Button", which are hyperlinks. FileButton is a
UIA Button with a Value (the transfer progress) since Unigram 11.5.3.

The upstream proposal for a native Space (IContent.TryInvoke, branch
message-invoke) is not in 13.1.1, so the add-on still presses the button.

An album item (AlbumContent's MessageSelector, a list item) holds just that
content button, so Right and Left Arrow look inside it to name the item.
"""

import ast
import sys
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"

SPACE_METHODS = [
	"_is_media_button",
	"_media_button_opens_viewer",
	"_find_media_button_in_message",
	"script_actionMediaInMessage",
]


def _module():
	return ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))


def _exec(nodes, namespace):
	for node in nodes:
		node.decorator_list = []
	exec(compile(ast.Module(body=nodes, type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace


def _load_functions(names, namespace):
	nodes = [node for node in _module().body if isinstance(node, ast.FunctionDef) and node.name in names]
	return _exec(nodes, namespace)


def _load_app_methods(names, namespace):
	cls = next(node for node in _module().body if isinstance(node, ast.ClassDef) and node.name == "AppModule")
	nodes = [node for node in cls.body if isinstance(node, ast.FunctionDef) and node.name in names]
	_exec(nodes, namespace)
	return [namespace[name] for name in names]


def _node(automation_id="", role="button", width=48, children=(), file_button=False, name=""):
	"""A UIA element. ``file_button`` stands for FileButton's Value pattern."""
	node = SimpleNamespace(
		UIAAutomationId=automation_id,
		role=role,
		name=name,
		location=SimpleNamespace(width=width),
		children=list(children),
		is_file_button=file_button,
		pressed=0,
	)
	node.doAction = lambda: setattr(node, "pressed", node.pressed + 1)
	return node


def _message(*children):
	obj = SimpleNamespace(media=None, children=list(children), focused=0)
	obj.firstChild = children[0] if children else None
	for index, child in enumerate(children):
		child.next = children[index + 1] if index + 1 < len(children) else None
	obj.setFocus = lambda: setattr(obj, "focused", obj.focused + 1)
	return obj


def _press_space(message_item, selection_mode=False, unigram_version="13.1.1.0"):
	sent = []
	namespace = {
		"Role": SimpleNamespace(LINK="link", BUTTON="button", LISTITEM="listitem"),
		"api": SimpleNamespace(getFocusObject=lambda: message_item),
		"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
		"_is_file_button": lambda obj: obj.is_file_button,
	}
	_load_functions(["is_version_greater"], namespace)
	are_links, is_media_button, opens_viewer, find_button, handler = _load_app_methods(
		["_media_buttons_are_links", *SPACE_METHODS], namespace
	)
	instance = SimpleNamespace(
		productVersion=unigram_version,
		is_message_object=lambda obj: True,
		_is_message_selection_mode=lambda obj: selection_mode,
		_toggle_selection=lambda obj: sent.append("toggle"),
		_MEDIA_BUTTON_AUTOMATION_IDS=("Button", "Download"),
		is_exit_from_media=False,
	)
	instance._media_buttons_are_links = lambda: are_links(instance)
	instance._is_media_button = lambda obj: is_media_button(instance, obj)
	instance._media_button_opens_viewer = lambda button, album_item=None: opens_viewer(instance, button, album_item)
	instance._find_media_button_in_message = lambda obj: find_button(instance, obj)
	handler(instance, SimpleNamespace(send=lambda: sent.append("space")))
	return instance, sent


def _voice_message(with_transcription=True):
	children = [_node("Subtitle", role="text")]
	toggle = _node("Button", role="togglebutton", width=28, name="Open transcription")
	if with_transcription:
		children.append(toggle)
	voice = _node("", width=320, children=children, file_button=True)
	return voice, toggle


def test_space_plays_a_voice_message_whose_file_button_has_no_automation_id():
	voice, toggle = _voice_message()
	message_item = _message(voice)

	instance, sent = _press_space(message_item)

	assert voice.pressed == 1, "the voice message itself is its play button"
	assert toggle.pressed == 0, "the voice-to-text toggle is named Button, but it is not the play button"
	assert sent == []
	# It plays where it is, so the focus stays on the message.
	assert message_item.focused == 1
	assert instance.is_exit_from_media is False


def test_space_plays_a_voice_message_without_the_voice_to_text_toggle():
	voice, _ = _voice_message(with_transcription=False)
	message_item = _message(voice)

	_press_space(message_item)

	assert voice.pressed == 1


def test_a_plain_button_without_an_automation_id_is_not_a_voice_message():
	# Inline keyboard buttons have no AutomationId either, but no Value.
	keyboard_button = _node("", width=200)
	message_item = _message(_node("Message", role="text"), keyboard_button)

	_, sent = _press_space(message_item)

	assert keyboard_button.pressed == 0
	assert sent == ["space"]


def test_space_opens_a_photo_in_the_viewer():
	photo = _node("Button", width=320, file_button=True)
	message_item = _message(photo, _node("Message", role="text"))

	instance, sent = _press_space(message_item)

	assert photo.pressed == 1
	assert sent == []
	assert message_item.focused == 0
	assert instance.is_exit_from_media is True, "Escape returns from the viewer to the message"


def test_space_downloads_or_opens_a_file_and_keeps_the_focus_on_the_message():
	# The whole file row is the button now, so its width no longer tells it from a photo.
	document = _node(
		"Button",
		width=320,
		file_button=True,
		children=[_node("Title", role="text", name="report.pdf"), _node("Subtitle", role="text")],
	)
	message_item = _message(document)

	instance, _ = _press_space(message_item)

	assert document.pressed == 1
	assert message_item.focused == 1
	assert instance.is_exit_from_media is False


def test_space_plays_music_with_the_song_itself_not_its_download_button():
	download = _node("Download", width=24, file_button=True)
	song = _node(
		"Button",
		width=320,
		file_button=True,
		children=[download, _node("Title", role="text"), _node("Subtitle", role="text")],
	)
	message_item = _message(song)

	instance, _ = _press_space(message_item)

	assert song.pressed == 1, "the song's own button streams it or downloads it"
	assert download.pressed == 0
	assert instance.is_exit_from_media is False


def test_space_leaves_stickers_to_unigram():
	sticker = _node("Button", role="link", width=180, children=[_node("Player", role="graphic")])
	message_item = _message(sticker)

	_, sent = _press_space(message_item)

	assert sticker.pressed == 0
	assert sent == ["space"]


def test_space_presses_hyperlink_media_buttons_of_unigram_before_11_5_3():
	# FileButton became a UIA Button in 11.5.3; before, every media button was a
	# hyperlink, and stickers and link previews were not named "Button".
	button = _node("Button", role="link", width=48)
	message_item = _message(_node("Message", role="text"), button)

	_, sent = _press_space(message_item, unigram_version="11.5.2.0")

	assert button.pressed == 1
	assert sent == []


def test_an_unreadable_unigram_version_counts_as_a_current_one():
	sticker = _node("Button", role="link", width=180)

	_, sent = _press_space(_message(sticker), unigram_version="")

	assert sticker.pressed == 0
	assert sent == ["space"]


def test_space_keeps_the_focus_on_an_older_album_file_whose_title_is_beside_its_button():
	# Before Unigram 13.0 a file's title sat in the album item next to the button.
	button = _node("Button", width=48, file_button=True)
	album_item = _node("", role="listitem", children=[button, _node("Title", role="text", name="report.pdf")])
	message_item = _message(album_item)

	instance, _ = _press_space(message_item, unigram_version="12.10.7.0")

	assert button.pressed == 1
	assert message_item.focused == 1
	assert instance.is_exit_from_media is False


def test_space_keeps_the_focus_on_an_older_album_file_chosen_with_the_arrows():
	button = _node("Button", width=48, file_button=True)
	album_item = _node("", role="listitem", children=[button, _node("Title", role="text", name="report.pdf")])
	message_item = _message(album_item)
	message_item.media = album_item

	instance, _ = _press_space(message_item, unigram_version="12.10.7.0")

	assert button.pressed == 1
	assert instance.is_exit_from_media is False


def test_space_opens_the_photo_of_a_link_preview_but_not_the_link():
	photo = _node("Button", width=300, file_button=True)
	preview = _node("Button", role="link", width=320, children=[_node("", role="text"), photo])
	message_item = _message(_node("Message", role="text"), preview)

	instance, sent = _press_space(message_item)

	assert preview.pressed == 0, "the link preview is a hyperlink named Button"
	assert photo.pressed == 1
	assert sent == []
	assert instance.is_exit_from_media is True


def test_space_opens_a_narrow_album_photo_in_the_viewer():
	photo = _node("Button", width=96, file_button=True)
	album_item = _node("", role="listitem", width=96, children=[photo])
	message_item = _message(album_item, _node("", role="listitem", children=[_node("Button", file_button=True)]))

	instance, _ = _press_space(message_item)

	assert photo.pressed == 1
	assert instance.is_exit_from_media is True


def test_space_opens_the_album_item_chosen_with_the_arrows():
	first = _node("Button", width=96, file_button=True)
	second = _node("Button", width=96, file_button=True)
	message_item = _message(
		_node("", role="listitem", children=[first]),
		_node("", role="listitem", children=[second]),
	)
	message_item.media = message_item.children[1]

	instance, _ = _press_space(message_item)

	assert (first.pressed, second.pressed) == (0, 1)
	assert instance.is_exit_from_media is True


def test_space_still_selects_in_selection_mode():
	voice, _ = _voice_message()

	_, sent = _press_space(_message(voice), selection_mode=True)

	assert voice.pressed == 0
	assert sent == ["toggle"]


def _album_item_name():
	"""Message_list_item._album_item_name, which Left and Right announce."""
	cls = next(
		node for node in _module().body
		if isinstance(node, ast.ClassDef) and node.name == "Message_list_item"
	)
	nodes = [node for node in cls.body if isinstance(node, ast.FunctionDef) and node.name == "_album_item_name"]
	namespace = _load_functions(["_relative"], {"_": lambda text: f"[{text}]"})
	return _exec(nodes, namespace)["_album_item_name"]


def _album_item(*children):
	"""An album item: a MessageSelector list item around one content control."""
	item = _node("", role="listitem", children=children)
	item.firstChild = children[0] if children else None
	return item


def test_an_album_photo_is_announced_as_a_photo_in_unigram_13():
	name = _album_item_name()

	# Without a download in progress, a photo exposes nothing inside its button.
	assert name(_album_item(_node("Button", file_button=True))) == "[Photo]"
	# The size it shows while downloading is a Subtitle inside the button.
	assert name(_album_item(_node("Button", file_button=True, children=[_node("Subtitle", role="text")]))) == "[Photo]"


def test_an_album_video_is_announced_as_a_video_in_unigram_13():
	video = _node("Button", file_button=True, children=[
		_node("Overlay", file_button=True, children=[_node("Subtitle", role="text")]),
	])

	assert _album_item_name()(_album_item(video)) == "[Video]"


def test_an_album_file_or_song_is_announced_by_its_title_in_unigram_13():
	song = _node("Button", file_button=True, children=[
		_node("Download", file_button=True),
		_node("Title", role="text", name="Track 1"),
		_node("Subtitle", role="text"),
	])

	assert _album_item_name()(_album_item(song)) == "Track 1"


def test_album_items_of_older_unigram_versions_keep_their_names():
	name = _album_item_name()

	assert name(_album_item(_node("Subtitle", role="text"), _node("Button"))) == "[Photo]"
	assert name(_album_item(_node("Texture", role="graphic"), _node("Button"))) == "[Video]"
	assert name(_album_item(_node("Button"), _node("Title", role="text", name="report.pdf"))) == "report.pdf"


def test_a_file_button_is_told_apart_by_its_value_pattern(monkeypatch):
	monkeypatch.setitem(
		sys.modules,
		"UIAHandler",
		SimpleNamespace(UIA=SimpleNamespace(UIA_IsValuePatternAvailablePropertyId="valueAvailable")),
	)
	namespace = _load_functions(["_raw_uia_property", "_is_file_button"], {})
	is_file_button = namespace["_is_file_button"]

	class Element:
		def __init__(self, available):
			self.available = available

		def GetCurrentPropertyValueEx(self, property_id, ignore_default):
			assert property_id == "valueAvailable"
			return self.available

	assert is_file_button(SimpleNamespace(UIAElement=Element(True)))
	assert not is_file_button(SimpleNamespace(UIAElement=Element(False)))
	# Not a UIA object, such as a fake or an IAccessible window.
	assert not is_file_button(SimpleNamespace())
