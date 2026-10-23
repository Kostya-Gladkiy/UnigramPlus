import ast
import time
from pathlib import Path
import sys
from types import SimpleNamespace


ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "addon" / "appModules"))

from voice_recording import (  # noqa: E402
	VoiceRecordingOutcome,
	VoiceRecordingState,
	is_recorded_message,
	is_recording_button,
	message_marker,
	recording_button_state,
)


def _app_module_ast():
	source = (ROOT / "addon" / "appModules" / "unigram.py").read_text(encoding="utf-8")
	module = ast.parse(source)
	return next(node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule")


def _method_source(name):
	method = next(
		node
		for node in _app_module_ast().body
		if isinstance(node, ast.FunctionDef) and node.name == name
	)
	return ast.unparse(method)


def _load_method(name, namespace):
	method = next(
		node
		for node in _app_module_ast().body
		if isinstance(node, ast.FunctionDef) and node.name == name
	)
	method.decorator_list = []
	exec(compile(ast.Module(body=[method], type_ignores=[]), "unigram.py", "exec"), namespace)
	return namespace[name]


def test_native_recording_shortcuts_are_not_bound_or_intercepted_by_unigramplus():
	app_module = _app_module_ast()
	legacy_scripts = {
		"script_recordingVoiceMessage",
		"script_cancelVoiceMessageRecording",
	}
	recording_scripts = {
		node.name
		for node in app_module.body
		if isinstance(node, ast.FunctionDef) and node.name in legacy_scripts
	}
	serialized = ast.dump(app_module).casefold()

	assert recording_scripts == set()
	assert "control+r" not in serialized
	assert "control+d" not in serialized


def test_native_recording_ui_events_produce_one_start_and_one_stop():
	state = VoiceRecordingState()

	assert state.shown() == "start"
	assert state.elapsedChanged("0:00,00") is None
	assert state.elapsedChanged("0:00.10") is None
	assert state.elapsedChanged("0:01.25") is None
	assert state.elapsedChanged("0:00,0") == "stopped"
	assert state.hidden() is None
	assert state.elapsedChanged("0:00,0") is None


def test_name_changes_work_when_uia_show_event_is_missing():
	state = VoiceRecordingState()

	assert state.elapsedChanged("0:00.10") == "start"
	assert state.elapsedChanged("0:00.00") == "stopped"


def test_hiding_timer_defers_the_send_outcome():
	state = VoiceRecordingState()

	assert state.shown() == "start"
	assert state.elapsedChanged("0:01.25") is None
	assert state.hidden() == "stopped"
	assert not state.active


def test_recorded_message_templates_and_message_markers_are_detected():
	voice = SimpleNamespace(
		UIAAutomationId="Message_item",
		children=[SimpleNamespace(UIAAutomationId="Recognize", children=[])],
	)
	voice_without_transcription = SimpleNamespace(
		UIAAutomationId="Message_item",
		children=[SimpleNamespace(UIAAutomationId="Subtitle", name="00:00 / 00:03", children=[])],
	)
	video = SimpleNamespace(
		UIAAutomationId="Message_item",
		children=[
			SimpleNamespace(UIAAutomationId="Player", children=[]),
			SimpleNamespace(UIAAutomationId="Subtitle", children=[]),
		],
	)
	text = SimpleNamespace(UIAAutomationId="Message_item", children=[])
	positioned = SimpleNamespace(positionInfo={"indexInGroup": 12, "similarItemsInGroup": 12})
	recycled_position = SimpleNamespace(positionInfo={"indexInGroup": 12, "similarItemsInGroup": 13})

	assert is_recorded_message(voice)
	assert is_recorded_message(voice_without_transcription)
	assert not is_recorded_message(text)
	assert is_recorded_message(video, video=True)
	assert not is_recorded_message(voice, video=True)
	assert message_marker(positioned) == ("position", 12, 12)
	assert message_marker(recycled_position) != message_marker(positioned)


def test_stopped_recording_is_sent_only_after_a_new_recorded_message_appears():
	outcome = VoiceRecordingOutcome(poll_limit=3)
	outcome.started(("position", 8))
	outcome.stopped()

	assert outcome.observe(("position", 8), is_recorded=True) is None
	assert outcome.observe(("position", 9), is_recorded=False) is None
	assert outcome.observe(("position", 9), is_recorded=True) == "sent"
	assert not outcome.pending


def test_new_message_is_sent_when_unigram_delays_its_voice_controls():
	outcome = VoiceRecordingOutcome(poll_limit=4)
	outcome.started(("position", 8, 8))
	outcome.stopped()

	assert outcome.observe(("position", 9, 9), is_recorded=False) is None
	assert outcome.observe(("position", 9, 9), is_recorded=False) == "sent"
	assert not outcome.pending


def test_transient_message_list_read_failure_is_not_treated_as_sent():
	outcome = VoiceRecordingOutcome(poll_limit=3)
	outcome.started(("position", 8, 8))
	outcome.stopped()

	assert outcome.observe(None, is_recorded=False) is None
	assert outcome.observe(("position", 8, 8), is_recorded=False) is None
	assert outcome.observe(("position", 8, 8), is_recorded=False) is None
	assert not outcome.pending


def test_stopped_recording_without_a_new_message_ends_silently():
	"""Unigram 13.0 announces "Recording canceled" itself, so the add-on does not."""
	outcome = VoiceRecordingOutcome(poll_limit=2)
	outcome.started(("position", 8))
	outcome.stopped()

	assert outcome.observe(("position", 8), is_recorded=False) is None
	assert outcome.observe(("position", 8), is_recorded=False) is None
	assert not outcome.pending
	assert outcome.observe(("position", 9), is_recorded=True) is None


def test_the_shipped_send_window_stays_short():
	"""Telegram inserts the outgoing message optimistically, so the window only
	has to cover that insertion, not the upload. A longer one would give an
	incoming message more time to be taken for a canceled recording being sent.
	"""
	source = (ROOT / "addon" / "appModules" / "unigram.py").read_text(encoding="utf-8")
	module = ast.parse(source)
	limit = next(
		node.value.value
		for node in module.body
		if isinstance(node, ast.Assign)
		and any(getattr(t, "id", "") == "_VOICE_RECORDING_OUTCOME_POLL_LIMIT" for t in node.targets)
	)
	interval = next(
		node.value.value
		for node in module.body
		if isinstance(node, ast.Assign)
		and any(getattr(t, "id", "") == "_VOICE_RECORDING_POLL_INTERVAL" for t in node.targets)
	)
	seconds = limit * interval
	assert 0.8 <= seconds <= 2.0, "a send is watched for %.1f s" % seconds


def test_a_sent_recording_is_still_reported_before_the_window_closes():
	outcome = VoiceRecordingOutcome(poll_limit=7)
	outcome.started(("position", 8))
	outcome.stopped()

	assert outcome.observe(("position", 9), is_recorded=True) == "sent"
	assert not outcome.pending


def test_nothing_is_reported_when_the_window_closes():
	outcome = VoiceRecordingOutcome(poll_limit=7)
	outcome.started(("position", 8))
	outcome.stopped()

	for _ in range(7):
		assert outcome.observe(("position", 8), is_recorded=False) is None
	assert not outcome.pending


def test_recording_state_uses_the_same_elapsed_sibling_as_the_button_label():
	idle_button = SimpleNamespace(
		UIAAutomationId="btnVoiceMessage",
		next=SimpleNamespace(UIAAutomationId="SomeOtherControl"),
	)
	recording_button = SimpleNamespace(
		UIAAutomationId="btnVoiceMessage",
		next=SimpleNamespace(UIAAutomationId="ElapsedLabel"),
	)

	assert is_recording_button(idle_button)
	assert recording_button_state(idle_button) is False
	assert recording_button_state(recording_button) is True
	assert recording_button_state(SimpleNamespace(UIAAutomationId="SendButton")) is None


def test_unreadable_cached_button_is_rediscovered_instead_of_misdetected():
	class StaleButton:
		UIAAutomationId = "btnVoiceMessage"

		@property
		def next(self):
			raise RuntimeError("stale UIA object")

	assert recording_button_state(StaleButton()) is None


def test_cached_recording_button_avoids_repeated_ui_tree_searches():
	button = SimpleNamespace(UIAAutomationId="btnVoiceMessage")
	focus = SimpleNamespace(UIAAutomationId="TextField")
	instance = SimpleNamespace(
		_voiceRecordingButton=button,
		_voiceRecordingDiscoveryFocus=None,
		getElements=lambda: (_ for _ in ()).throw(AssertionError("unexpected UI tree scan")),
	)
	namespace = {"is_recording_button": is_recording_button}
	method = _load_method("_getVoiceRecordingButton", namespace)

	assert method(instance, focus) is button


def test_recording_button_discovery_runs_only_once_for_the_same_focus():
	focus = SimpleNamespace(UIAAutomationId="TextField")
	searches = []
	instance = SimpleNamespace(
		_voiceRecordingButton=None,
		_voiceRecordingDiscoveryFocus=None,
		getElements=lambda: searches.append(True) or [],
	)
	namespace = {"is_recording_button": is_recording_button}
	method = _load_method("_getVoiceRecordingButton", namespace)

	assert method(instance, focus) is None
	assert method(instance, focus) is None
	assert searches == [True]


def test_recording_monitor_samples_off_the_main_loop_without_timer_threads():
	# The monitor reads Unigram's record button and message list, so it samples on
	# the shared background poller rather than on NVDA's event loop, and never
	# spawns a native Timer thread per sample.
	scheduled = []
	instance = SimpleNamespace(
		_voiceRecordingMonitorRunning=True,
		_pollVoiceRecordingState=lambda: None,
	)
	namespace = {
		"_VOICE_RECORDING_POLL_INTERVAL": 0.2,
		"_BackgroundPoller": SimpleNamespace(
			schedule=lambda key, delay, callback: scheduled.append((delay, callback)),
			cancel=lambda key: None,
		),
	}
	method = _load_method("_scheduleVoiceRecordingPoll", namespace)

	method(instance)

	assert scheduled == [(0.2, instance._pollVoiceRecordingState)]
	assert "Timer" not in _method_source("_scheduleVoiceRecordingPoll")
	assert "core.callLater" not in _method_source("_scheduleVoiceRecordingPoll")


def test_app_transition_handler_captures_baseline_before_resolving_outcome():
	announcements = []
	button = SimpleNamespace(states=set())
	outcome = VoiceRecordingOutcome(poll_limit=2)
	instance = SimpleNamespace(
		_voiceRecordingButton=button,
		_voiceRecordingOutcome=outcome,
		_getVoiceRecordingLastMessage=lambda: (("position", 5), object()),
		_announceVoiceRecordingTransition=announcements.append,
	)
	namespace = {"State": SimpleNamespace(PRESSED="pressed"), "time": time}
	method = _load_method("_handleVoiceRecordingTransition", namespace)

	method(instance, "start")
	method(instance, "stopped")

	assert outcome.baseline == ("position", 5)
	assert outcome.pending
	assert not outcome.video
	assert announcements == ["start"]


def test_app_outcome_poll_announces_new_voice_message_as_sent():
	announcements = []
	logs = []
	voice = SimpleNamespace(
		UIAAutomationId="Message_item",
		children=[SimpleNamespace(UIAAutomationId="Recognize", children=[])],
	)
	outcome = VoiceRecordingOutcome(poll_limit=2)
	outcome.started(("position", 5))
	outcome.stopped()
	instance = SimpleNamespace(
		_voiceRecordingOutcome=outcome,
		_getVoiceRecordingLastMessage=lambda: (("position", 6), voice),
		_announceVoiceRecordingTransition=announcements.append,
	)
	namespace = {
		"is_recorded_message": is_recorded_message,
		"log": SimpleNamespace(debug=logs.append),
	}
	method = _load_method("_pollVoiceRecordingOutcome", namespace)

	method(instance)

	assert announcements == ["sent"]
	assert logs and logs[0].endswith("sent")
	assert not outcome.pending


def test_polling_native_ui_announces_manual_or_keyboard_recording_once():
	transitions = []
	scheduled = []

	button = SimpleNamespace(
		UIAAutomationId="btnVoiceMessage",
		next=SimpleNamespace(UIAAutomationId="ElapsedLabel"),
	)
	instance = SimpleNamespace(
		_voiceRecordingMonitorRunning=True,
		_voiceRecordingState=VoiceRecordingState(),
		_voiceRecordingButton=button,
		_getVoiceRecordingButton=lambda focus: button,
		_pollVoiceRecordingOutcome=lambda: None,
		_handleVoiceRecordingTransition=lambda transition: transitions.append(transition) if transition else None,
		_scheduleVoiceRecordingPoll=lambda: scheduled.append(True),
		_is_main_window_object=lambda obj: True,
	)
	focus = SimpleNamespace(appModule=instance)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"recording_button_state": recording_button_state,
		"log": SimpleNamespace(debug=lambda text: None, info=lambda text: None),
	}
	method = _load_method("_pollVoiceRecordingState", namespace)

	method(instance)
	method(instance)
	button.next = SimpleNamespace(UIAAutomationId="SomeOtherControl")
	method(instance)

	assert transitions == ["start", "stopped"]
	assert scheduled == [True, True, True]
	assert not instance._voiceRecordingState.active


