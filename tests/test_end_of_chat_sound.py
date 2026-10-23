import ast
import os
import sys
from pathlib import Path
from types import MethodType, SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"


def _source_module():
	return ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))


def _load_end_of_chat_sound_functions(namespace):
	functions = {
		node.name: node
		for node in _source_module().body
		if isinstance(node, ast.FunctionDef)
		and node.name in {"_get_end_of_chat_sound_path", "play_end_of_chat_sound"}
	}
	exec(
		compile(
			ast.Module(
				body=[
					functions["_get_end_of_chat_sound_path"],
					functions["play_end_of_chat_sound"],
				],
				type_ignores=[],
			),
			str(SOURCE_PATH),
			"exec",
		),
		namespace,
	)
	return namespace["play_end_of_chat_sound"]


def _load_message_list_item(namespace):
	message_class = next(
		node
		for node in _source_module().body
		if isinstance(node, ast.ClassDef) and node.name == "Message_list_item"
	)
	exec(
		compile(ast.Module(body=[message_class], type_ignores=[]), str(SOURCE_PATH), "exec"),
		namespace,
	)
	return namespace["Message_list_item"]


def _load_app_methods(names, namespace):
	app_module = next(
		node
		for node in _source_module().body
		if isinstance(node, ast.ClassDef) and node.name == "AppModule"
	)
	methods = []
	for name in names:
		method = next(
			node
			for node in app_module.body
			if isinstance(node, ast.FunctionDef) and node.name == name
		)
		method.decorator_list = []
		methods.append(method)
	exec(
		compile(ast.Module(body=methods, type_ignores=[]), str(SOURCE_PATH), "exec"),
		namespace,
	)
	return {name: namespace[name] for name in names}


def _bind_methods(instance, methods):
	for name, method in methods.items():
		setattr(instance, name, MethodType(method, instance))
	return instance


class _UIAElement:
	def __init__(self, runtime_id, properties=None):
		self.runtime_id = tuple(runtime_id)
		self.properties = properties or {}

	def GetRuntimeId(self):
		return self.runtime_id

	def GetCurrentPropertyValueEx(self, property_id, _ignore_default):
		return self.properties.get(property_id)


class _Node:
	def __init__(
		self,
		runtime_id,
		*,
		parent=None,
		automation_id="",
		position_info=None,
		properties=None,
		states=(),
		location=None,
		name="",
	):
		self.UIAElement = _UIAElement(runtime_id, properties)
		self.parent = parent
		self.UIAAutomationId = automation_id
		self.positionInfo = position_info if position_info is not None else {}
		self.states = set(states)
		self.location = location or SimpleNamespace(width=100, height=30)
		self.name = name
		self.lastChild = None


def _endpoint_nodes(
	*, prefix="current", position_info=None, properties=None, messages_properties=None
):
	messages = _Node(
		(prefix, "messages"),
		automation_id="Messages",
		properties=messages_properties,
	)
	row = _Node(
		(prefix, "row"),
		parent=messages,
		position_info=position_info,
		properties=properties,
	)
	focus = _Node((prefix, "message"), parent=row, automation_id="Message_item")
	messages.lastChild = row
	return messages, row, focus


def _button(*, hidden):
	return _Node(
		("messages-button",),
		states=("offscreen",) if hidden else (),
		location=SimpleNamespace(width=0 if hidden else 30, height=30),
	)


