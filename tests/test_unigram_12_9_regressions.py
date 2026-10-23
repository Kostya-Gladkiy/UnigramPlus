import ast
import sys
import threading
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"


class Node:
	def __init__(
		self,
		name="",
		children=None,
		role=None,
		parent=None,
		automation_id="",
		class_name="",
		focusable=True,
	):
		self.name = name
		self.children = children or []
		self.role = role
		self.parent = parent
		self.UIAAutomationId = automation_id
		self.UIAClassName = class_name
		self.isFocusable = focusable
		self.states = set()
		self.next = None
		self.previous = None
		self.actions = 0
		for index, child in enumerate(self.children):
			child.parent = self
			child.previous = self.children[index - 1] if index else None
			child.next = self.children[index + 1] if index + 1 < len(self.children) else None

	@property
	def childCount(self):
		return len(self.children)

	@property
	def firstChild(self):
		return self.children[0] if self.children else None

	def doAction(self):
		self.actions += 1

	@property
	def lastChild(self):
		return self.children[-1] if self.children else None


def _load_module_members(names, namespace):
	module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
	members = []
	for node in module.body:
		if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names:
			if isinstance(node, ast.FunctionDef):
				node.decorator_list = []
			members.append(node)
	exec(compile(ast.Module(body=members, type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace


def _load_app_method(name, namespace):
	module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
	app_module = next(
		node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule"
	)
	method = next(node for node in app_module.body if isinstance(node, ast.FunctionDef) and node.name == name)
	method.decorator_list = []
	exec(compile(ast.Module(body=[method], type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace[name]


def test_context_menu_icon_matching_handles_unigram_12_9_wrappers_and_cycles():
	namespace = _load_module_members(
		{"_walk_bounded_descendants", "_menu_item_has_icon"},
		{},
	)
	icon = Node("\ue74d")
	wrapper = Node(children=[Node(children=[icon])])
	icon.children = [wrapper]

	assert namespace["_menu_item_has_icon"](wrapper, "\ue74d")
	assert not namespace["_menu_item_has_icon"](wrapper, "\ue8b2")


def test_raw_context_menu_item_is_invoked_by_unigrams_font_icon(monkeypatch):
	invocations = []
	conditions = []

	class TextRange:
		def __init__(self, text):
			self.text = text

		def GetText(self, limit):
			assert limit == 64
			return self.text

	class TextPattern:
		def __init__(self, text):
			self.DocumentRange = TextRange(text)

		def QueryInterface(self, interface):
			assert interface == "textInterface"
			return self

	class InvokePattern:
		def QueryInterface(self, interface):
			assert interface == "invokeInterface"
			return self

		def Invoke(self):
			invocations.append(True)

	class RawElement:
		def __init__(
			self,
			control_type,
			parent=None,
			first_child=None,
			class_name="",
			automation_id="",
			name="",
			value="",
			text="",
		):
			self.parent = parent
			self.first_child = first_child
			self.properties = {
				"controlType": control_type,
				"className": class_name,
				"automationId": automation_id,
				"name": name,
				"value": value,
				"legacyValue": "",
				"textAvailable": bool(text),
			}
			self.text = text

		def GetCachedPropertyValueEx(self, property_id, ignore_default):
			assert ignore_default
			return self.properties[property_id]

		def GetCurrentPattern(self, pattern_id):
			if pattern_id == "invokePattern":
				return InvokePattern()
			if pattern_id == "textPattern" and self.text:
				return TextPattern(self.text)
			raise LookupError(pattern_id)

		def GetCachedPattern(self, pattern_id):
			return self.GetCurrentPattern(pattern_id)

	class ElementArray:
		def __init__(self, elements):
			self.elements = elements
			self.length = len(elements)

		def getElement(self, index):
			return self.elements[index]

	class Root:
		def __init__(self, menu_items, parent=None):
			self.menu_items = menu_items
			self.parent = parent
			self.find_all_calls = 0

		def findAll(self, scope, condition):
			assert scope == "descendants"
			self.find_all_calls += 1
			parts = condition[1] if condition[0] == "and" else (condition,)
			assert ("controlType", "menuItem") in parts
			return ElementArray(self.menu_items)

	class Client:
		@staticmethod
		def CreatePropertyCondition(property_id, value):
			conditions.append((property_id, value))
			return (property_id, value)

		@staticmethod
		def CreateAndConditionFromArray(parts):
			return ("and", tuple(parts))

		@staticmethod
		def CompareElements(first, second):
			return first is second

	class Walker:
		@staticmethod
		def getParentElement(element):
			return element.parent

		@staticmethod
		def GetFirstChildElementBuildCache(element, cache_request):
			assert cache_request == "baseCache"
			return element.first_child

	def menu_item_with_icon(icon):
		font_icon = RawElement("text", class_name="FontIcon", text=icon)
		icon_content = RawElement(
			"group",
			first_child=font_icon,
			class_name="ContentPresenter",
			automation_id="IconContent",
		)
		viewbox = RawElement("group", first_child=icon_content, class_name="Viewbox")
		layout = RawElement(
			"group",
			first_child=viewbox,
			class_name="Grid",
			automation_id="LayoutRoot",
		)
		return RawElement("menuItem", first_child=layout, class_name="MenuFlyoutItem")

	desktop_root = Root([])
	nonmatching_item = menu_item_with_icon("\ue104")
	menu_item = menu_item_with_icon("\ue248")
	common_xaml_root = Root([nonmatching_item, menu_item], parent=desktop_root)
	focused_popup = SimpleNamespace(
		processID=4242,
		UIAElement=Root([], parent=common_xaml_root),
	)
	monkeypatch.setitem(
		sys.modules,
		"UIAHandler",
		SimpleNamespace(
			handler=SimpleNamespace(
				clientObject=Client(),
				baseTreeWalker=Walker(),
				baseCacheRequest="baseCache",
				rootElement=desktop_root,
			),
			UIA=SimpleNamespace(
				UIA_NamePropertyId="name",
				UIA_ValueValuePropertyId="value",
				UIA_IsTextPatternAvailablePropertyId="textAvailable",
				UIA_ClassNamePropertyId="className",
				UIA_AutomationIdPropertyId="automationId",
				UIA_ProcessIdPropertyId="processId",
				UIA_ControlTypePropertyId="controlType",
				UIA_MenuItemControlTypeId="menuItem",
			),
			UIA_LegacyIAccessibleValuePropertyId="legacyValue",
			TreeScope_Descendants="descendants",
			UIA_TextPatternId="textPattern",
			IUIAutomationTextPattern="textInterface",
			UIA_InvokePatternId="invokePattern",
			IUIAutomationInvokePattern="invokeInterface",
		),
	)
	namespace = _load_module_members(
		{
			"_raw_uia_property",
			"_raw_uia_text",
			"_raw_menu_item_has_icon",
			"_find_raw_context_menu_item_by_icon",
			"_invoke_raw_context_menu_option",
		},
		{
			"_CONTEXT_MENU_RAW_SCOPE_LIMIT": 6,
			"_CONTEXT_MENU_RAW_ITEM_DEPTH_LIMIT": 10,
			"_CONTEXT_MENU_RAW_TEXT_LIMIT": 64,
			"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
		},
	)

	assert namespace["_invoke_raw_context_menu_option"](
		focused_popup,
		("\ue91d", "\ue248"),
		4242,
	)
	assert conditions.count(("controlType", "menuItem")) == 2
	assert conditions.count(("processId", 4242)) == 2
	assert not any(property_id == "name" for property_id, value in conditions)
	assert desktop_root.find_all_calls == 0
	assert invocations == [True]


def test_chat_deletion_does_not_wait_for_a_menu_focus_event():
	source = SOURCE_PATH.read_text(encoding="utf-8")

	assert "if state == 0:" not in source


def test_shift_delete_uses_unigrams_native_delete_for_messages():
	sent = []
	scheduled = []
	focus = Node(parent=Node(role="group"))
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"Role": SimpleNamespace(LISTITEM="listItem"),
		"conf": SimpleNamespace(get=lambda key: False),
		"core": SimpleNamespace(callLater=lambda *args: scheduled.append(args)),
		"_": lambda text: text,
	}
	_load_module_members({"_relative"}, namespace)
	method = _load_app_method("startDeleteMessage", namespace)
	instance = SimpleNamespace(
		is_message_object=lambda obj: True,
		keys={
			"delete": SimpleNamespace(send=lambda: sent.append("delete")),
			"Applications": SimpleNamespace(send=lambda: sent.append("applications")),
		},
		_expire_native_delete=lambda pending: None,
	)

	assert method(instance, True, True)
	assert sent == ["delete"]
	assert instance.isDelete["state"] == 1
	assert instance.isDelete["isCompleteDeletion"] is True
	assert len(scheduled) == 1
	assert scheduled[0][0] == 20000
	assert scheduled[0][2] is instance.isDelete


def test_native_delete_preserves_the_confirmation_dialog_setting():
	sent = []
	focus = Node(parent=Node(role="group"))
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"Role": SimpleNamespace(LISTITEM="listItem"),
		"conf": SimpleNamespace(get=lambda key: True),
		"core": SimpleNamespace(
			callLater=lambda *args: (_ for _ in ()).throw(
				AssertionError("confirmed deletion must not schedule automatic activation")
			),
		),
		"_": lambda text: text,
	}
	_load_module_members({"_relative"}, namespace)
	method = _load_app_method("startDeleteMessage", namespace)
	instance = SimpleNamespace(
		is_message_object=lambda obj: True,
		keys={
			"delete": SimpleNamespace(send=lambda: sent.append("delete")),
			"Applications": SimpleNamespace(send=lambda: sent.append("applications")),
		},
		_expire_native_delete=lambda pending: None,
	)

	assert method(instance, True, True)
	assert sent == ["delete"]
	assert instance.isDelete is False


def test_shift_delete_keeps_context_menu_fallback_for_chat_rows():
	sent = []
	chat_list = Node(automation_id="ChatsList")
	focus = Node(children=[Node(), Node("ordinary chat")], parent=chat_list)
	namespace = {
		"api": SimpleNamespace(getFocusObject=lambda: focus),
		"Role": SimpleNamespace(LISTITEM="listItem"),
		"conf": SimpleNamespace(get=lambda key: False),
		"_is_chat_list_item": lambda obj: obj is focus,
		"icons_from_context_menu": {"delete": "delete"},
		"_": lambda text: text,
	}
	_load_module_members({"_relative"}, namespace)
	method = _load_app_method("startDeleteMessage", namespace)
	instance = SimpleNamespace(
		is_message_object=lambda obj: False,
		keys={
			"delete": SimpleNamespace(send=lambda: sent.append("delete")),
			"Applications": SimpleNamespace(send=lambda: sent.append("applications")),
		},
		activate_option_for_menu=lambda option, list_name: sent.append((option, list_name)) or True,
	)

	assert method(instance, True, True)
	assert sent == [(("delete",), "ChatsList")]
	assert instance.isDelete["state"] == 1


def test_native_delete_activates_the_focused_primary_button_from_the_popup():
	class UnexpectedAdjacentTarget:
		@property
		def location(self):
			raise AssertionError("native deletion must not inspect cached adjacent rows")

	role = SimpleNamespace(MENUITEM="menuItem", CHECKBOX="checkBox", BUTTON="button")
	state = SimpleNamespace(CHECKED="checked")
	primary = Node(role=role.BUTTON, automation_id="PrimaryButton")
	namespace = {
		"Role": role,
		"State": state,
		"conf": SimpleNamespace(get=lambda key: False),
		"speech": SimpleNamespace(cancelSpeech=lambda: None),
	}
	method = _load_app_method("deleteMessageAndChat", namespace)
	instance = SimpleNamespace(
		isDelete={
			"state": 1,
			"isCompleteDeletion": True,
			"elements": [UnexpectedAdjacentTarget()],
			"list": "other",
			"nativeDelete": True,
		},
		_find_deletion_primary_button=lambda obj: False,
	)

	assert method(instance, primary)

	assert primary.actions == 1
	assert instance.isDelete["state"] == 2
	assert "def _find_deletion_primary_button" in SOURCE_PATH.read_text(encoding="utf-8")


def test_native_delete_ignores_unrelated_buttons_while_the_popup_is_loading():
	role = SimpleNamespace(MENUITEM="menuItem", CHECKBOX="checkBox", BUTTON="button")
	cancelled = []
	namespace = {
		"Role": role,
		"State": SimpleNamespace(CHECKED="checked"),
		"conf": SimpleNamespace(get=lambda key: False),
		"speech": SimpleNamespace(cancelSpeech=lambda: cancelled.append(True)),
	}
	method = _load_app_method("deleteMessageAndChat", namespace)
	pending = {
		"state": 1,
		"isCompleteDeletion": True,
		"elements": [],
		"list": "messages",
		"nativeDelete": True,
	}
	instance = SimpleNamespace(isDelete=pending)

	for automation_id in ("CalendarButton", "Attach", "SecondaryButton", ""):
		button = Node(role=role.BUTTON, automation_id=automation_id)
		assert not method(instance, button)
		assert button.actions == 0

	assert instance.isDelete is pending
	assert pending["state"] == 1
	assert cancelled == []


def test_native_delete_checkbox_is_only_toggled_when_delete_for_everyone_is_unchecked():
	role = SimpleNamespace(MENUITEM="menuItem", CHECKBOX="checkBox", BUTTON="button")
	state = SimpleNamespace(CHECKED="checked")
	namespace = {
		"Role": role,
		"State": state,
		"conf": SimpleNamespace(get=lambda key: False),
		"speech": SimpleNamespace(cancelSpeech=lambda: None),
	}
	method = _load_app_method("deleteMessageAndChat", namespace)
	pending = {
		"state": 1,
		"isCompleteDeletion": True,
		"elements": [],
		"list": "messages",
		"nativeDelete": True,
	}
	instance = SimpleNamespace(
		isDelete=pending,
		_find_deletion_primary_button=lambda obj: False,
	)
	checkbox = Node(role=role.CHECKBOX, automation_id="RevokeCheck")

	assert method(instance, checkbox)
	assert checkbox.actions == 1
	assert pending["state"] == 1
	checkbox.states.add(state.CHECKED)
	assert method(instance, checkbox)
	assert checkbox.actions == 1
	assert pending["state"] == 1


def test_native_delete_timeout_only_clears_the_request_that_scheduled_it():
	method = _load_app_method("_expire_native_delete", {})
	first = {"state": 1}
	second = {"state": 1}
	instance = SimpleNamespace(isDelete=second)

	method(instance, first)
	assert instance.isDelete is second
	method(instance, second)
	assert instance.isDelete is False


def test_context_menu_delete_finds_the_popup_primary_button_by_automation_id():
	role = SimpleNamespace(MENUITEM="menuItem", CHECKBOX="checkBox", BUTTON="button")
	state = SimpleNamespace(CHECKED="checked")
	checkbox = Node(role=role.CHECKBOX, automation_id="CheckBox")
	primary = Node(role=role.BUTTON, automation_id="PrimaryButton")
	popup = Node(children=[checkbox, primary])
	namespace = {
		"Role": role,
		"State": state,
		"conf": SimpleNamespace(get=lambda key: False),
		"speech": SimpleNamespace(cancelSpeech=lambda: None),
	}
	method = _load_app_method("deleteMessageAndChat", namespace)
	instance = SimpleNamespace(
		isDelete={
			"state": 1,
			"isCompleteDeletion": True,
			"elements": [],
			"list": "other",
			"nativeDelete": False,
		},
		_find_deletion_primary_button=lambda obj: primary if obj is checkbox else False,
	)

	method(instance, checkbox)

	assert checkbox.actions == 1
	assert primary.actions == 1
	assert instance.isDelete["state"] == 2


def test_chat_delete_popup_without_checkbox_uses_its_primary_button():
	role = SimpleNamespace(MENUITEM="menuItem", CHECKBOX="checkBox", BUTTON="button")
	primary = Node(role=role.BUTTON, automation_id="PrimaryButton")
	namespace = {
		"Role": role,
		"State": SimpleNamespace(CHECKED="checked"),
		"conf": SimpleNamespace(get=lambda key: False),
		"speech": SimpleNamespace(cancelSpeech=lambda: None),
	}
	method = _load_app_method("deleteMessageAndChat", namespace)
	instance = SimpleNamespace(
		isDelete={
			"state": 1,
			"isCompleteDeletion": True,
			"elements": [],
			"list": "chats",
			"nativeDelete": False,
		},
		script_toChatList=lambda gesture: None,
	)

	assert method(instance, primary)
	assert primary.actions == 1
	assert instance.isDelete["state"] == 2


def test_inline_button_workaround_was_removed_after_unigram_fixed_its_automation_peer():
	source = SOURCE_PATH.read_text(encoding="utf-8")

	# Unigram 12.9.1 now exposes reply-markup labels through GetNameCore. Keeping
	# any raw TextPattern probing here would reintroduce multi-second UIA stalls
	# while NVDA materializes messages, bot lists, chat rows, or reaction popups.
	for removed_symbol in (
		"_clean_inline_button_text",
		"_is_inline_button_list_item",
		"_inline_button_descendant_text",
		"_queue_inline_button_text_read",
		"ReplyMarkupInlineButtonListItem",
		"_unigramPlusInlineButtonName",
	):
		assert removed_symbol not in source


def test_saved_messages_topic_workaround_is_absent_after_unigram_native_fix():
	source = SOURCE_PATH.read_text(encoding="utf-8")

	assert "_SAVED_MESSAGES_TOPIC_TYPE_NAME" not in source
	assert "_repair_saved_messages_topic_name" not in source
	assert "Telegram.Td.Api.SavedMessagesTopic" not in source


def test_saved_items_uses_only_a_valid_focused_window_handle():
	focus = SimpleNamespace(windowHandle=200)
	namespace = _load_module_members(
		{"Saved_items"},
		{"api": SimpleNamespace(getFocusObject=lambda: focus)},
	)
	saved_items = namespace["Saved_items"]()
	saved_items._items = {}

	saved_items.save("last message", "message in first window")
	assert saved_items.get("last message") == "message in first window"

	focus.windowHandle = 201
	assert saved_items.get("last message") is False
	saved_items.save("last message", "message in second window")
	assert saved_items._items == {
		200: {"last message": "message in first window"},
		201: {"last message": "message in second window"},
	}

	for invalid_window_handle in (None, 0, -1, True, "201"):
		focus = SimpleNamespace(windowHandle=invalid_window_handle)
		assert saved_items.get("last message") is False
		saved_items.save("last message", "must not be cached")

	focus = SimpleNamespace()
	assert saved_items.get("last message") is False
	saved_items.save("last message", "must not be cached")
	assert saved_items._items == {
		200: {"last message": "message in first window"},
		201: {"last message": "message in second window"},
	}


def test_shift_delete_remains_bound_but_alt_end_is_removed():
	source = SOURCE_PATH.read_text(encoding="utf-8")

	assert 'gesture="kb:shift+delete"' in source
	assert 'gesture="kb:ALT+end"' not in source
	assert "def script_to_down" not in source


def test_alt_c_web_view_code_and_setting_are_removed():
	config = (ROOT / "addon" / "appModules" / "cnf.py").read_text(encoding="utf-8")
	settings = (ROOT / "addon" / "GlobalPlugins" / "UnigramPlus" / "__init__.py").read_text(
		encoding="utf-8-sig"
	)
	app = SOURCE_PATH.read_text(encoding="utf-8")

	assert "displayMessagesInWebView" not in config + settings + app
	assert "browseableMessage" not in app
	assert not (ROOT / "addon" / "appModules" / "rich_message_dialog.py").exists()


def test_current_unigram_message_selector_is_recognized_without_legacy_automation_id():
	role = SimpleNamespace(LISTITEM="listItem")
	namespace = _load_module_members(
		{"_find_ancestor_by_automation_id", "_is_message_list_item"},
		{"Role": role},
	)
	messages = Node(role="list", automation_id="Messages")
	container = Node(role=role.LISTITEM, parent=messages)
	selector = Node(role=role.LISTITEM, parent=container, class_name="MessageSelector")

	assert namespace["_is_message_list_item"](selector)
	assert not namespace["_is_message_list_item"](
		Node(role=role.LISTITEM, parent=container, class_name="ReactionButton")
	)


def test_wrapped_chat_row_is_accepted_for_alt_shift_r_context_menu():
	role = SimpleNamespace(LISTITEM="listItem")
	namespace = _load_module_members(
		{"_find_ancestor_by_automation_id", "_is_chat_list_item"},
		{"Role": role},
	)
	chat_list = Node(role="list", automation_id="ChatsList")
	wrapper = Node(parent=chat_list)
	chat = Node(role=role.LISTITEM, parent=wrapper, class_name="ChatListListViewItem")

	assert namespace["_is_chat_list_item"](chat)
	assert not namespace["_is_chat_list_item"](
		Node(role=role.LISTITEM, parent=Node(automation_id="SettingsList"))
	)


def test_enter_opens_the_reply_context_menu_for_current_message_selectors():
	sent = []
	armed = []
	probes = []
	focus = Node(class_name="MessageSelector", role="listItem")
	method = _load_app_method(
		"activate_option_for_menu",
		{
			"api": SimpleNamespace(getFocusObject=lambda: focus),
			"_is_chat_list_item": lambda obj: False,
			"_CONTEXT_MENU_OPEN_TIMEOUT_MS": 10000,
		},
	)
	instance = SimpleNamespace(
		execute_context_menu_option=False,
		is_message_object=lambda obj: True,
		keys={"Applications": SimpleNamespace(send=lambda: sent.append("applications"))},
		_arm_context_menu_timeout=lambda pending, delay: armed.append((pending, delay)),
		_schedule_context_menu_raw_probe=lambda root, pending: probes.append((root, pending)),
	)

	assert method(instance, "replyIcon", "Messages")
	assert instance.execute_context_menu_option == {
		"icons": "replyIcon",
		"processID": 0,
		"moves": 0,
		"navigationScheduled": False,
		"timeoutToken": 0,
		"rawProbeToken": 0,
		"rawProbeAttempts": 0,
		"rawProbeDiagnosed": False,
		"rawProbeObjectPriority": -1,
		"rawInvoked": False,
	}
	assert sent == ["applications"]
	assert armed == [(instance.execute_context_menu_option, 10000)]
	assert probes == [(None, instance.execute_context_menu_option)]


def test_alt_shift_r_opens_the_context_menu_for_wrapped_chat_rows():
	sent = []
	armed = []
	probes = []
	focus = Node(class_name="ChatListListViewItem", role="listItem")
	method = _load_app_method(
		"activate_option_for_menu",
		{
			"api": SimpleNamespace(getFocusObject=lambda: focus),
			"_is_chat_list_item": lambda obj: True,
			"_CONTEXT_MENU_OPEN_TIMEOUT_MS": 10000,
		},
	)
	instance = SimpleNamespace(
		execute_context_menu_option=False,
		is_message_object=lambda obj: False,
		keys={"Applications": SimpleNamespace(send=lambda: sent.append("applications"))},
		_arm_context_menu_timeout=lambda pending, delay: armed.append((pending, delay)),
		_schedule_context_menu_raw_probe=lambda root, pending: probes.append((root, pending)),
	)

	assert method(instance, ("readIcon", "unreadIcon"), "ChatsList")
	assert instance.execute_context_menu_option == {
		"icons": ("readIcon", "unreadIcon"),
		"processID": 0,
		"moves": 0,
		"navigationScheduled": False,
		"timeoutToken": 0,
		"rawProbeToken": 0,
		"rawProbeAttempts": 0,
		"rawProbeDiagnosed": False,
		"rawProbeObjectPriority": -1,
		"rawInvoked": False,
	}
	assert sent == ["applications"]
	assert armed == [(instance.execute_context_menu_option, 10000)]
	assert probes == [(None, instance.execute_context_menu_option)]


def test_context_menu_popup_focus_schedules_raw_probe_without_walking_nvda_objects():
	role = SimpleNamespace(
		MENUITEM="menuItem",
		LINK="link",
		BUTTON="button",
		WINDOW="window",
		POPUPMENU="popupMenu",
		MENU="menu",
	)
	scheduled = []
	next_calls = []
	probes = []
	method = _load_app_method(
		"_handle_pending_context_menu_focus",
		{
			"Role": role,
			"_menu_item_has_icon": lambda obj, icons: (_ for _ in ()).throw(
				AssertionError("popup descendants must not be inspected")
			),
			"core": SimpleNamespace(callLater=lambda *args: scheduled.append(args)),
			"_CONTEXT_MENU_STEP_DELAY_MS": 20,
			"_CONTEXT_MENU_NAVIGATION_DELAY_MS": 250,
			"_CONTEXT_MENU_NAVIGATION_LIMIT": 30,
		},
	)
	pending = {"icons": "\ue248", "moves": 0}
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		keys={},
		_invoke_context_menu_item=lambda item: None,
		_arm_context_menu_timeout=lambda pending, delay: None,
		_find_context_menu_command=lambda obj, icons: None,
		_schedule_context_menu_raw_probe=lambda obj, request: probes.append((obj, request)),
	)
	popup = Node(role="window", children=[Node(children=[Node(children=[Node()])])])

	assert method(instance, popup, lambda: next_calls.append(True))
	assert instance.execute_context_menu_option is pending
	assert next_calls == [True]
	assert scheduled == []
	assert probes == [(popup, pending)]


def test_context_menu_popup_focus_storm_does_not_restart_the_raw_probe_chain():
	scheduled = []
	priority = _load_module_members({"_context_menu_raw_probe_hint_priority"}, {})[
		"_context_menu_raw_probe_hint_priority"
	]
	method = _load_app_method(
		"_schedule_context_menu_raw_probe",
		{
			"core": SimpleNamespace(callLater=lambda *args: scheduled.append(args)),
			"_CONTEXT_MENU_RAW_PROBE_DELAY_MS": 50,
			"_context_menu_raw_probe_hint_priority": priority,
		},
	)
	pending = {
		"rawProbeToken": 0,
		"rawProbeAttempts": 0,
		"rawProbeDiagnosed": False,
		"rawInvoked": False,
	}
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		_queue_context_menu_raw_probe=lambda *args: None,
	)

	assert method(instance, None, pending)
	assert pending["rawProbeToken"] == 1
	assert len(scheduled) == 1

	pending["rawProbeAttempts"] = 3
	pending["rawProbeDiagnosed"] = True
	first_popup = Node(class_name="PopupRoot")
	latest_popup = Node(class_name="MenuFlyoutPresenter")
	generic_window = Node(name="Unigram", class_name="Window")
	assert method(instance, first_popup, pending)
	assert method(instance, latest_popup, pending)
	assert method(instance, generic_window, pending)

	assert pending["rawProbeToken"] == 1
	assert pending["rawProbeAttempts"] == 3
	assert pending["rawProbeDiagnosed"] is True
	assert pending["rawProbeObject"] is latest_popup
	assert pending["rawProbeObjectPriority"] == 2
	assert len(scheduled) == 1


def test_context_menu_focus_after_raw_invoke_only_continues_the_event_chain():
	method = _load_app_method("_handle_pending_context_menu_focus", {})
	pending = {"rawInvoked": True}
	next_calls = []
	instance = SimpleNamespace(execute_context_menu_option=pending)

	assert method(instance, object(), lambda: next_calls.append(True))
	assert instance.execute_context_menu_option is pending
	assert next_calls == [True]


def test_context_menu_focused_item_is_invoked_by_unigrams_icon_not_its_translation():
	role = SimpleNamespace(MENUITEM="menuItem", LINK="link", BUTTON="button")
	scheduled = []
	namespace = _load_module_members(
		{"_walk_bounded_descendants", "_menu_item_has_icon"},
		{"Role": role},
	)
	namespace.update(
		{
			"_claim_context_menu_option": _load_context_menu_claim(),
			"core": SimpleNamespace(callLater=lambda *args: scheduled.append(args)),
			"_CONTEXT_MENU_STEP_DELAY_MS": 20,
			"_CONTEXT_MENU_NAVIGATION_DELAY_MS": 250,
			"_CONTEXT_MENU_NAVIGATION_LIMIT": 30,
		}
	)
	method = _load_app_method("_handle_pending_context_menu_focus", namespace)
	item = Node(
		name="any localized label",
		role=role.MENUITEM,
		children=[Node(children=[Node(name="\ue248")])],
	)
	pending = {"icons": "\ue248", "moves": 0}
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		keys={},
		_invoke_context_menu_item=lambda item: None,
		_arm_context_menu_timeout=lambda pending, delay: None,
		_find_context_menu_command=lambda obj, icons: None,
	)

	assert method(instance, item, lambda: None)
	assert instance.execute_context_menu_option is False
	assert scheduled == [(20, instance._invoke_context_menu_item, item)]


def test_context_menu_moves_one_item_at_a_time_until_read_icon_is_focused():
	role = SimpleNamespace(MENUITEM="menuItem", LINK="link", BUTTON="button")
	scheduled = []
	sent = []
	armed = []
	method = _load_app_method(
		"_handle_pending_context_menu_focus",
		{
			"Role": role,
			"_menu_item_has_icon": lambda obj, icons: False,
			"core": SimpleNamespace(callLater=lambda *args: scheduled.append(args)),
			"_CONTEXT_MENU_STEP_DELAY_MS": 20,
			"_CONTEXT_MENU_NAVIGATION_DELAY_MS": 250,
			"_CONTEXT_MENU_NAVIGATION_LIMIT": 30,
			"_CONTEXT_MENU_ACTIVITY_TIMEOUT_MS": 3000,
		},
	)
	pending = {"icons": ("\ue91d", "\ue91c"), "moves": 0}
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		keys={
			"downArrow": SimpleNamespace(send=lambda: sent.append("down")),
			"escape": SimpleNamespace(send=lambda: sent.append("escape")),
		},
		_invoke_context_menu_item=lambda item: None,
		_find_context_menu_command=lambda obj, icons: None,
		_arm_context_menu_timeout=lambda pending, delay: armed.append((pending, delay)),
		_send_pending_context_menu_navigation_key=lambda request: sent.append("down"),
	)

	assert method(instance, Node(role=role.MENUITEM), lambda: None)
	assert pending["moves"] == 1
	assert armed == [(pending, 3000)]
	assert scheduled[0][0] == 250
	scheduled[0][1](*scheduled[0][2:])
	assert sent == ["down"]


