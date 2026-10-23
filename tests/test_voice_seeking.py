import ast
from pathlib import Path
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"


def _app_class_ast():
	module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
	return next(node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule")


def _load_methods(names, namespace):
	methods = [
		node for node in _app_class_ast().body if isinstance(node, ast.FunctionDef) and node.name in names
	]
	for method in methods:
		method.decorator_list = []
	exec(
		compile(ast.Module(body=methods, type_ignores=[]), str(SOURCE_PATH), "exec"),
		namespace,
	)
	return [namespace[name] for name in names]


class _SavedItems:
	def __init__(self, slider=None):
		self.slider = slider
		self.saved = []

	def get(self, key):
		assert key == "slider"
		return self.slider

	def save(self, key, value):
		assert key == "slider"
		self.slider = value
		self.saved.append(value)


def _slider(width=200, role="unknown", name="Seek"):
	return SimpleNamespace(
		role=role,
		UIAAutomationId="Slider",
		name=name,
		location=SimpleNamespace(width=width),
		setFocus=lambda: None,
	)


def _node(*children):
	return SimpleNamespace(
		role="window",
		UIAAutomationId="Window",
		name="",
		location=SimpleNamespace(width=800),
		children=list(children),
	)


def _load_slider_helpers():
	namespace = {"Role": SimpleNamespace(SLIDER="slider")}
	return _load_methods(
		["_is_visible_playback_slider", "_get_playback_slider"],
		namespace,
	)


def test_current_custom_role_playback_slider_is_discovered_and_cached():
	is_visible, get_slider = _load_slider_helpers()
	current = _slider(role="unknown")
	saved = _SavedItems()
	instance = SimpleNamespace(
		saved_items=saved,
		getElements=lambda: [SimpleNamespace(UIAAutomationId="Other"), current],
		_is_visible_playback_slider=lambda obj: is_visible(None, obj),
	)

	assert get_slider(instance) is current
	assert saved.saved == [current]


def test_hidden_cached_slider_is_replaced_by_the_live_slider():
	is_visible, get_slider = _load_slider_helpers()
	stale = _slider(width=0)
	current = _slider(width=300, role="unknown")
	saved = _SavedItems(stale)
	instance = SimpleNamespace(
		saved_items=saved,
		getElements=lambda: [current],
		_is_visible_playback_slider=lambda obj: is_visible(None, obj),
	)

	assert get_slider(instance) is current
	assert saved.saved == [current]


def test_stale_cached_slider_exception_is_replaced():
	class StaleSlider:
		UIAAutomationId = "Slider"
		name = "Seek"
		role = "unknown"

		@property
		def location(self):
			raise RuntimeError("element no longer available")

	is_visible, get_slider = _load_slider_helpers()
	current = _slider(role="unknown")
	saved = _SavedItems(StaleSlider())
	instance = SimpleNamespace(
		saved_items=saved,
		getElements=lambda: [current],
		_is_visible_playback_slider=lambda obj: is_visible(None, obj),
	)

	assert get_slider(instance) is current
	assert saved.saved == [current]


def test_nested_current_playback_slider_is_discovered():
	is_visible, get_slider = _load_slider_helpers()
	current = _slider(role="unknown")
	saved = _SavedItems()
	instance = SimpleNamespace(
		saved_items=saved,
		getElements=lambda: [_node(_node(current))],
		_is_visible_playback_slider=lambda obj: is_visible(None, obj),
	)

	assert get_slider(instance) is current
	assert saved.saved == [current]


@pytest.mark.parametrize("direction", ["rightArrow", "leftArrow"])
def test_voice_seek_uses_current_slider_and_restores_playback_and_focus(direction):
	events = []
	messages = []
	focus = SimpleNamespace(setFocus=lambda: events.append("restoreFocus"))
	slider = _slider(role="unknown")
	slider.setFocus = lambda: events.append("sliderFocus")

	class Gesture:
		def send(self):
			events.append(direction)

	_, _, rewind = _load_methods(
		["_is_visible_playback_slider", "_get_playback_slider", "rewind_voice_message"],
		{
			"Role": SimpleNamespace(SLIDER="slider"),
			"message": messages.append,
			"_": lambda text: text,
			"api": SimpleNamespace(getFocusObject=lambda: focus),
			"KeyboardInputGesture": SimpleNamespace(fromName=lambda name: Gesture()),
			"speech": SimpleNamespace(cancelSpeech=lambda: events.append("cancelSpeech")),
		},
	)
	instance = SimpleNamespace(
		_get_playback_slider=lambda: slider,
		_send_key_without_held_modifiers=lambda key: events.append(key),
	)

	assert rewind(instance, direction) is True
	assert events == [
		"sliderFocus",
		direction,
		"restoreFocus",
		"cancelSpeech",
	]
	assert messages == []


def test_voice_seek_without_a_visible_slider_reports_once_and_sends_nothing():
	messages = []
	events = []
	_, _, rewind = _load_methods(
		["_is_visible_playback_slider", "_get_playback_slider", "rewind_voice_message"],
		{
			"Role": SimpleNamespace(SLIDER="slider"),
			"message": messages.append,
			"_": lambda text: text,
			"api": SimpleNamespace(getFocusObject=lambda: None),
			"KeyboardInputGesture": SimpleNamespace(fromName=lambda name: events.append(name)),
			"speech": SimpleNamespace(cancelSpeech=lambda: events.append("cancel")),
		},
	)
	instance = SimpleNamespace(
		_get_playback_slider=lambda: None,
	)

	assert rewind(instance, "rightArrow") is False
	assert messages == ["Nothing is playing right now"]
	assert events == []


def test_voice_seek_restores_focus_and_reports_once_when_slider_turns_stale():
	messages = []
	events = []
	focus = SimpleNamespace(setFocus=lambda: events.append("restore"))
	slider = _slider(role="unknown")
	slider.setFocus = lambda: (_ for _ in ()).throw(RuntimeError("stale"))
	_, _, rewind = _load_methods(
		["_is_visible_playback_slider", "_get_playback_slider", "rewind_voice_message"],
		{
			"Role": SimpleNamespace(SLIDER="slider"),
			"message": messages.append,
			"_": lambda text: text,
			"api": SimpleNamespace(getFocusObject=lambda: focus),
			"KeyboardInputGesture": SimpleNamespace(fromName=lambda name: None),
			"speech": SimpleNamespace(cancelSpeech=lambda: events.append("cancel")),
			"log": SimpleNamespace(debug=lambda *args: events.append("logged")),
		},
	)
	instance = SimpleNamespace(
		_get_playback_slider=lambda: slider,
		_send_key_without_held_modifiers=lambda key: events.append(key),
	)

	assert rewind(instance, "rightArrow") is False
	assert events == ["logged", "restore"]
	assert messages == ["Nothing is playing right now"]


def test_playback_slider_detection_keeps_legacy_slider_role_compatibility():
	is_visible, _get_slider = _load_slider_helpers()
	legacy = _slider(role="slider", name="")

	assert is_visible(None, legacy)


def test_voice_seek_lifts_the_modifiers_the_user_is_holding():
	"""Ctrl+Alt+Left/Right did nothing because the modifiers stayed down.

	Unigram's Seek slider accepts a bare arrow key. NVDA's send() leaves the
	modifiers the user physically holds pressed, so the app saw Ctrl+Alt+Left
	and ignored it.
	"""
	events = []
	codes = {"ctrl": 17, "alt": 18, "shift": 16, "lwin": 91, "rwin": 92}
	state = {codes["ctrl"]: True, codes["alt"]: True}

	def key_state(code):
		return 32768 if state.get(code) else 0

	def keybd_event(code, scan, flags, extra):
		if flags & 2:
			state[code] = False
			events.append(("up", code))
		else:
			state[code] = True
			events.append(("down", code))

	win_user = SimpleNamespace(
		VK_CONTROL=codes["ctrl"],
		VK_MENU=codes["alt"],
		VK_SHIFT=codes["shift"],
		VK_LWIN=codes["lwin"],
		VK_RWIN=codes["rwin"],
		# getKeyState answers from this thread's queue, which never saw these
		# keystrokes; reading it instead of the async state finds nothing held.
		getKeyState=lambda code: 0,
		getAsyncKeyState=key_state,
		keybd_event=keybd_event,
	)

	class Gesture:
		def send(self):
			# What the app really sees at this moment.
			events.append(("key", tuple(sorted(c for c, held in state.items() if held))))

	(send_key,) = _load_methods(
		["_send_key_without_held_modifiers"],
		{
			"winUser": win_user,
			"_KEYEVENTF_KEYUP": 2,
			"KeyboardInputGesture": SimpleNamespace(fromName=lambda name: Gesture()),
		},
	)
	instance = SimpleNamespace(_MODIFIER_KEYS=("VK_CONTROL", "VK_MENU", "VK_SHIFT", "VK_LWIN", "VK_RWIN"))

	send_key(instance, "leftArrow")

	key_events = [event for event in events if event[0] == "key"]
	assert key_events == [("key", ())], "the arrow must arrive with no modifier held"
	assert state[codes["ctrl"]] and state[codes["alt"]], "modifiers must be put back"
	assert not state.get(codes["shift"]), "a modifier the user never held must stay up"


def test_seeking_focuses_the_slider_and_restores_the_previous_focus():
	events = []
	messages = []
	focus = SimpleNamespace(setFocus=lambda: events.append("restoreFocus"))
	slider = _slider(role="unknown")
	slider.setFocus = lambda: events.append("sliderFocus")
	(rewind,) = _load_methods(
		["rewind_voice_message"],
		{
			"message": messages.append,
			"_": lambda text: text,
			"api": SimpleNamespace(getFocusObject=lambda: focus),
			"speech": SimpleNamespace(cancelSpeech=lambda: events.append("cancelSpeech")),
		},
	)
	instance = SimpleNamespace(
		_get_playback_slider=lambda: slider,
		_send_key_without_held_modifiers=lambda key: events.append(key),
	)

	assert rewind(instance, "rightArrow") is True
	assert events == ["sliderFocus", "rightArrow", "restoreFocus", "cancelSpeech"]
	assert messages == []


def _player_button(automation_id="", role="button", glyph=None, name=""):
	child = SimpleNamespace(name=glyph) if glyph is not None else None
	return SimpleNamespace(
		UIAAutomationId=automation_id,
		role=role,
		name=name,
		firstChild=child,
	)


def _load_close_button_lookup(elements):
	namespace = {
		"Role": SimpleNamespace(BUTTON="button"),
		"icons_in_audio_player": {"close": ""},
	}
	(lookup,) = _load_methods(["_get_audio_player_close_button"], namespace)
	instance = SimpleNamespace(getElements=lambda: elements)
	return lambda: lookup(instance)


def test_close_audio_player_finds_the_button_by_its_icon():
	"""Current Unigram has no ShuffleButton, which the old lookup anchored on."""
	close = _player_button(glyph="", name="Close audio player")
	elements = [
		_player_button(automation_id="PreviousButton", glyph=""),
		_player_button(automation_id="PlaybackButton", glyph=""),
		_player_button(automation_id="SpeedButton", name="Speed"),
		close,
	]

	assert _load_close_button_lookup(elements)() is close


def test_close_audio_player_reports_nothing_playing_when_no_player_is_open():
	# The close glyph alone is not enough: without PlaybackButton no player is up.
	elements = [_player_button(glyph="", name="Close something else")]

	assert _load_close_button_lookup(elements)() is None


def test_close_audio_player_ignores_buttons_that_carry_an_automation_id():
	labelled = _player_button(automation_id="Close", glyph="", name="Close Unigram")
	elements = [_player_button(automation_id="PlaybackButton", glyph=""), labelled]

	assert _load_close_button_lookup(elements)() is None


def _message(children, media=None):
	obj = SimpleNamespace(media=media, children=children)
	obj.firstChild = children[0] if children else None
	for index, child in enumerate(children):
		child.next = children[index + 1] if index + 1 < len(children) else None
		child.previous = children[index - 1] if index else None
	obj.setFocus = lambda: obj.__dict__.setdefault("focused", True)
	return obj


def _media_child(automation_id="", role="button", width=48):
	return SimpleNamespace(
		UIAAutomationId=automation_id,
		role=role,
		location=SimpleNamespace(width=width),
	)


def _load_space_handler(namespace_extra=None):
	namespace = {
		"Role": SimpleNamespace(LINK="link", BUTTON="button", LISTITEM="listitem"),
		"api": SimpleNamespace(getFocusObject=lambda: namespace["_focus"]),
		"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
		"_is_file_button": lambda obj: getattr(obj, "is_file_button", False),
	}
	namespace.update(namespace_extra or {})
	is_media_button, opens_viewer, find_button, handler = _load_methods(
		[
			"_is_media_button",
			"_media_button_opens_viewer",
			"_find_media_button_in_message",
			"script_actionMediaInMessage",
		],
		namespace,
	)
	return namespace, (is_media_button, opens_viewer, find_button), handler


def _space_instance(namespace, methods, is_message=True, selection_mode=False, links=False):
	"""``links`` stands for Unigram before 11.5.3, whose media buttons were links."""
	is_media_button, opens_viewer, find_button = methods
	instance = SimpleNamespace(
		is_message_object=lambda obj: is_message,
		_is_message_selection_mode=lambda obj: selection_mode,
		_media_buttons_are_links=lambda: links,
		_MEDIA_BUTTON_AUTOMATION_IDS=("Button", "Download"),
		is_exit_from_media=False,
	)
	instance._is_media_button = lambda obj: is_media_button(instance, obj)
	instance._media_button_opens_viewer = lambda button, album_item=None: opens_viewer(instance, button, album_item)
	instance._find_media_button_in_message = lambda obj: find_button(instance, obj)
	return instance


def test_space_plays_media_without_toggling_the_message():
	"""Unigram exposes a message as a ToggleButton, so Space would select it.

	The old handler passed Space on and then refused to act because that
	selection had changed the message state, which is why voice messages and
	music stopped playing.
	"""
	invoked = []
	sent = []
	button = _media_child(automation_id="Button")
	button.doAction = lambda: invoked.append("play")
	message_item = _message([button, _media_child(automation_id="Progress", role="custom")])
	namespace, methods, handler = _load_space_handler()
	namespace["_focus"] = message_item
	instance = _space_instance(namespace, methods)

	handler(instance, SimpleNamespace(send=lambda: sent.append("space")))

	assert invoked == ["play"], "the play button must be pressed"
	assert sent == [], "Space must not reach Unigram and select the message"


def test_space_selects_a_media_message_in_selection_mode_instead_of_playing_it():
	"""In Unigram's selection mode Space selects or unselects the message."""
	invoked = []
	toggled = []
	button = _media_child(automation_id="Button")
	button.doAction = lambda: invoked.append("play")
	message_item = _message([button])
	namespace, methods, handler = _load_space_handler()
	namespace["_focus"] = message_item
	instance = _space_instance(namespace, methods, selection_mode=True)
	instance._toggle_selection = toggled.append

	handler(instance, SimpleNamespace(send=lambda: invoked.append("space")))

	assert toggled == [message_item]
	assert invoked == []


def test_space_is_passed_through_when_the_message_has_nothing_to_play():
	sent = []
	message_item = _message([_media_child(automation_id="TextBlock", role="text")])
	namespace, methods, handler = _load_space_handler()
	namespace["_focus"] = message_item
	instance = _space_instance(namespace, methods)

	handler(instance, SimpleNamespace(send=lambda: sent.append("space")))

	assert sent == ["space"]


def test_space_outside_a_message_keeps_its_normal_behavior():
	sent = []
	namespace, methods, handler = _load_space_handler()
	namespace["_focus"] = SimpleNamespace()
	instance = _space_instance(namespace, methods, is_message=False)

	handler(instance, SimpleNamespace(send=lambda: sent.append("space")))

	assert sent == ["space"]


def test_the_seek_shortcut_still_works_while_the_modifiers_stay_held():
	"""Holding Ctrl+Alt and tapping the arrow again must keep seeking.

	The modifiers have to be pressed back after the arrow. Leaving them up while
	the user still holds them means the next arrow arrives on its own, so NVDA
	never recognizes the shortcut again.
	"""
	codes = {"ctrl": 17, "alt": 18, "shift": 16, "lwin": 91, "rwin": 92}
	physical = {codes["ctrl"]: True, codes["alt"]: True}
	seen = []

	def keybd_event(code, scan, flags, extra):
		physical[code] = not (flags & 2)

	win_user = SimpleNamespace(
		VK_CONTROL=codes["ctrl"],
		VK_MENU=codes["alt"],
		VK_SHIFT=codes["shift"],
		VK_LWIN=codes["lwin"],
		VK_RWIN=codes["rwin"],
		getKeyState=lambda code: 0,
		getAsyncKeyState=lambda code: 32768 if physical.get(code) else 0,
		keybd_event=keybd_event,
	)

	class Gesture:
		def send(self):
			seen.append(tuple(sorted(c for c, held in physical.items() if held)))

	(send_key,) = _load_methods(
		["_send_key_without_held_modifiers"],
		{
			"winUser": win_user,
			"_KEYEVENTF_KEYUP": 2,
			"KeyboardInputGesture": SimpleNamespace(fromName=lambda name: Gesture()),
		},
	)
	instance = SimpleNamespace(_MODIFIER_KEYS=("VK_CONTROL", "VK_MENU", "VK_SHIFT", "VK_LWIN", "VK_RWIN"))

	# The user holds Ctrl+Alt throughout and taps the arrow three times.
	for _ in range(3):
		send_key(instance, "rightArrow")

	assert seen == [(), (), ()], "every arrow must arrive with no modifier held"
	assert physical[codes["ctrl"]] and physical[codes["alt"]], (
		"the modifiers must be held again after each press, or the shortcut stops repeating"
	)


@pytest.mark.parametrize(
	"role, links",
	[("link", True), ("button", False)],
	ids=["link before Unigram 11.5.3", "button since 11.5.3"],
)
def test_space_plays_a_music_or_file_message_whose_button_is_named_download(role, links):
	invoked = []
	sent = []
	button = _media_child(automation_id="Download", role=role)
	button.doAction = lambda: invoked.append("play")
	message_item = _message([_media_child(automation_id="PhotoRoot", role="link"), button])
	namespace, methods, handler = _load_space_handler()
	namespace["_focus"] = message_item
	instance = _space_instance(namespace, methods, links=links)

	handler(instance, SimpleNamespace(send=lambda: sent.append("space")))

	assert invoked == ["play"]
	assert sent == []
