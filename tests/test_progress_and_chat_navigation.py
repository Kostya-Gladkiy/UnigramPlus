import ast
import re
import sys
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"


def _class_ast(name):
	module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
	return next(node for node in module.body if isinstance(node, ast.ClassDef) and node.name == name)


def _load_app_method(name, namespace):
	method = next(
		node
		for node in _class_ast("AppModule").body
		if isinstance(node, ast.FunctionDef) and node.name == name
	)
	method.decorator_list = []
	exec(compile(ast.Module(body=[method], type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace[name]


def _load_module_function(name, namespace):
	module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
	function = next(
		node
		for node in module.body
		if isinstance(node, ast.FunctionDef) and node.name == name
	)
	exec(compile(ast.Module(body=[function], type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace[name]


def _fake_background_poller(scheduled):
	"""Stand in for the shared poller and record what each sample scheduled."""
	class ScheduledCall:
		def __init__(self):
			self.stopped = False

	def schedule(key, delay, callback):
		scheduled.append((round(delay * 1000), callback, ScheduledCall()))

	def cancel(key):
		for entry in scheduled:
			entry[2].stopped = True

	return SimpleNamespace(schedule=schedule, cancel=cancel)


def _load_progress_tracker(monkeypatch, scheduled):
	namespace = {
		"_BackgroundPoller": _fake_background_poller(scheduled),
		"Role": SimpleNamespace(LINK="link", BUTTON="button"),
		"api": SimpleNamespace(getFocusObject=lambda: None),
		"conf": SimpleNamespace(get=lambda key: "upload_download"),
		"log": SimpleNamespace(info=lambda *args: None, debug=lambda *args: None),
		"queueHandler": SimpleNamespace(
			eventQueue=object(),
			queueFunction=lambda *args: None,
		),
		"speech": SimpleNamespace(speakMessage=lambda text: None),
		"re": re,
		"_": lambda text: text,
	}
	exec(
		compile(ast.Module(body=[_class_ast("File_transfer_progress_tracking")], type_ignores=[]), str(SOURCE_PATH), "exec"),
		namespace,
	)
	return namespace["File_transfer_progress_tracking"]


def _load_chat_list_item():
	class ListItem:
		pass

	def script(**kwargs):
		return lambda function: function

	namespace = {
		"ListItem": ListItem,
		"script": script,
		"_": lambda text: text,
		"message": lambda text: None,
	}
	exec(
		compile(ast.Module(body=[_class_ast("ChatListItem")], type_ignores=[]), str(SOURCE_PATH), "exec"),
		namespace,
	)
	return namespace["ChatListItem"]


def test_progress_tracker_samples_off_the_main_loop_without_timer_threads(monkeypatch):
	scheduled = []
	tracker = _load_progress_tracker(monkeypatch, scheduled)

	tracker.start()

	assert len(scheduled) == 1
	assert scheduled[0][0] == 350
	assert "Timer" not in {
		node.id
		for node in ast.walk(_class_ast("File_transfer_progress_tracking"))
		if isinstance(node, ast.Name)
	}

	_, callback, first_call = scheduled.pop()
	callback()

	assert len(scheduled) == 1
	assert not first_call.stopped
	tracker.stop()
	assert scheduled[0][2].stopped


def test_progress_tracker_stops_and_does_not_reschedule_at_100_percent(monkeypatch):
	scheduled = []
	tracker = _load_progress_tracker(monkeypatch, scheduled)
	button = object()
	tracker._is_unigram_object = classmethod(lambda cls, obj: True)
	tracker._is_in_foreground = classmethod(lambda cls, obj: True)
	tracker._is_transfer_button = classmethod(lambda cls, obj: True)
	tracker._read_fresh_value = classmethod(lambda cls, obj: "100%")
	tracker._get_key = classmethod(lambda cls, obj: ("button",))

	tracker.start()
	assert tracker.handle_progress(button, speak_first=True)

	assert not tracker.active
	assert not tracker._scheduled
	assert scheduled[0][2].stopped

	# A canceled callback may already be queued by some main-loop implementations.
	# Its generation token must prevent it from reviving the completed tracker.
	scheduled[0][1]()
	assert not tracker.active
	assert len(scheduled) == 1


def test_progress_tracker_never_walks_an_unrelated_focused_uia_tree(monkeypatch):
	scheduled = []
	tree_accesses = []
	tracker = _load_progress_tracker(monkeypatch, scheduled)

	class InlineButton:
		role = "listItem"
		UIAAutomationId = ""
		appModule = object()
		isInForeground = True

		@property
		def parent(self):
			tree_accesses.append("parent")
			raise AssertionError("the recurring transfer poll must not walk parents")

		@property
		def children(self):
			tree_accesses.append("children")
			raise AssertionError("the recurring transfer poll must not walk children")

	focus = InlineButton()
	tracker._is_unigram_object = classmethod(lambda cls, obj: obj is focus)
	tracker._is_in_foreground = classmethod(lambda cls, obj: obj is focus)
	tracker.start()
	_scheduled_delay, callback, _scheduled_call = scheduled.pop()
	callback()

	assert tracker.active
	assert len(scheduled) == 1
	assert tree_accesses == []
	assert "_find_transfer_button" not in {
		node.name
		for node in _class_ast("File_transfer_progress_tracking").body
		if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
	}


def test_focus_handler_does_not_search_message_subtrees_for_file_transfers():
	method = _load_app_method("event_gainFocus", {})
	assert "_find_transfer_button" not in method.__code__.co_names


def test_file_transfer_tracker_keeps_unigram_and_messages_scope_restrictions():
	tracker = _class_ast("File_transfer_progress_tracking")
	transfer_button = next(
		node
		for node in tracker.body
		if isinstance(node, ast.FunctionDef) and node.name == "_is_transfer_button"
	)
	tick = next(
		node
		for node in tracker.body
		if isinstance(node, ast.FunctionDef) and node.name == "tick"
	)
	handle_progress = next(
		node
		for node in tracker.body
		if isinstance(node, ast.FunctionDef) and node.name == "handle_progress"
	)

	assert "_is_inside_messages" in ast.unparse(transfer_button)
	assert "_is_unigram_object" in ast.unparse(handle_progress)
	assert "_is_unigram_object" in ast.unparse(tick)
	assert "_is_transfer_button" in ast.unparse(tick)


def test_chat_folder_unread_count_parses_only_a_trailing_badge():
	get_unread_count = _load_module_function("_get_chat_folder_unread_count", {"re": re})
	get_folder_name = _load_app_method("_get_chat_folder_name", {"re": re})
	instance = SimpleNamespace()

	assert get_unread_count("All, 538") == "538"
	assert get_unread_count("All 538") is None
	assert get_unread_count("(All, 538)") == "538"
	assert get_unread_count("Personal, 1") == "1"
	assert get_unread_count("Unread, 0") is None
	assert get_unread_count("Personal") is None
	assert get_unread_count("Project 2024") is None
	assert get_unread_count("Folder 12 notes") is None
	assert get_folder_name(instance, "All, 538") == "All"
	assert get_folder_name(instance, "All 538") == "All 538"
	assert get_folder_name(instance, "(All, 538)") == "All"
	assert get_folder_name(instance, "Personal, 1") == "Personal"
	assert get_folder_name(instance, "Unread, 0") == "Unread"
	assert get_folder_name(instance, "Personal") == "Personal"
	assert get_folder_name(instance, "Project 2024") == "Project 2024"


def test_change_chats_folder_announces_nonzero_unread_count_once():
	announcements = []
	saved = {"last selected folder": "All"}
	instance = SimpleNamespace(
		saved_items=SimpleNamespace(
			get=lambda key: saved.get(key),
			save=lambda key, value: saved.__setitem__(key, value),
		),
	)
	get_name = _load_app_method("_get_chat_folder_name", {"re": re})
	instance._get_chat_folder_name = lambda name: get_name(instance, name)
	change_folder = _load_app_method(
		"change_chats_folder",
		{
			"_get_chat_folder_unread_count": _load_module_function(
				"_get_chat_folder_unread_count", {"re": re}
			),
			"message": lambda text: announcements.append(text),
			"conf": SimpleNamespace(get=lambda key: True),
			"queueHandler": SimpleNamespace(
				eventQueue=object(),
				queueFunction=lambda queue, callback, text: callback(text),
			),
		},
	)

	change_folder(instance, SimpleNamespace(name="Unread, 538"), None)
	assert saved["last selected folder"] == "Unread"
	assert announcements == ["Unread, 538"]

	saved["last selected folder"] = "All"
	change_folder(instance, SimpleNamespace(name="Unread, 0"), None)
	change_folder(instance, SimpleNamespace(name="Personal"), None)
	assert saved["last selected folder"] == "Personal"
	assert announcements == ["Unread, 538", "Unread", "Personal"]

	change_folder(instance, SimpleNamespace(name="Personal, 12"), None)
	assert announcements == ["Unread, 538", "Unread", "Personal"]

	saved["last selected folder"] = "All"
	change_folder(instance, SimpleNamespace(name="Project 2024"), None)
	assert saved["last selected folder"] == "Project 2024"
	assert announcements == ["Unread, 538", "Unread", "Personal", "Project 2024"]


def test_all_recurring_uia_pollers_sample_off_the_nvda_main_loop():
	# These ticks issue cross-process UIA reads. Running them on NVDA's event
	# loop stalls speech and keyboard handling for as long as Unigram takes to
	# answer, so they belong on the shared background poller - which, unlike the
	# original threading.Timer approach, does not create a thread per sample.
	for class_name in ("Title_change_tracking", "Typing_sound_tracking", "Chat_update"):
		class_node = _class_ast(class_name)
		assert any(
			isinstance(base, ast.Name) and base.id == "_BackgroundStatePoller"
			for base in class_node.bases
		)
		assert "Timer" not in {
			node.id
			for node in ast.walk(class_node)
			if isinstance(node, ast.Name)
		}

	poller_source = ast.unparse(_class_ast("_BackgroundStatePoller"))
	assert "_BackgroundPoller.schedule" in poller_source
	assert "core.callLater" not in poller_source


def test_pollers_hand_every_announcement_back_to_the_main_thread():
	# Sampling happens off-thread, so anything that reaches NVDA's UI from a tick
	# must be queued rather than called directly.
	for class_name in ("Title_change_tracking", "Chat_update"):
		tick = next(
			node
			for node in _class_ast(class_name).body
			if isinstance(node, ast.FunctionDef) and node.name == "tick"
		)
		source = ast.unparse(tick)
		assert "queueHandler.queueFunction" in source


def test_background_poller_runs_one_shared_worker_thread():
	poller_source = ast.unparse(_class_ast("_BackgroundPoller"))
	assert "daemon=True" in poller_source
	assert "threading.Thread" in poller_source


def test_chat_mention_navigation_uses_the_stable_unigram_badge_glyph():
	chat_item = _load_chat_list_item()
	mention = SimpleNamespace(
		UIAAutomationId="UnreadMentionsLabel",
		name="\ueb00",
		children=[],
	)
	reaction = SimpleNamespace(
		UIAAutomationId="UnreadMentionsLabel",
		name="\ue9b6",
		children=[],
	)
	with_mention = SimpleNamespace(
		UIAAutomationId="ChatCell",
		children=[SimpleNamespace(UIAAutomationId="Grid", children=[mention])],
	)
	with_reaction = SimpleNamespace(UIAAutomationId="ChatCell", children=[reaction])

	assert chat_item._has_unread_mentions(with_mention)
	assert not chat_item._has_unread_mentions(with_reaction)


def test_chat_mention_navigation_skips_other_chats_in_both_directions():
	chat_item = _load_chat_list_item()

	def chat(glyph=None):
		children = []
		if glyph:
			children.append(SimpleNamespace(UIAAutomationId="UnreadMentionsLabel", name=glyph, children=[]))
		return SimpleNamespace(
			UIAAutomationId="ChatCell",
			children=children,
			next=None,
			previous=None,
			setFocus=lambda: None,
		)

	previous_mention = chat("\ueb00")
	previous_plain = chat()
	current = chat_item()
	current.UIAAutomationId = "ChatCell"
	current.children = []
	current.next = None
	current.previous = None
	next_plain = chat()
	next_mention = chat("\ueb00")
	items = [previous_mention, previous_plain, current, next_plain, next_mention]
	focused = []
	for index, item in enumerate(items):
		item.previous = items[index - 1] if index else None
		item.next = items[index + 1] if index + 1 < len(items) else None
		item.setFocus = lambda item=item: focused.append(item)

	assert current._move_to_chat_with_unread_mentions(True)
	assert focused.pop() is next_mention
	assert current._move_to_chat_with_unread_mentions(False)
	assert focused.pop() is previous_mention


def test_app_module_gain_focus_starts_one_shot_chat_list_focusing():
	scheduled = []
	instance = SimpleNamespace(
		isUnigramWindow=True,
		_autoFocusChatListAttempts=7,
		_scheduleAutoFocusChatList=lambda: scheduled.append(True),
	)
	method = _load_app_method("event_appModule_gainFocus", {})

	method(instance)

	assert instance._autoFocusChatListAttempts == 0
	assert scheduled == [True]


def test_auto_focus_is_scheduled_on_nvda_main_loop(monkeypatch):
	scheduled = []
	core = SimpleNamespace(
		callLater=lambda delay, callback, *args: scheduled.append((delay, callback, args))
	)
	monkeypatch.setitem(sys.modules, "core", core)
	callback = lambda generation: None
	instance = SimpleNamespace(
		_autoFocusChatListDone=False,
		_autoFocusChatListScheduled=False,
		_autoFocusChatListGeneration=4,
		_autoFocusChatListTick=callback,
	)
	namespace = {
		"conf": SimpleNamespace(get=lambda key: True),
		"log": SimpleNamespace(debug=lambda *args: None),
		"_AUTO_FOCUS_CHAT_LIST_DELAY_MS": 300,
	}
	method = _load_app_method("_scheduleAutoFocusChatList", namespace)

	method(instance)
	method(instance)

	assert instance._autoFocusChatListScheduled
	assert scheduled == [(300, callback, (4,))]


def test_auto_focus_is_not_scheduled_when_disabled(monkeypatch):
	scheduled = []
	monkeypatch.setitem(
		sys.modules,
		"core",
		SimpleNamespace(callLater=lambda *args: scheduled.append(args)),
	)
	instance = SimpleNamespace(
		_autoFocusChatListDone=False,
		_autoFocusChatListScheduled=False,
		_autoFocusChatListGeneration=4,
		_autoFocusChatListTick=lambda generation: None,
	)
	namespace = {
		"conf": SimpleNamespace(get=lambda key: False),
		"log": SimpleNamespace(debug=lambda *args: None),
		"_AUTO_FOCUS_CHAT_LIST_DELAY_MS": 300,
	}
	method = _load_app_method("_scheduleAutoFocusChatList", namespace)

	method(instance)

	assert not instance._autoFocusChatListScheduled
	assert scheduled == []


def test_auto_focus_waits_for_the_chat_list_then_completes():
	focus_calls = []
	retries = []
	instance = SimpleNamespace(
		_autoFocusChatListDone=False,
		_autoFocusChatListScheduled=True,
		_autoFocusChatListAttempts=0,
		_autoFocusChatListGeneration=2,
		script_toChatList=lambda gesture, arg=False: focus_calls.append(arg) or True,
		_scheduleAutoFocusChatList=lambda: retries.append(True),
		_classify_window_surface=lambda obj: "main",
		_is_focus_in_popup=lambda focus: False,
	)
	focus = SimpleNamespace(
		appModule=instance,
		isInForeground=True,
		role="pane",
		parent=None,
	)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"conf": SimpleNamespace(get=lambda key: True),
		"Role": SimpleNamespace(LISTITEM="listItem"),
		"log": SimpleNamespace(debug=lambda *args: None),
		"_AUTO_FOCUS_CHAT_LIST_RETRY_LIMIT": 10,
	}
	method = _load_app_method("_autoFocusChatListTick", namespace)

	method(instance, 2)

	assert instance._autoFocusChatListDone
	assert not instance._autoFocusChatListScheduled
	assert focus_calls == [True]
	assert retries == []


def test_auto_focus_does_not_repeat_when_focus_is_already_in_chat_list():
	focus_calls = []
	instance = SimpleNamespace(
		_autoFocusChatListDone=False,
		_autoFocusChatListScheduled=True,
		_autoFocusChatListAttempts=0,
		_autoFocusChatListGeneration=1,
		script_toChatList=lambda gesture, arg=False: focus_calls.append(True),
		_scheduleAutoFocusChatList=lambda: None,
		_classify_window_surface=lambda obj: "main",
		_is_focus_in_popup=lambda focus: False,
	)
	parent = SimpleNamespace(UIAAutomationId="ChatsList")
	focus = SimpleNamespace(
		appModule=instance,
		isInForeground=True,
		role="listItem",
		parent=parent,
	)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"conf": SimpleNamespace(get=lambda key: True),
		"Role": SimpleNamespace(LISTITEM="listItem"),
		"log": SimpleNamespace(debug=lambda *args: None),
		"_AUTO_FOCUS_CHAT_LIST_RETRY_LIMIT": 10,
	}
	method = _load_app_method("_autoFocusChatListTick", namespace)

	method(instance, 1)

	assert instance._autoFocusChatListDone
	assert focus_calls == []


def test_auto_focus_never_moves_focus_away_from_a_separate_call_window():
	focus_calls = []
	instance = SimpleNamespace(
		_autoFocusChatListDone=False,
		_autoFocusChatListScheduled=True,
		_autoFocusChatListAttempts=0,
		_autoFocusChatListGeneration=1,
		script_toChatList=lambda gesture, arg=False: focus_calls.append(True),
		_scheduleAutoFocusChatList=lambda: None,
		_classify_window_surface=lambda obj: "call",
	)
	focus = SimpleNamespace(
		appModule=instance,
		isInForeground=True,
		role="button",
		windowHandle=200,
	)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"conf": SimpleNamespace(get=lambda key: True),
		"Role": SimpleNamespace(LISTITEM="listItem"),
		"log": SimpleNamespace(debug=lambda *args: None),
		"_AUTO_FOCUS_CHAT_LIST_RETRY_LIMIT": 10,
	}
	method = _load_app_method("_autoFocusChatListTick", namespace)

	method(instance, 1)

	assert instance._autoFocusChatListDone
	assert focus_calls == []


def test_auto_focus_does_not_mistake_an_unidentified_or_second_chat_window_for_a_call():
	focus_calls = []
	instance = SimpleNamespace(
		_autoFocusChatListDone=False,
		_autoFocusChatListScheduled=True,
		_autoFocusChatListAttempts=0,
		_autoFocusChatListGeneration=1,
		# Unigram can host a second chat in another WindowEx. A different handle is
		# not sufficient evidence that this is a call surface.
		_mainWindowHandle=999,
		script_toChatList=lambda gesture, arg=False: focus_calls.append(arg) or True,
		_scheduleAutoFocusChatList=lambda: None,
		_classify_window_surface=lambda obj: None,
		_is_focus_in_popup=lambda focus: False,
	)
	focus = SimpleNamespace(
		appModule=instance,
		isInForeground=True,
		role="button",
		windowHandle=100,
	)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"conf": SimpleNamespace(get=lambda key: True),
		"Role": SimpleNamespace(LISTITEM="listItem"),
		"log": SimpleNamespace(debug=lambda *args: None),
		"_AUTO_FOCUS_CHAT_LIST_RETRY_LIMIT": 10,
	}
	method = _load_app_method("_autoFocusChatListTick", namespace)

	method(instance, 1)

	assert instance._autoFocusChatListDone
	assert focus_calls == [True]


def test_auto_focus_leaves_the_focus_in_a_popup():
	# Opening a group invite link shows Unigram's request to join popup as the
	# app starts or comes to the foreground.
	focus_calls = []
	retries = []
	instance = SimpleNamespace(
		_autoFocusChatListDone=False,
		_autoFocusChatListScheduled=True,
		_autoFocusChatListAttempts=0,
		_autoFocusChatListGeneration=1,
		script_toChatList=lambda gesture, arg=False: focus_calls.append(arg) or True,
		_scheduleAutoFocusChatList=lambda: retries.append(True),
		_classify_window_surface=lambda obj: "main",
		_is_focus_in_popup=lambda focus: True,
	)
	focus = SimpleNamespace(
		appModule=instance,
		isInForeground=True,
		role="button",
		parent=None,
	)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"conf": SimpleNamespace(get=lambda key: True),
		"Role": SimpleNamespace(LISTITEM="listItem"),
		"log": SimpleNamespace(debug=lambda *args: None),
		"_AUTO_FOCUS_CHAT_LIST_RETRY_LIMIT": 10,
	}
	method = _load_app_method("_autoFocusChatListTick", namespace)

	method(instance, 1)

	assert instance._autoFocusChatListDone
	assert focus_calls == []
	assert retries == []


def test_popup_is_recognized_from_the_dialog_role_of_the_focus_or_an_ancestor():
	class Gone:
		@property
		def role(self):
			raise RuntimeError("the UIA element is gone")

	window = SimpleNamespace(role="window")
	pane = SimpleNamespace(role="pane")
	popup = SimpleNamespace(role="dialog")
	join_button = SimpleNamespace(role="button")
	ancestors = []
	namespace = {
		"api": SimpleNamespace(getFocusAncestors=lambda: ancestors),
		"Role": SimpleNamespace(DIALOG="dialog"),
	}
	is_in_popup = _load_app_method("_is_focus_in_popup", namespace)

	ancestors[:] = [window, Gone(), popup, pane]
	assert is_in_popup(None, join_button)
	ancestors[:] = [window, pane]
	assert not is_in_popup(None, join_button)
	# A popup without focusable content keeps the focus itself.
	assert is_in_popup(None, popup)


def test_auto_focus_retries_when_the_initial_focus_object_is_not_ready():
	retries = []
	instance = SimpleNamespace(
		_autoFocusChatListDone=False,
		_autoFocusChatListScheduled=True,
		_autoFocusChatListAttempts=0,
		_autoFocusChatListGeneration=1,
		_scheduleAutoFocusChatList=lambda: retries.append(True),
	)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: None),
		"conf": SimpleNamespace(get=lambda key: True),
		"Role": SimpleNamespace(LISTITEM="listItem"),
		"log": SimpleNamespace(debug=lambda *args: None),
		"_AUTO_FOCUS_CHAT_LIST_RETRY_LIMIT": 10,
	}
	method = _load_app_method("_autoFocusChatListTick", namespace)

	method(instance, 1)

	assert instance._autoFocusChatListAttempts == 1
	assert retries == [True]