def test_context_menu_moves_from_unigrams_reaction_link_to_the_first_command():
	role = SimpleNamespace(MENUITEM="menuItem", LINK="link", BUTTON="button")
	scheduled = []
	sent = []
	armed = []
	method = _load_app_method(
		"_handle_pending_context_menu_focus",
		{
			"Role": role,
			"_menu_item_has_icon": lambda obj, icons: (_ for _ in ()).throw(
				AssertionError("a reaction link is not a menu command")
			),
			"core": SimpleNamespace(callLater=lambda *args: scheduled.append(args)),
			"_CONTEXT_MENU_STEP_DELAY_MS": 20,
			"_CONTEXT_MENU_NAVIGATION_DELAY_MS": 250,
			"_CONTEXT_MENU_NAVIGATION_LIMIT": 30,
			"_CONTEXT_MENU_ACTIVITY_TIMEOUT_MS": 3000,
		},
	)
	pending = {"icons": "\ue248", "moves": 0}
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		keys={
			"downArrow": SimpleNamespace(send=lambda: sent.append("down")),
			"escape": SimpleNamespace(send=lambda: sent.append("escape")),
		},
		_invoke_context_menu_item=lambda item: None,
		_find_context_menu_command=lambda obj, icons: None,
		_arm_context_menu_timeout=lambda pending, delay: armed.append((pending, delay)),
		_send_pending_context_menu_navigation_key=lambda request: sent.append("down"),
	)

	assert method(instance, Node(name="group-specific reaction", role=role.LINK), lambda: None)
	assert method(instance, Node(name="another reaction event", role=role.LINK), lambda: None)
	assert pending["moves"] == 1
	assert armed == [(pending, 3000), (pending, 3000)]
	assert len(scheduled) == 1
	assert scheduled[0][0] == 250
	scheduled[0][1](*scheduled[0][2:])
	assert sent == ["down"]


