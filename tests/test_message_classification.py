import ast
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"
_UNSET = object()


class Node:
	def __init__(
		self,
		*,
		parent=None,
		role="listItem",
		automation_id="",
		class_name="",
		cached_class_name=_UNSET,
		selection_item_pattern=_UNSET,
		toggle_pattern=_UNSET,
		name="",
		focusable=True,
	):
		self.parent = parent
		self.role = role
		self.UIAAutomationId = automation_id
		self.UIAClassName = class_name
		self.UIAElement = SimpleNamespace(
			cachedClassName=class_name if cached_class_name is _UNSET else cached_class_name
		)
		if selection_item_pattern is not _UNSET:
			self.UIASelectionItemPattern = selection_item_pattern
		if toggle_pattern is not _UNSET:
			self.UIATogglePattern = toggle_pattern
		self.name = name
		self.isFocusable = focusable
		self.states = set()


def _source_module():
	return ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))


def _load_members(names, namespace):
	members = [
		node
		for node in _source_module().body
		if isinstance(node, ast.FunctionDef) and node.name in names
	]
	exec(compile(ast.Module(body=members, type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace


def _load_overlay_chooser(namespace):
	app_module = next(
		node for node in _source_module().body if isinstance(node, ast.ClassDef) and node.name == "AppModule"
	)
	chooser = next(
		node
		for node in app_module.body
		if isinstance(node, ast.FunctionDef) and node.name == "chooseNVDAObjectOverlayClasses"
	)
	chooser.decorator_list = []
	exec(compile(ast.Module(body=[chooser], type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace["chooseNVDAObjectOverlayClasses"]


def _message_predicate():
	namespace = {"Role": SimpleNamespace(LISTITEM="listItem")}
	_load_members({"_find_ancestor_by_automation_id", "_is_message_list_item"}, namespace)
	return namespace["_is_message_list_item"]


def _chat_predicate():
	namespace = {"Role": SimpleNamespace(LISTITEM="listItem")}
	_load_members({"_find_ancestor_by_automation_id", "_is_chat_list_item"}, namespace)
	return namespace["_is_chat_list_item"]


def _overlay_classes_for(obj, **extra_namespace):
	message_overlay = type("Message_list_item", (), {})
	chat_overlay = type("ChatListItem", (), {})
	namespace = {
		"Role": SimpleNamespace(LISTITEM="listItem", EDITABLETEXT="editableText", BUTTON="button"),
		"State": SimpleNamespace(SELECTED="selected"),
		"Message_list_item": message_overlay,
		"ChatListItem": chat_overlay,
		"EditableText": type("EditableText", (), {}),
		"Audio_and_video_button": type("Audio_and_video_button", (), {}),
		"keywordsInMessages": {"en": ("seen", "not seen", "Sent at", "Received at")},
		"conf": SimpleNamespace(get=lambda key: "en" if key == "lang" else "normal"),
		"_WINDOW_SURFACE_AUTOMATION_IDS": frozenset(),
		"_is_chat_list_item": _chat_predicate(),
		"_is_message_list_item": _message_predicate(),
		"is_recording_button": lambda candidate: False,
	}
	namespace.update(extra_namespace)
	chooser = _load_overlay_chooser(namespace)
	app = SimpleNamespace(
		isUnigramWindow=True,
		sender_message="unchanged",
		end_text="unchanged",
		_remember_messages_button=lambda candidate: None,
	)
	classes = []
	chooser(app, obj, classes)
	return classes, app, message_overlay, chat_overlay


def test_saved_messages_topics_with_received_or_sent_dates_are_not_messages():
	for name in (
		"某聊天室, 某訊息內容, 收到了 2026/8/31 下午 11:22",
		"某聊天室, 某訊息內容, 傳送於 2026/8/31 下午 11:22",
	):
		topic = Node(parent=Node(automation_id="ScrollingHost"), name=name)
		assert not _message_predicate()(topic)

		classes, app, message_overlay, _chat_overlay = _overlay_classes_for(topic)
		assert message_overlay not in classes
		assert app.sender_message == "unchanged"
		assert app.end_text == "unchanged"


def test_current_message_selectors_receive_message_overlay():
	messages = Node(automation_id="Messages", role="list")
	for automation_id, class_name in (
		("MessageSelector", ""),
		("", "MessageSelector"),
	):
		message = Node(
			parent=messages,
			automation_id=automation_id,
			class_name=class_name,
			name="Message body, Received at 2026/08/31 23:22",
		)

		assert _message_predicate()(message)
		classes, app, message_overlay, _chat_overlay = _overlay_classes_for(message)
		assert message_overlay in classes
		assert app.sender_message == "received"


def test_current_toggle_button_message_selector_receives_message_overlay():
	"""Unigram 12.10.2 exposes MessageSelector as a ToggleButton with selection support."""
	message = Node(
		parent=Node(automation_id="Messages", role="list"),
		class_name="ToggleButton",
		selection_item_pattern=object(),
		toggle_pattern=None,
	)

	assert _message_predicate()(message)
	classes, _app, message_overlay, _chat_overlay = _overlay_classes_for(message)
	assert message_overlay in classes


def test_legacy_message_marker_and_blank_service_messages_remain_messages():
	message = Node(parent=Node(), automation_id="Message_item", name="")

	assert _message_predicate()(message)
	classes, _app, message_overlay, _chat_overlay = _overlay_classes_for(message)
	assert message_overlay in classes


def test_empty_cached_uia_class_falls_back_to_the_live_message_class():
	messages = Node(automation_id="Messages", role="list")
	for cached_class_name, class_name, selection_item_pattern, toggle_pattern in (
		("", "ToggleButton", object(), None),
		(None, "MessageSelector", _UNSET, _UNSET),
	):
		message = Node(
			parent=messages,
			class_name=class_name,
			cached_class_name=cached_class_name,
			selection_item_pattern=selection_item_pattern,
			toggle_pattern=toggle_pattern,
		)

		assert _message_predicate()(message)
		classes, _app, message_overlay, _chat_overlay = _overlay_classes_for(message)
		assert message_overlay in classes


def test_unigram_12102_reaction_toggle_button_does_not_receive_message_overlay():
	"""5.6.9/5.7.0 misclassified reactions as messages; keep their native Toggle semantics."""
	reaction = Node(
		parent=Node(automation_id="Messages", role="list"),
		class_name="ToggleButton",
		selection_item_pattern=None,
		toggle_pattern=object(),
		name="43 people reacted with grinning face",
	)

	assert not _message_predicate()(reaction)
	classes, _app, message_overlay, _chat_overlay = _overlay_classes_for(reaction)
	assert message_overlay not in classes


def test_generic_message_subtree_toggle_button_does_not_receive_message_overlay():
	control = Node(
		parent=Node(automation_id="Messages", role="list"),
		class_name="ToggleButton",
		selection_item_pattern=None,
		toggle_pattern=object(),
	)

	assert not _message_predicate()(control)
	classes, _app, message_overlay, _chat_overlay = _overlay_classes_for(control)
	assert message_overlay not in classes


def test_toggle_button_with_unavailable_pattern_information_fails_closed():
	control = Node(parent=Node(automation_id="Messages", role="list"), class_name="ToggleButton")

	assert not _message_predicate()(control)
	classes, _app, message_overlay, _chat_overlay = _overlay_classes_for(control)
	assert message_overlay not in classes


def test_toggle_button_list_items_outside_messages_do_not_receive_message_overlay():
	for automation_id in ("CallsList", "SettingsList", "ScrollingHost"):
		control = Node(parent=Node(automation_id=automation_id), class_name="ToggleButton")

		assert not _message_predicate()(control)
		classes, _app, message_overlay, _chat_overlay = _overlay_classes_for(control)
		assert message_overlay not in classes


def test_chat_rows_with_message_like_summaries_keep_the_chat_overlay():
	chat = Node(
		parent=Node(automation_id="ChatsList"),
		name="Group, last message, Received at 2026/08/31 23:22",
	)

	assert not _message_predicate()(chat)
	classes, _app, message_overlay, chat_overlay = _overlay_classes_for(chat)
	assert message_overlay not in classes
	assert chat_overlay in classes


def test_navigation_tabs_keep_their_native_enter_and_space():
	"""Unigram names several tab lists "Navigation", not only the settings one.

	The sticker panel's Emoji, GIFs and Stickers tabs are focusable rows of
	such a list. The settings-category overlay removed in 5.8.3 matched them
	too and took over Enter and Space there.
	"""
	tabs = Node(automation_id="Navigation", role="list")
	for name in ("Emoji", "GIFs", "Stickers"):
		tab = Node(parent=tabs, class_name="TopNavViewItem", name=name)

		# Defined so that a chooser still naming the old overlay would add it,
		# rather than fail on the name inside its catch-all.
		classes, _app, _message_overlay, _chat_overlay = _overlay_classes_for(
			tab, SettingsPanelListItem=type("SettingsPanelListItem", (), {})
		)
		assert classes == [], name


def test_message_overlay_does_not_override_the_provider_automation_id():
	message_class = next(
		node
		for node in _source_module().body
		if isinstance(node, ast.ClassDef) and node.name == "Message_list_item"
	)
	assert not any(
		isinstance(node, ast.Assign)
		and any(isinstance(target, ast.Name) and target.id == "UIAAutomationId" for target in node.targets)
		for node in message_class.body
	)


def test_a_realized_message_with_no_readable_uia_class_is_still_a_message():
	"""Taken from a live Unigram: a focused voice message reported no class at all.

	Rejecting it there disabled every message-only shortcut on that message,
	including Space to play it and Enter to reply. The selection semantics below
	are the real discriminator, so an unreadable class must not decide the
	question on its own.
	"""
	messages = Node(automation_id="Messages", role="list")
	row = Node(parent=messages, class_name="ListViewItem")
	message = Node(
		parent=row,
		class_name=None,
		cached_class_name=None,
		selection_item_pattern=object(),
		toggle_pattern=None,
		name="علی, Owner. Voice message, 00:18, Received at 3:30 PM",
	)

	assert _message_predicate()(message)
	classes, _app, message_overlay, _chat_overlay = _overlay_classes_for(message)
	assert message_overlay in classes


def test_an_unreadable_class_without_selection_semantics_is_still_rejected():
	# The reaction buttons fixed in 5.7.1 must not slip through the same gap.
	messages = Node(automation_id="Messages", role="list")
	for selection_item_pattern, toggle_pattern in ((None, object()), (None, None)):
		control = Node(
			parent=messages,
			class_name=None,
			cached_class_name=None,
			selection_item_pattern=selection_item_pattern,
			toggle_pattern=toggle_pattern,
		)

		assert not _message_predicate()(control)


def test_an_unreadable_class_outside_messages_is_rejected():
	control = Node(
		parent=Node(automation_id="ScrollingHost"),
		class_name=None,
		cached_class_name=None,
		selection_item_pattern=object(),
		toggle_pattern=None,
	)

	assert not _message_predicate()(control)


def test_a_message_is_recognized_once_its_parent_chain_becomes_reachable():
	"""Overlay selection runs while NVDA is still constructing the object.

	The parent chain can be unreachable for that moment. Remembering that miss
	made the message permanently unrecognized, so Space, Enter, ALT+D and every
	other message-only shortcut stayed inactive on it for as long as the object
	lived.
	"""
	messages = Node(automation_id="Messages", role="list")
	message = Node(
		class_name="ToggleButton",
		selection_item_pattern=object(),
		toggle_pattern=None,
	)
	message.parent = None  # not reachable yet

	predicate = _message_predicate()
	assert not predicate(message)

	message.parent = messages  # NVDA finished building it
	assert predicate(message)


def test_a_recognized_message_is_not_re_probed():
	messages = Node(automation_id="Messages", role="list")
	message = Node(
		parent=messages,
		class_name="ToggleButton",
		selection_item_pattern=object(),
		toggle_pattern=None,
	)
	predicate = _message_predicate()

	assert predicate(message)

	# The answer is kept, so the ancestor walk is not paid for again.
	message.parent = None
	assert predicate(message)


class _RawElement:
	"""A UIA element chain, the way it is readable before NVDA builds objects."""

	def __init__(self, automation_id="", parent=None):
		self.CurrentAutomationId = automation_id
		self._parent = parent


class _RawWalker:
	def GetParentElement(self, element):
		return element._parent


def test_the_messages_ancestor_is_found_through_raw_uia_before_nvda_objects_exist():
	"""Overlay selection decides once, so it must not depend on NVDA's parents.

	If the parent chain is unreachable at that moment, the message never gets
	its overlay, and Enter, ALT+C and the message arrow keys stay dead on it for
	as long as it lives. The raw element chain is readable right away.
	"""
	import sys
	from types import SimpleNamespace

	namespace = {"Role": SimpleNamespace(LISTITEM="listItem", WINDOW="window")}
	_load_members({"_find_ancestor_by_automation_id"}, namespace)
	find_ancestor = namespace["_find_ancestor_by_automation_id"]

	messages_element = _RawElement("Messages")
	row_element = _RawElement("", messages_element)
	message = Node(class_name="ToggleButton")
	message.parent = None  # NVDA cannot walk up yet
	message.UIAElement = _RawElement("", row_element)

	sys.modules["UIAHandler"] = SimpleNamespace(
		handler=SimpleNamespace(baseTreeWalker=_RawWalker())
	)
	try:
		found = find_ancestor(message, ("Messages",), max_depth=8)
		assert found is not None
		assert found.UIAAutomationId == "Messages"
	finally:
		del sys.modules["UIAHandler"]