def test_focus_events_do_not_restart_startup_chat_list_focusing():
	app_module = _class_ast("AppModule")
	method = next(
		node
		for node in app_module.body
		if isinstance(node, ast.FunctionDef) and node.name == "event_gainFocus"
	)

	assert "_scheduleAutoFocusChatList" not in ast.unparse(method)


def test_main_chat_window_is_identified_from_stable_uia_ancestors():
	main_marker = SimpleNamespace(UIAAutomationId="Messages", parent=None)
	main_focus = SimpleNamespace(UIAAutomationId="Message_item", parent=main_marker, windowHandle=100)
	call_marker = SimpleNamespace(UIAAutomationId="ActiveButtons", parent=None)
	call_focus = SimpleNamespace(UIAAutomationId="Mute", parent=call_marker, windowHandle=200)
	namespace = {
		"_MAIN_WINDOW_AUTOMATION_IDS": frozenset(("ChatsList", "Messages", "TextField", "Navigation")),
		"_CALL_WINDOW_AUTOMATION_IDS": frozenset(("ActiveButtons", "BottomRoot")),
		"_WINDOW_SURFACE_AUTOMATION_IDS": frozenset(
			("ChatsList", "Messages", "TextField", "Navigation", "ActiveButtons", "BottomRoot")
		),
	}
	namespace["_find_ancestor_by_automation_id"] = _load_module_function(
		"_find_ancestor_by_automation_id",
		{},
	)
	classify = _load_app_method("_classify_window_surface", namespace)
	is_main = _load_app_method("_is_main_window_object", namespace)
	instance = SimpleNamespace(_mainWindowHandle=None, _callWindowHandles=set())

	assert classify(instance, main_focus) == "main"
	assert is_main(instance, main_focus)
	assert classify(instance, call_focus) == "call"
	assert not is_main(instance, call_focus)