def test_delayed_context_menu_navigation_is_cancelled_after_raw_invoke():
	sent = []
	method = _load_app_method("_send_pending_context_menu_navigation_key", {})
	pending = {"navigationScheduled": True}
	instance = SimpleNamespace(
		execute_context_menu_option=False,
		keys={"downArrow": SimpleNamespace(send=lambda: sent.append("down"))},
	)

	assert not method(instance, pending)
	assert sent == []

	instance.execute_context_menu_option = pending
	pending["rawInvoked"] = True
	assert not method(instance, pending)
	assert sent == []

	pending["rawInvoked"] = False
	assert method(instance, pending)
	assert pending["navigationScheduled"] is False
	assert sent == ["down"]


def test_raw_context_menu_probe_runs_on_nvdas_mta_thread(monkeypatch):
	jobs = []
	main_queue_calls = []
	monkeypatch.setitem(
		sys.modules,
		"UIAHandler",
		SimpleNamespace(
			handler=SimpleNamespace(
				MTAThreadQueue=SimpleNamespace(put_nowait=jobs.append),
			),
		),
	)
	old_popup = object()
	latest_popup = object()
	pending = {
		"icons": "\ue248",
		"processID": 4242,
		"rawProbeToken": 3,
		"rawProbeAttempts": 0,
		"rawProbeDiagnosed": False,
		"rawInvoked": False,
		"rawProbeObject": latest_popup,
	}
	namespace = {
		"_CONTEXT_MENU_RAW_PROBE_LIMIT": 8,
		"_get_raw_context_menu_focus": lambda process_id: None,
		"_invoke_raw_context_menu_option": lambda root, icons, process_id, diagnose=False, pending=None: (
			root is latest_popup and icons == "\ue248" and process_id == 4242 and diagnose
		),
		"queueHandler": SimpleNamespace(
			eventQueue="eventQueue",
			queueFunction=lambda queue, callback, *args: main_queue_calls.append((queue, callback, args)),
		),
		"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
	}
	method = _load_app_method("_queue_context_menu_raw_probe", namespace)
	completed = []
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		_complete_context_menu_raw_probe=lambda *args: completed.append(args),
	)

	assert method(instance, old_popup, pending, 3)
	assert pending["rawProbeAttempts"] == 1
	assert len(jobs) == 1
	assert not main_queue_calls

	jobs[0]()
	assert pending["rawInvoked"] is True
	assert len(main_queue_calls) == 1
	queue, callback, args = main_queue_calls[0]
	assert queue == "eventQueue"
	callback(*args)
	assert completed == [(latest_popup, pending, 3, True)]