def test_recording_monitor_does_not_scan_a_separate_call_window():
	scheduled = []
	instance = SimpleNamespace(
		_voiceRecordingMonitorRunning=True,
		_voiceRecordingDiscoveryFocus=object(),
		_is_main_window_object=lambda obj: False,
		_pollVoiceRecordingOutcome=lambda: (_ for _ in ()).throw(AssertionError("unexpected outcome scan")),
		_getVoiceRecordingButton=lambda focus: (_ for _ in ()).throw(AssertionError("unexpected UI tree scan")),
		_scheduleVoiceRecordingPoll=lambda: scheduled.append(True),
	)
	focus = SimpleNamespace(appModule=instance, windowHandle=200)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"recording_button_state": recording_button_state,
		"log": SimpleNamespace(debug=lambda text: None, info=lambda text: None),
	}
	method = _load_method("_pollVoiceRecordingState", namespace)

	method(instance)

	assert instance._voiceRecordingDiscoveryFocus is None
	assert scheduled == [True]


def test_recording_monitor_does_not_probe_uia_ancestors_on_each_poll():
	scheduled = []
	instance = SimpleNamespace(
		_voiceRecordingMonitorRunning=True,
		_voiceRecordingDiscoveryFocus=object(),
		_classify_window_surface=lambda obj: (_ for _ in ()).throw(
			AssertionError("the high-frequency poll must not walk UIA ancestors")
		),
		_is_main_window_object=lambda obj: False,
		_scheduleVoiceRecordingPoll=lambda: scheduled.append(True),
	)
	focus = SimpleNamespace(appModule=instance, windowHandle=200)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"recording_button_state": recording_button_state,
		"log": SimpleNamespace(debug=lambda text: None, info=lambda text: None),
	}
	method = _load_method("_pollVoiceRecordingState", namespace)

	method(instance)

	assert scheduled == [True]