def test_known_main_window_uses_the_handle_without_walking_uia_parents():
	class Focus:
		windowHandle = 100
		UIAAutomationId = "ComposeButton"

		@property
		def parent(self):
			raise AssertionError("known windows must not walk UIA parents")

	namespace = {
		"_MAIN_WINDOW_AUTOMATION_IDS": frozenset(("ChatsList", "Messages", "TextField", "Navigation")),
		"_CALL_WINDOW_AUTOMATION_IDS": frozenset(("ActiveButtons", "BottomRoot")),
		"_WINDOW_SURFACE_AUTOMATION_IDS": frozenset(
			("ChatsList", "Messages", "TextField", "Navigation", "ActiveButtons", "BottomRoot")
		),
		"_find_ancestor_by_automation_id": lambda *args, **kwargs: (_ for _ in ()).throw(
			AssertionError("known windows must not search UIA ancestors")
		),
	}
	classify = _load_app_method("_classify_window_surface", namespace)
	instance = SimpleNamespace(_mainWindowHandle=100, _callWindowHandles=set())

	assert classify(instance, Focus()) == "main"


def test_direct_marker_reclassifies_a_reused_window_handle():
	namespace = {
		"_MAIN_WINDOW_AUTOMATION_IDS": frozenset(("ChatsList", "Messages", "TextField", "Navigation")),
		"_CALL_WINDOW_AUTOMATION_IDS": frozenset(("ActiveButtons", "BottomRoot")),
		"_WINDOW_SURFACE_AUTOMATION_IDS": frozenset(
			("ChatsList", "Messages", "TextField", "Navigation", "ActiveButtons", "BottomRoot")
		),
		"_find_ancestor_by_automation_id": lambda *args, **kwargs: None,
	}
	classify = _load_app_method("_classify_window_surface", namespace)
	instance = SimpleNamespace(_mainWindowHandle=None, _callWindowHandles={200})
	chats = SimpleNamespace(UIAAutomationId="ChatsList", windowHandle=200)
	call = SimpleNamespace(UIAAutomationId="ActiveButtons", windowHandle=200)

	assert classify(instance, chats) == "main"
	assert instance._mainWindowHandle == 200
	assert 200 not in instance._callWindowHandles
	assert classify(instance, call) == "call"
	assert instance._mainWindowHandle is None
	assert 200 in instance._callWindowHandles