def test_raw_context_menu_probe_tries_latest_popup_after_current_focus_fails(monkeypatch):
	jobs = []
	main_queue_calls = []
	monkeypatch.setitem(
		sys.modules,
		"UIAHandler",
		SimpleNamespace(
			handler=SimpleNamespace(
				MTAThreadQueue=SimpleNamespace(put_nowait=jobs.append),
			),
		),
	)
	current_window = object()
	latest_popup = object()
	pending = {
		"icons": "\ue248",
		"processID": 4242,
		"rawProbeToken": 1,
		"rawProbeAttempts": 0,
		"rawProbeDiagnosed": False,
		"rawInvoked": False,
		"rawProbeObject": latest_popup,
	}
	invocations = []
	def invoke(root, icons, process_id, diagnose=False, pending=None):
		invocations.append((root, diagnose))
		if root is current_window:
			raise RuntimeError("transient provider failure")
		return root is latest_popup

	namespace = {
		"_CONTEXT_MENU_RAW_PROBE_LIMIT": 8,
		"_get_raw_context_menu_focus": lambda process_id: current_window,
		"_invoke_raw_context_menu_option": invoke,
		"queueHandler": SimpleNamespace(
			eventQueue="eventQueue",
			queueFunction=lambda queue, callback, *args: main_queue_calls.append((queue, callback, args)),
		),
		"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
	}
	method = _load_app_method("_queue_context_menu_raw_probe", namespace)
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		_complete_context_menu_raw_probe=lambda *args: None,
	)

	assert method(instance, object(), pending, 1)
	jobs[0]()

	assert invocations == [(current_window, True), (latest_popup, True)]
	assert pending["rawInvoked"] is True
	assert len(main_queue_calls) == 1