def test_recording_start_and_send_keep_text_and_audio_notifications():
	announcements = []
	sounds = []
	button = SimpleNamespace(
		role="toggle",
		UIAAutomationId="btnVoiceMessage",
		states=set(),
	)
	settings = {"indicator": "text"}
	namespace = {
		"conf": SimpleNamespace(get=lambda key: settings["indicator"]),
		"Role": SimpleNamespace(TOGGLEBUTTON="toggle"),
		"State": SimpleNamespace(PRESSED="pressed"),
		"winsound": SimpleNamespace(
			SND_ASYNC=1,
			SND_NOSTOP=2,
			PlaySound=lambda path, flags: sounds.append((path, flags)),
		),
		"baseDir": "media/",
		"message": announcements.append,
		"log": SimpleNamespace(debug=lambda text: None),
		"_": lambda text: text,
	}
	namespace["queueHandler"] = SimpleNamespace(
		eventQueue=object(),
		queueFunction=lambda queue, callback, *args: callback(*args),
	)
	method = _load_method("_announceVoiceRecordingTransition", namespace)
	do_announce = _load_method("_doAnnounceVoiceRecordingTransition", namespace)
	instance = SimpleNamespace(_voiceRecordingButton=button)
	instance._doAnnounceVoiceRecordingTransition = lambda transition: do_announce(
		instance, transition
	)

	method(instance, "start")
	method(instance, "sent")
	settings["indicator"] = "audio"
	method(instance, "start")
	method(instance, "sent")

	assert announcements == ["Audio", "Record sent"]
	assert [path for path, flags in sounds] == [
		"media/start_recording_voice_message.wav",
		"media/send_voice_message.wav",
	]