def test_overlay_selection_only_probes_direct_main_window_markers():
	chooser = next(
		node
		for node in _class_ast("AppModule").body
		if isinstance(node, ast.FunctionDef) and node.name == "chooseNVDAObjectOverlayClasses"
	)
	source = ast.unparse(chooser)

	assert "automation_id in _WINDOW_SURFACE_AUTOMATION_IDS" in source
	# An ancestor walk here would run for every object NVDA materializes.
	assert "_find_ancestor_by_automation_id(obj, _WINDOW_SURFACE_AUTOMATION_IDS" not in source


def test_call_control_detection_never_enumerates_siblings():
	class Node(SimpleNamespace):
		@property
		def children(self):
			raise AssertionError("call control siblings must not be materialized")

	container = Node(UIAAutomationId="ActiveButtons", parent=None)
	control = Node(UIAAutomationId="Mute", parent=container)
	find_ancestor = _load_module_function("_find_ancestor_by_automation_id", {})

	assert find_ancestor(control, ("ActiveButtons",), max_depth=4) is container


def test_call_state_announcements_use_the_nvda_main_loop(monkeypatch):
	scheduled = []
	monkeypatch.setitem(
		sys.modules,
		"core",
		SimpleNamespace(callLater=lambda delay, callback, *args: scheduled.append((delay, callback, args))),
	)
	announcements = []
	message = lambda text: announcements.append(text)
	method = _load_module_function("_announce_call_state_later", {"message": message})

	method("Microphone muted", 100)

	assert scheduled == [(100, message, ("Microphone muted",))]
	assert announcements == []