def _make_endpoint_app(messages, focus, button, settings=None):
	settings = settings or {
		"play_end_of_chat_sound": True,
		"action_when_pressing_up_arrow_in_text_field": "normal",
	}
	api_state = {"foreground": object(), "focus": focus}
	sounds = []
	moves = []
	namespace = {
		"api": SimpleNamespace(
			getForegroundObject=lambda: api_state["foreground"],
			getFocusObject=lambda: api_state["focus"],
		),
		"Role": SimpleNamespace(BUTTON="button"),
		"State": SimpleNamespace(OFFSCREEN="offscreen"),
		"conf": SimpleNamespace(get=lambda key: settings[key]),
		"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
		"_normalized_text": lambda text: str(text or "").strip().casefold(),
		"play_end_of_chat_sound": lambda: sounds.append(True),
		"_END_OF_CHAT_PROBE_DELAY_MS": 50,
	}
	scheduled = _install_fake_poller(namespace)
	method_names = (
		"is_message_object",
		"_same_uia_element",
		"_get_current_message_row_and_list",
		"_messages_button_visibility",
		"_get_end_of_chat_candidate",
		"_get_end_of_chat_state",
		"_is_last_message_in_chat",
		"_schedule_end_of_chat_confirmation",
		"_confirm_end_of_chat",
		"_apply_end_of_chat_result",
	)
	app = _bind_methods(SimpleNamespace(), _load_app_methods(method_names, namespace))
	app._endOfChatProbeGeneration = 0
	app.getMessagesElement = lambda: messages
	app._messagesButton = button
	app._find_descendant = lambda *args, **kwargs: (_ for _ in ()).throw(
		AssertionError("end-of-chat checks must not walk the foreground UIA tree")
	)
	app.script_moveFocusToTextMessage = lambda gesture: moves.append(gesture)
	app._scheduled_probes = scheduled
	return app, api_state, settings, sounds, moves


def _install_fake_poller(namespace):
	"""Capture what the endpoint probe hands to the shared background poller.

	The probe walks the message ancestry, so it must not run on NVDA's main
	loop; the sound and the focus move it produces must go back to it.
	"""
	scheduled = []
	namespace["_BackgroundPoller"] = SimpleNamespace(
		schedule=lambda key, delay, callback: scheduled.append(
			(round(delay * 1000), callback, ())
		),
		cancel=lambda key: None,
	)
	namespace["queueHandler"] = SimpleNamespace(
		eventQueue=object(),
		queueFunction=lambda queue, callback, *args: callback(*args),
	)
	return scheduled


def test_end_of_chat_sound_respects_setting_and_prefers_user_override(tmp_path):
	played = []
	enabled = {"value": True}
	base_dir = os.path.join("bundled", "media")
	custom_sound = tmp_path / "UnigramEndOfChat.wav"
	custom_sound.write_bytes(b"custom wave")
	namespace = {
		"os": os,
		"globalVars": SimpleNamespace(appArgs=SimpleNamespace(configPath=str(tmp_path))),
		"_END_OF_CHAT_SOUND_FILENAME": "EndOfChatDefault.wav",
		"_END_OF_CHAT_CUSTOM_SOUND_FILENAME": "UnigramEndOfChat.wav",
		"baseDir": base_dir,
		"conf": SimpleNamespace(get=lambda key: enabled["value"]),
		"winsound": SimpleNamespace(
			SND_FILENAME=1,
			SND_ASYNC=2,
			PlaySound=lambda *args: played.append(args),
		),
		"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
	}
	play = _load_end_of_chat_sound_functions(namespace)

	assert play()
	assert played == [(str(custom_sound), 3)]

	custom_sound.unlink()
	assert play()
	assert played[-1] == (os.path.join(base_dir, "EndOfChatDefault.wav"), 3)

	enabled["value"] = False
	assert not play()
	assert len(played) == 2


def test_candidate_uses_realized_last_row_like_russian_mod():
	messages, row, focus = _endpoint_nodes(
		# This simulates an overlay's stale construction-time metadata.
		position_info={"indexInGroup": 9, "similarItemsInGroup": 10},
		properties={1: 10, 2: 10},
	)
	button = _button(hidden=True)
	app, _api_state, _settings, _sounds, _moves = _make_endpoint_app(
		messages, focus, button
	)

	candidate = app._get_end_of_chat_candidate(focus)
	assert candidate == (messages, row)
	assert app._get_end_of_chat_state(focus) is True

	# Button state is intentionally irrelevant to the RussianMod endpoint rule.
	button.states.clear()
	button.location = SimpleNamespace(width=30, height=30)
	assert app._get_end_of_chat_state(focus) is True

	# RussianMod does not trust PositionInSet because Unigram virtualizes its
	# loaded history. Direct last-row identity remains the core signal.
	row.UIAElement.properties = {1: 9, 2: 10}
	assert app._get_end_of_chat_candidate(focus) is not None