def test_raw_context_menu_probe_finds_uia_focus_without_a_popup_event(monkeypatch):
	jobs = []
	main_queue_calls = []
	monkeypatch.setitem(
		sys.modules,
		"UIAHandler",
		SimpleNamespace(
			handler=SimpleNamespace(
				MTAThreadQueue=SimpleNamespace(put_nowait=jobs.append),
			),
		),
	)
	pending = {
		"icons": "\ue248",
		"processID": 4242,
		"rawProbeToken": 1,
		"rawProbeAttempts": 0,
		"rawProbeDiagnosed": False,
		"rawInvoked": False,
	}
	raw_focus = object()
	invocations = []
	namespace = {
		"_CONTEXT_MENU_RAW_PROBE_LIMIT": 64,
		"_get_raw_context_menu_focus": lambda process_id: raw_focus,
		"_invoke_raw_context_menu_option": lambda root, icons, process_id, diagnose=False, pending=None: (
			invocations.append((root, icons, process_id, diagnose)) or True
		),
		"queueHandler": SimpleNamespace(
			eventQueue="eventQueue",
			queueFunction=lambda queue, callback, *args: main_queue_calls.append((queue, callback, args)),
		),
		"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
	}
	method = _load_app_method("_queue_context_menu_raw_probe", namespace)
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		_complete_context_menu_raw_probe=lambda *args: None,
	)

	assert method(instance, None, pending, 1)
	jobs[0]()

	assert invocations == [(raw_focus, "\ue248", 4242, True)]
	assert pending["rawInvoked"] is True
	assert len(main_queue_calls) == 1