def test_a_canceled_recording_is_left_to_unigram():
	"""Unigram 13.0 raises its own "Recording canceled" UIA notification.

	ChatRecordButton.Cancel raises it for Ctrl+D, the cancel button and sliding
	away, so the add-on announcing the same thing would be heard twice.
	"""
	announcements = []
	sounds = []
	namespace = {
		"winsound": SimpleNamespace(
			SND_ASYNC=1,
			SND_NOSTOP=2,
			PlaySound=lambda path, flags: sounds.append(path),
		),
		"baseDir": "media/",
		"message": announcements.append,
		"State": SimpleNamespace(PRESSED="pressed"),
		"log": SimpleNamespace(debug=lambda text: None),
		"_": lambda text: text,
	}
	do_announce = _load_method("_doAnnounceVoiceRecordingTransition", namespace)
	instance = SimpleNamespace(_voiceRecordingButton=None)

	for indicator in ("text", "audio"):
		namespace["conf"] = SimpleNamespace(get=lambda key, value=indicator: value)
		do_announce(instance, "canceled")

	assert announcements == []
	assert sounds == []
	source = (ROOT / "addon" / "appModules" / "unigram.py").read_text(encoding="utf-8")
	assert "Recording canceled\")" not in source
	assert "cancel_voice_message_recording" not in source
	assert not (ROOT / "addon" / "appModules" / "media" / "cancel_voice_message_recording.wav").exists()