def test_candidate_prefers_current_ancestor_over_stale_cached_messages():
	current_messages = _Node(("current", "messages"), automation_id="Messages")
	current_row = _Node(("current", "row"), parent=current_messages, name="current")
	wrapper = _Node(("current", "wrapper"), parent=current_row)
	focus = _Node(
		("current", "message"),
		parent=wrapper,
		automation_id="Message_item",
	)
	current_messages.lastChild = current_row

	stale_messages, _stale_row, _stale_focus = _endpoint_nodes(prefix="stale")
	app, _api_state, _settings, _sounds, _moves = _make_endpoint_app(
		stale_messages, focus, None
	)

	assert app._get_end_of_chat_candidate(focus) == (current_messages, current_row)


def test_candidate_falls_back_to_message_text_when_uia_ancestry_is_broken():
	messages = _Node(("messages",), automation_id="Messages")
	last_row = _Node(
		("last-row",),
		parent=messages,
		name="Sender\r\nA sufficiently long final message used for endpoint matching",
	)
	messages.lastChild = last_row
	broken_parent = _Node(("broken-parent",), name="unrelated wrapper")
	focus = _Node(
		("focus",),
		parent=broken_parent,
		automation_id="Message_item",
		name="A sufficiently long final message used for endpoint matching",
	)
	app, _api_state, _settings, _sounds, _moves = _make_endpoint_app(
		messages, focus, None
	)

	assert app._get_end_of_chat_candidate(focus) == (messages, broken_parent)

	# Short repeated labels are too ambiguous for the degraded text-only path.
	focus.name = "Today"
	last_row.name = "Today"
	assert app._get_end_of_chat_candidate(focus) is None


def test_confirmation_is_tied_to_the_original_row():
	messages, row, focus = _endpoint_nodes()
	button = _button(hidden=False)
	settings = {
		"play_end_of_chat_sound": True,
		"action_when_pressing_up_arrow_in_text_field": "to_messages",
	}
	app, _api_state, _settings, sounds, moves = _make_endpoint_app(
		messages, focus, button, settings
	)
	scheduled = app._scheduled_probes

	assert app._schedule_end_of_chat_confirmation(focus, move_focus_to_text=True)
	assert scheduled[0][0] == 50
	_, callback, args = scheduled[0]
	callback(*args)
	assert sounds == [True]
	assert moves == [None]


def test_confirmation_matches_russian_mod_when_auxiliary_states_are_unavailable():
	messages, _row, focus = _endpoint_nodes()
	app, _api_state, _settings, sounds, _moves = _make_endpoint_app(
		messages, focus, None
	)
	scheduled = app._scheduled_probes

	assert app._schedule_end_of_chat_confirmation(focus)
	_, callback, args = scheduled[0]
	callback(*args)
	assert sounds == [True]
	assert len(scheduled) == 1


def test_scheduling_an_end_probe_does_not_read_uia_before_down_returns():
	messages, _row, focus = _endpoint_nodes()
	app, _api_state, _settings, _sounds, _moves = _make_endpoint_app(
		messages, focus, None
	)
	scheduled = app._scheduled_probes
	app._get_end_of_chat_candidate = lambda *args: (_ for _ in ()).throw(
		AssertionError("scheduling must not inspect UIA")
	)

	assert app._schedule_end_of_chat_confirmation(focus)
	assert scheduled[0][0] == 50


def test_confirmation_cancels_when_source_is_not_slice_final():
	messages, row, focus = _endpoint_nodes()
	button = _button(hidden=True)
	app, _api_state, _settings, sounds, _moves = _make_endpoint_app(messages, focus, button)
	scheduled = app._scheduled_probes

	# Ordinary navigation may schedule a cheap callback, but it must not read the
	# UIA tree or play a sound when the source is no longer the slice's last row.
	messages.lastChild = _Node(("different-row",), parent=messages)
	assert app._schedule_end_of_chat_confirmation(focus)
	_, callback, args = scheduled[0]
	callback(*args)
	assert sounds == []