def test_first_real_popup_query_keeps_diagnostics_after_empty_focus_polls(monkeypatch):
	jobs = []
	main_queue_calls = []
	monkeypatch.setitem(
		sys.modules,
		"UIAHandler",
		SimpleNamespace(
			handler=SimpleNamespace(
				MTAThreadQueue=SimpleNamespace(put_nowait=jobs.append),
			),
		),
	)
	pending = {
		"icons": "\ue248",
		"processID": 4242,
		"rawProbeToken": 1,
		"rawProbeAttempts": 0,
		"rawProbeDiagnosed": False,
		"rawInvoked": False,
	}
	raw_focus = object()
	focuses = iter((None, raw_focus))
	invocations = []
	namespace = {
		"_CONTEXT_MENU_RAW_PROBE_LIMIT": 64,
		"_get_raw_context_menu_focus": lambda process_id: next(focuses),
		"_invoke_raw_context_menu_option": lambda root, icons, process_id, diagnose=False, pending=None: (
			invocations.append((root, diagnose)) or True
		),
		"queueHandler": SimpleNamespace(
			eventQueue="eventQueue",
			queueFunction=lambda queue, callback, *args: main_queue_calls.append((queue, callback, args)),
		),
		"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
	}
	method = _load_app_method("_queue_context_menu_raw_probe", namespace)
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		_complete_context_menu_raw_probe=lambda *args: None,
	)

	assert method(instance, None, pending, 1)
	jobs[0]()
	assert pending["rawProbeAttempts"] == 1
	assert pending["rawProbeDiagnosed"] is False
	assert invocations == []

	assert method(instance, None, pending, 1)
	jobs[1]()
	assert pending["rawProbeAttempts"] == 2
	assert pending["rawProbeDiagnosed"] is True
	assert invocations == [(raw_focus, True)]