def test_auto_focus_stops_retrying_at_the_limit():
	retries = []
	instance = SimpleNamespace(
		_autoFocusChatListDone=False,
		_autoFocusChatListScheduled=True,
		_autoFocusChatListAttempts=9,
		_autoFocusChatListGeneration=3,
		script_toChatList=lambda gesture, arg=False: False,
		_scheduleAutoFocusChatList=lambda: retries.append(True),
		_classify_window_surface=lambda obj: "main",
		_is_focus_in_popup=lambda focus: False,
	)
	focus = SimpleNamespace(
		appModule=instance,
		isInForeground=True,
		role="pane",
		parent=None,
	)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"conf": SimpleNamespace(get=lambda key: True),
		"Role": SimpleNamespace(LISTITEM="listItem"),
		"log": SimpleNamespace(debug=lambda *args: None),
		"_AUTO_FOCUS_CHAT_LIST_RETRY_LIMIT": 10,
	}
	method = _load_app_method("_autoFocusChatListTick", namespace)

	method(instance, 3)

	assert not instance._autoFocusChatListDone
	assert instance._autoFocusChatListAttempts == 10
	assert retries == []


def test_auto_focus_checkbox_is_persisted_and_enabled_by_default():
	config_source = (ROOT / "addon" / "appModules" / "cnf.py").read_text(encoding="utf-8")
	settings_source = (
		ROOT / "addon" / "GlobalPlugins" / "UnigramPlus" / "__init__.py"
	).read_text(encoding="utf-8-sig")

	assert '"autoFocusChatList = boolean(default=True)"' in config_source
	assert 'conf.get("autoFocusChatList")' in settings_source
	assert 'conf.set("autoFocusChatList", self.autoFocusChatList.IsChecked())' in settings_source