def test_down_arrow_reads_settings_at_use_time_and_preserves_native_navigation():
	scheduled = []
	native_gestures = []
	events = []
	settings = {
		"play_end_of_chat_sound": False,
		"action_when_pressing_up_arrow_in_text_field": "normal",
	}

	class ListItem:
		pass

	def script(**_kwargs):
		return lambda function: function

	message_class = _load_message_list_item(
		{
			"ListItem": ListItem,
			"script": script,
			"_": lambda text: text,
			"message": lambda text: None,
			"conf": SimpleNamespace(get=lambda key: settings[key]),
		}
	)
	item = message_class()
	item.appModule = SimpleNamespace(
		_schedule_end_of_chat_confirmation=lambda source, move: scheduled.append(
			(source, move)
		) or events.append("schedule"),
	)
	gesture = SimpleNamespace(send=lambda: native_gestures.append(True) or events.append("send"))

	item.script_next_message(gesture)
	assert scheduled == []
	assert native_gestures == [True]

	# The binding is permanent, but the settings are evaluated for every press,
	# so enabling it does not require a new message overlay.
	settings["play_end_of_chat_sound"] = True
	item.script_next_message(gesture)
	assert scheduled == [(item, False)]
	assert native_gestures == [True, True]
	assert events[-2:] == ["send", "schedule"]

	settings["play_end_of_chat_sound"] = False
	settings["action_when_pressing_up_arrow_in_text_field"] = "to_messages"
	item.script_next_message(gesture)
	assert scheduled[-1] == (item, True)
	assert native_gestures == [True, True, True]

	source = SOURCE_PATH.read_text(encoding="utf-8")
	assert 'self.bindGesture("kb:downArrow", "next_message")' in source


def test_alt_2_prioritizes_the_cached_go_to_bottom_button():
	actions = []
	method = _load_app_methods(
		("script_toLastMessage",),
		{"api": SimpleNamespace(getFocusObject=lambda: (_ for _ in ()).throw(AssertionError("fallback")))},
	)["script_toLastMessage"]
	button = SimpleNamespace(doAction=lambda: actions.append(True))
	instance = SimpleNamespace(
		_messagesButton=button,
		_messages_button_visibility=lambda: True,
		_find_descendant=lambda *args: (_ for _ in ()).throw(AssertionError("tree walk")),
	)

	assert method(instance, None) is True
	assert actions == [True]


def test_alt_2_at_a_confirmed_last_message_plays_the_sound():
	sounds = []
	announcements = []
	sent = []
	probes = []
	focus = SimpleNamespace(name="Last message")
	method = _load_app_methods(
		("script_toLastMessage",),
		{
			"api": SimpleNamespace(getFocusObject=lambda: focus),
			"play_end_of_chat_sound": lambda: sounds.append(True),
			"message": announcements.append,
			"KeyboardInputGesture": SimpleNamespace(
				fromName=lambda name: SimpleNamespace(send=lambda: sent.append(name))
			),
			"_": lambda text: text,
		},
	)["script_toLastMessage"]
	endpoint = {"value": True}
	instance = SimpleNamespace(
		is_message_object=lambda obj: obj is focus,
		_is_last_message_in_chat=lambda obj: endpoint["value"],
		_schedule_end_of_chat_confirmation=lambda source: probes.append(source),
	)

	assert method(instance, None)
	assert sounds == [True]
	assert announcements == ["Last message"]
	assert sent == []

	endpoint["value"] = False
	assert method(instance, None)
	assert sounds == [True]
	assert sent == ["end"]
	assert probes == [focus]


def test_blank_service_messages_receive_the_message_overlay():
	source = SOURCE_PATH.read_text(encoding="utf-8")
	assert "if obj.role == Role.LISTITEM and obj.isFocusable:" in source
	assert '_is_message_list_item(obj)' in source
	assert 'automation_id == "Message_item"' in source
	assert '("Messages",), max_depth=8' in source


def test_end_of_chat_sound_setting_is_enabled_by_default_and_persisted():
	config_source = (ROOT / "addon" / "appModules" / "cnf.py").read_text(encoding="utf-8")
	settings_source = (
		ROOT / "addon" / "GlobalPlugins" / "UnigramPlus" / "__init__.py"
	).read_text(encoding="utf-8-sig")

	assert '"play_end_of_chat_sound = boolean(default=True)"' in config_source
	assert '_("Play a sound when reaching the end of a chat")' in settings_source
	assert 'conf.set("play_end_of_chat_sound", self.play_end_of_chat_sound.IsChecked())' in settings_source