def test_raw_context_menu_focus_is_limited_to_the_target_process_and_popup_controls(monkeypatch):
	class RawFocus:
		def __init__(self):
			self.properties = {"processId": 4242, "controlType": "menuItem"}

		def GetCachedPropertyValueEx(self, property_id, ignore_default):
			assert ignore_default
			return self.properties[property_id]

	focus = RawFocus()
	client = SimpleNamespace(
		GetFocusedElementBuildCache=lambda cache_request: focus,
	)
	monkeypatch.setitem(
		sys.modules,
		"UIAHandler",
		SimpleNamespace(
			handler=SimpleNamespace(
				clientObject=client,
				baseCacheRequest="baseCache",
			),
			UIA=SimpleNamespace(
				UIA_ProcessIdPropertyId="processId",
				UIA_ControlTypePropertyId="controlType",
				UIA_MenuItemControlTypeId="menuItem",
				UIA_MenuControlTypeId="menu",
				UIA_HyperlinkControlTypeId="hyperlink",
				UIA_ButtonControlTypeId="button",
				UIA_WindowControlTypeId="window",
			),
		),
	)
	namespace = _load_module_members(
		{"_raw_uia_property", "_get_raw_context_menu_focus"},
		{},
	)
	get_focus = namespace["_get_raw_context_menu_focus"]

	assert get_focus(4242) is focus
	assert get_focus(7) is None
	assert get_focus("not-a-process-id") is None
	focus.properties["controlType"] = "listItem"
	assert get_focus(4242) is None


def test_failed_raw_context_menu_probe_keeps_its_chain_across_popup_hint_changes():
	scheduled = []
	stale_popup = object()
	latest_popup = object()
	pending = {
		"icons": "\ue248",
		"rawProbeToken": 1,
		"rawProbeAttempts": 1,
		"rawProbeObject": latest_popup,
	}
	method = _load_app_method(
		"_complete_context_menu_raw_probe",
		{
			"core": SimpleNamespace(callLater=lambda *args: scheduled.append(args)),
			"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
			"_CONTEXT_MENU_RAW_RETRY_DELAY_MS": 150,
			"_CONTEXT_MENU_RAW_PROBE_LIMIT": 8,
		},
	)
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		_queue_context_menu_raw_probe=lambda *args: None,
	)

	method(instance, stale_popup, pending, 2, False)
	assert scheduled == []

	method(instance, stale_popup, pending, 1, False)
	assert scheduled == [
		(150, instance._queue_context_menu_raw_probe, latest_popup, pending, 1),
	]

	method(instance, stale_popup, pending, 1, True)
	assert instance.execute_context_menu_option is False


def test_context_menu_timeout_generation_prevents_stale_callbacks_from_closing_the_menu():
	method = _load_app_method("_expire_context_menu_option", {})
	sent = []
	old_pending = {"icons": "old", "moves": 0, "timeoutToken": 1}
	new_pending = {"icons": "new", "moves": 0, "timeoutToken": 2}
	instance = SimpleNamespace(
		execute_context_menu_option=new_pending,
		keys={"escape": SimpleNamespace(send=lambda: sent.append("escape"))},
	)

	method(instance, old_pending, 1)
	assert instance.execute_context_menu_option is new_pending
	assert sent == []

	method(instance, new_pending, 1)
	assert instance.execute_context_menu_option is new_pending
	assert sent == []

	method(instance, new_pending, 2)
	assert instance.execute_context_menu_option is False
	assert sent == ["escape"]


def test_context_menu_timeout_does_not_escape_after_raw_invoke():
	method = _load_app_method("_expire_context_menu_option", {})
	sent = []
	pending = {"timeoutToken": 3, "rawInvoked": True}
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		keys={"escape": SimpleNamespace(send=lambda: sent.append("escape"))},
	)

	method(instance, pending, 3)

	assert instance.execute_context_menu_option is False
	assert sent == []


def _load_context_menu_claim():
	return _load_module_members(
		{"_claim_context_menu_option"},
		{"_CONTEXT_MENU_CLAIM_LOCK": threading.Lock()},
	)["_claim_context_menu_option"]