def _record_button(location_width=40):
	return SimpleNamespace(
		UIAAutomationId="btnVoiceMessage",
		location=SimpleNamespace(width=location_width),
	)


def _load_record_focus_restore(setting):
	restored = []
	namespace = {
		"is_recording_button": is_recording_button,
		"conf": SimpleNamespace(get=lambda key: setting),
		"speech": SimpleNamespace(cancelSpeech=lambda: restored.append("cancelSpeech")),
		"time": time,
		"_RECORD_TRANSITION_FOCUS_WINDOW": 1.5,
	}
	method = _load_method("_restore_focus_after_record_button", namespace)
	return method, restored


def _field(events):
	return SimpleNamespace(
		location=SimpleNamespace(width=300),
		setFocus=lambda: events.append("backToField"),
	)


def test_the_54_option_keeps_the_focus_in_the_message_field():
	"""5.4 pressed the record button itself and put the focus straight back."""
	method, events = _load_record_focus_restore("none")
	instance = SimpleNamespace(
		_focusBeforeRecordButton=_field(events),
		_recordTransitionTime=time.monotonic(),
	)

	assert method(instance, _record_button()) is True
	assert events == ["cancelSpeech", "backToField"]


def test_tabbing_to_the_record_button_always_reaches_it():
	"""Only Unigram's own move is undone; the user navigating there is not."""
	method, events = _load_record_focus_restore("none")
	for transition_time in (None, time.monotonic() - 5):
		instance = SimpleNamespace(
			_focusBeforeRecordButton=_field(events),
			_recordTransitionTime=transition_time,
		)

		assert method(instance, _record_button()) is False
		assert events == []


def test_the_other_options_let_the_focus_reach_the_record_button():
	for setting in ("withElapsedTime", "labelOnly"):
		method, events = _load_record_focus_restore(setting)
		instance = SimpleNamespace(
			_focusBeforeRecordButton=_field(events),
			_recordTransitionTime=time.monotonic(),
		)

		assert method(instance, _record_button()) is False
		assert events == []


def test_nothing_is_restored_without_a_remembered_message_field():
	method, events = _load_record_focus_restore("none")
	instance = SimpleNamespace(_focusBeforeRecordButton=None, _recordTransitionTime=time.monotonic())

	assert method(instance, _record_button()) is False
	assert events == []


def test_other_controls_are_never_bounced():
	method, events = _load_record_focus_restore("none")
	instance = SimpleNamespace(
		_focusBeforeRecordButton=_field(events),
		_recordTransitionTime=time.monotonic(),
	)
	other = SimpleNamespace(UIAAutomationId="ButtonAttach")

	assert method(instance, other) is False
	assert events == []