def test_chat_list_items_receive_the_mention_navigation_overlay():
	app_module = _class_ast("AppModule")
	chooser = next(
		node
		for node in app_module.body
		if isinstance(node, ast.FunctionDef) and node.name == "chooseNVDAObjectOverlayClasses"
	)
	source = ast.unparse(chooser)

	assert "_is_chat_list_item(obj)" in source
	assert "clsList.insert(0, ChatListItem)" in source


def test_the_folder_unread_count_can_be_turned_off():
	announcements = []
	saved = {"last selected folder": "All"}
	instance = SimpleNamespace(
		saved_items=SimpleNamespace(
			get=lambda key: saved.get(key),
			save=lambda key, value: saved.__setitem__(key, value),
		),
	)
	get_name = _load_app_method("_get_chat_folder_name", {"re": re})
	instance._get_chat_folder_name = lambda name: get_name(instance, name)
	change_folder = _load_app_method(
		"change_chats_folder",
		{
			"_get_chat_folder_unread_count": _load_module_function(
				"_get_chat_folder_unread_count", {"re": re}
			),
			"message": lambda text: announcements.append(text),
			"conf": SimpleNamespace(get=lambda key: False),
			"queueHandler": SimpleNamespace(
				eventQueue=object(),
				queueFunction=lambda queue, callback, text: callback(text),
			),
		},
	)

	change_folder(instance, SimpleNamespace(name="Unread, 538"), None)

	assert announcements == ["Unread"]