def test_focused_command_is_left_to_a_raw_invoke_that_claimed_it_first():
	"""Ctrl+Space left selection mode at once in Unigram 13.1.

	The raw probe invoked Select, which closed the flyout. The focus path then
	called doAction on the closed item, got NotImplementedError and sent Escape,
	and Escape ended the selection mode that Select had just started.

	The focus path must also keep the request current while that Invoke runs, so
	the next probe or focus event can still run the command if Invoke fails.
	"""
	role = SimpleNamespace(MENUITEM="menuItem", LINK="link", BUTTON="button")
	scheduled = []
	next_calls = []
	method = _load_app_method(
		"_handle_pending_context_menu_focus",
		{
			"Role": role,
			"_claim_context_menu_option": _load_context_menu_claim(),
			"_menu_item_has_icon": lambda obj, icons: True,
			"core": SimpleNamespace(callLater=lambda *args: scheduled.append(args)),
			"_CONTEXT_MENU_STEP_DELAY_MS": 20,
		},
	)
	item = Node(role=role.MENUITEM)
	pending = {"icons": "\ue97e", "moves": 0}

	def find_command_while_the_raw_probe_claims_it(obj, icons):
		# The raw probe's claim lands while this lookup crosses into Unigram.
		pending["claimed"] = True
		return item

	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		_invoke_context_menu_item=lambda item: None,
		_find_context_menu_command=find_command_while_the_raw_probe_claims_it,
	)

	assert method(instance, item, lambda: next_calls.append(True))
	assert scheduled == []
	assert instance.execute_context_menu_option is pending
	assert next_calls == [True]

	# Invoke raised on the MTA thread and gave the claim back.
	pending["claimed"] = False
	instance._find_context_menu_command = lambda obj, icons: item
	assert method(instance, item, lambda: next_calls.append(True))
	assert scheduled == [(20, instance._invoke_context_menu_item, item)]
	assert instance.execute_context_menu_option is False
	assert pending["claimed"] is True
	assert next_calls == [True]


def test_raw_probe_does_not_invoke_a_command_the_focus_path_claimed(monkeypatch):
	invocations = []
	failures = []

	class InvokePattern:
		def QueryInterface(self, interface):
			assert interface == "invokeInterface"
			return self

		def Invoke(self):
			if failures:
				raise RuntimeError("the popup closed")
			invocations.append(True)

	item = SimpleNamespace(GetCurrentPattern=lambda pattern_id: InvokePattern())
	monkeypatch.setitem(
		sys.modules,
		"UIAHandler",
		SimpleNamespace(UIA_InvokePatternId="invokePattern", IUIAutomationInvokePattern="invokeInterface"),
	)
	invoke = _load_module_members(
		{"_invoke_raw_context_menu_option"},
		{
			"_claim_context_menu_option": _load_context_menu_claim(),
			"_find_raw_context_menu_item_by_icon": lambda root, icons, process_id, diagnose: item,
		},
	)["_invoke_raw_context_menu_option"]

	assert not invoke(object(), "", 4242, pending={"claimed": True})
	assert invocations == []

	pending = {}
	assert invoke(object(), "", 4242, pending=pending)
	assert invocations == [True]
	assert not invoke(object(), "", 4242, pending=pending)
	assert invocations == [True]

	# A failed Invoke releases the request, so a later probe can still run it.
	failures.append(True)
	pending = {}
	try:
		invoke(object(), "", 4242, pending=pending)
	except RuntimeError:
		pass
	assert pending["claimed"] is False


def test_context_menu_focus_after_raw_claim_only_continues_the_event_chain():
	method = _load_app_method("_handle_pending_context_menu_focus", {})
	pending = {"rawInvoked": False, "claimed": True}
	next_calls = []
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		_find_context_menu_command=lambda obj, icons: (_ for _ in ()).throw(
			AssertionError("the raw probe already runs this command")
		),
	)

	assert method(instance, object(), lambda: next_calls.append(True))
	assert instance.execute_context_menu_option is pending
	assert next_calls == [True]


def test_context_menu_timeout_arming_invalidates_the_previous_timer():
	scheduled = []
	method = _load_app_method(
		"_arm_context_menu_timeout",
		{"core": SimpleNamespace(callLater=lambda *args: scheduled.append(args))},
	)
	pending = {"icons": "reply", "moves": 0, "timeoutToken": 0}
	instance = SimpleNamespace(_expire_context_menu_option=lambda pending, token: None)

	method(instance, pending, 10000)
	method(instance, pending, 3000)

	assert pending["timeoutToken"] == 2
	assert scheduled == [
		(10000, instance._expire_context_menu_option, pending, 1),
		(3000, instance._expire_context_menu_option, pending, 2),
	]


def test_enter_invokes_reply_directly_like_version_54():
	"""Enter must not arrow towards Reply once the flyout realized its commands.

	Up to 5.4 the add-on scanned the realized flyout and invoked the command at
	once. Arrowing towards it instead makes Enter appear not to work while every
	intermediate item is announced.
	"""
	role = SimpleNamespace(MENUITEM="menuItem", LINK="link", BUTTON="button")
	scheduled = []
	namespace = _load_module_members(
		{"_walk_bounded_descendants", "_menu_item_has_icon"},
		{"Role": role},
	)
	namespace.update(
		{
			"_claim_context_menu_option": _load_context_menu_claim(),
			"core": SimpleNamespace(callLater=lambda *args: scheduled.append(args)),
			"_CONTEXT_MENU_STEP_DELAY_MS": 20,
			"_CONTEXT_MENU_NAVIGATION_DELAY_MS": 250,
			"_CONTEXT_MENU_NAVIGATION_LIMIT": 30,
			"_CONTEXT_MENU_ACTIVITY_TIMEOUT_MS": 3000,
		}
	)
	find_command = _load_app_method("_find_context_menu_command", namespace)
	method = _load_app_method("_handle_pending_context_menu_focus", namespace)

	reply = Node(name="Reply", role=role.MENUITEM, children=[Node(name="")])
	flyout = Node(
		role=role.MENUITEM,
		children=[
			Node(name="Copy", role=role.MENUITEM, children=[Node(name="")]),
			reply,
			Node(name="Delete", role=role.MENUITEM, children=[Node(name="")]),
		],
	)
	focused = flyout.children[0]
	pending = {"icons": ("",), "moves": 0}
	sent = []
	instance = SimpleNamespace(
		execute_context_menu_option=pending,
		keys={"downArrow": SimpleNamespace(send=lambda: sent.append("down"))},
		_invoke_context_menu_item=lambda item: None,
		_arm_context_menu_timeout=lambda pending, delay: None,
	)
	instance._find_context_menu_command = lambda obj, icons: find_command(instance, obj, icons)

	assert method(instance, focused, lambda: None)

	assert instance.execute_context_menu_option is False
	assert scheduled == [(20, instance._invoke_context_menu_item, reply)]
	assert sent == [], "Reply must be invoked directly, not reached with arrow keys"


def test_a_reaction_link_still_falls_back_when_no_command_is_realized_yet():
	role = SimpleNamespace(MENUITEM="menuItem", LINK="link", BUTTON="button")
	namespace = _load_module_members(
		{"_walk_bounded_descendants", "_menu_item_has_icon"},
		{"Role": role},
	)
	find_command = _load_app_method("_find_context_menu_command", namespace)
	reactions = Node(children=[Node(name="thumbs up", role=role.LINK)])

	assert find_command(SimpleNamespace(), reactions.children[0], ("",)) is None
