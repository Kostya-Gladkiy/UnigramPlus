"""NVDA 2026.3: no deprecated NVDA API on the add-on's paths.

NVDA 2026.3 removes nothing the add-on uses, but three of its calls go through
deprecation shims: gui.messageBox (deprecated in 2025.1 and warned about with
warnings.warn), gui.mainFrame._popupSettingsDialog and winUser.KEYEVENTF_KEYUP
(moved to winBindings.user32 in 2026.1). The last two log a warning with a
stack trace on every use, and deprecated names may go in a later release.
"""

import ast
import sys
import types
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_PATH = ROOT / "addon" / "GlobalPlugins" / "UnigramPlus" / "__init__.py"
APP_MODULE_PATH = ROOT / "addon" / "appModules" / "unigram.py"

# The real wx values, so composing them is checked rather than assumed.
WX_OK = 4
WX_ICON_WARNING = 256
WX_ICON_INFORMATION = 2048


def _plugin_module():
	return ast.parse(PLUGIN_PATH.read_text(encoding="utf-8-sig"))


def _load_plugin_functions(names, namespace):
	"""Execute the named module-level functions without importing NVDA."""
	members = [
		node for node in _plugin_module().body if isinstance(node, ast.FunctionDef) and node.name in names
	]
	assert {node.name for node in members} == set(names)
	exec(compile(ast.Module(body=members, type_ignores=[]), str(PLUGIN_PATH), "exec"), namespace)
	return namespace


def _namespace(message_box_calls):
	# `gui` here is the module global the fallback calls; the `gui` entry in
	# sys.modules separately decides whether `from gui.message import ...` resolves.
	return {
		"gui": SimpleNamespace(messageBox=lambda *args: message_box_calls.append(args)),
		"wx": SimpleNamespace(OK=WX_OK, ICON_INFORMATION=WX_ICON_INFORMATION, ICON_WARNING=WX_ICON_WARNING),
		"_": lambda text: text,
	}


DIALOG_TYPE = SimpleNamespace(STANDARD="standard", WARNING="warning")


def _install_modern_gui(monkeypatch, shown, show_modal=None):
	"""Stub NVDA 2025.1+ gui.message and gui.guiHelper, recording each dialog shown."""
	main_thread_calls = []

	class MessageDialog:
		def __init__(self, parent, message, title, dialogType=DIALOG_TYPE.STANDARD, **kwargs):
			self.args = (parent, message, title, dialogType, kwargs)

		def ShowModal(self):
			if show_modal:
				show_modal()
			shown.append(self.args)

	def wx_call_on_main(function):
		main_thread_calls.append(function)
		return function()

	monkeypatch.setitem(sys.modules, "gui", types.ModuleType("gui"))
	message_module = types.ModuleType("gui.message")
	message_module.MessageDialog = MessageDialog
	message_module.DialogType = DIALOG_TYPE
	monkeypatch.setitem(sys.modules, "gui.message", message_module)
	gui_helper = types.ModuleType("gui.guiHelper")
	gui_helper.wxCallOnMain = wx_call_on_main
	monkeypatch.setitem(sys.modules, "gui.guiHelper", gui_helper)
	return main_thread_calls


def _install_legacy_gui(monkeypatch):
	# NVDA before 2025.1 has a gui.message module without MessageDialog.
	monkeypatch.setitem(sys.modules, "gui", types.ModuleType("gui"))
	monkeypatch.setitem(sys.modules, "gui.message", types.ModuleType("gui.message"))


def test_alert_dialog_uses_message_dialog_on_current_nvda(monkeypatch):
	shown = []
	message_box_calls = []
	main_thread_calls = _install_modern_gui(monkeypatch, shown)
	namespace = _load_plugin_functions({"_alert_dialog", "no_updates_dialog"}, _namespace(message_box_calls))

	namespace["no_updates_dialog"]()

	assert shown == [(None, "No updates available", "UnigramPlus update", DIALOG_TYPE.STANDARD, {})]
	# Like MessageDialog.alert, the dialog is built on NVDA's main thread.
	assert len(main_thread_calls) == 1
	# The deprecated call must not also run, or the user sees two dialogs.
	assert message_box_calls == []


def test_alert_dialog_keeps_the_warning_style_on_current_nvda(monkeypatch):
	"""MessageDialog.alert has no dialog type, so a warning must not go through it."""
	shown = []
	_install_modern_gui(monkeypatch, shown)
	namespace = _load_plugin_functions({"_alert_dialog"}, _namespace([]))

	namespace["_alert_dialog"]("Incompatible", "UnigramPlus update", WX_ICON_WARNING)

	assert shown == [(None, "Incompatible", "UnigramPlus update", DIALOG_TYPE.WARNING, {})]


def test_alert_dialog_falls_back_to_message_box_on_older_nvda(monkeypatch):
	message_box_calls = []
	_install_legacy_gui(monkeypatch)
	namespace = _load_plugin_functions({"_alert_dialog", "no_updates_dialog"}, _namespace(message_box_calls))

	namespace["no_updates_dialog"]()
	namespace["_alert_dialog"]("Incompatible", "UnigramPlus update", WX_ICON_WARNING)

	assert message_box_calls == [
		("No updates available", "UnigramPlus update", WX_OK | WX_ICON_INFORMATION),
		("Incompatible", "UnigramPlus update", WX_OK | WX_ICON_WARNING),
	]


def test_alert_dialog_does_not_retry_a_failing_message_dialog(monkeypatch):
	"""Only a missing MessageDialog may select the fallback."""
	message_box_calls = []

	def fail():
		raise RuntimeError("wx failed")

	_install_modern_gui(monkeypatch, [], show_modal=fail)
	namespace = _load_plugin_functions({"_alert_dialog"}, _namespace(message_box_calls))

	try:
		namespace["_alert_dialog"]("Body", "Title")
	except RuntimeError:
		pass
	else:
		raise AssertionError("a failing MessageDialog.alert should not be swallowed")
	assert message_box_calls == []


def _called_names(node):
	"""Every dotted call target inside an AST subtree, e.g. "gui.messageBox"."""
	names = set()
	for child in ast.walk(node):
		if not isinstance(child, ast.Call):
			continue
		func = child.func
		if isinstance(func, ast.Name):
			names.add(func.id)
		elif isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
			names.add("%s.%s" % (func.value.id, func.attr))
	return names


def test_the_message_box_only_survives_inside_the_fallback():
	holders = [
		node.name
		for node in ast.walk(_plugin_module())
		if isinstance(node, ast.FunctionDef) and "gui.messageBox" in _called_names(node)
	]

	assert holders == ["_alert_dialog"]


def test_the_incompatible_update_warning_keeps_its_warning_icon():
	setup_update = next(
		node
		for node in ast.walk(_plugin_module())
		if isinstance(node, ast.FunctionDef) and node.name == "setup_update"
	)
	call = next(
		node
		for node in ast.walk(setup_update)
		if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "_alert_dialog"
	)

	assert ast.unparse(call.args[-1]) == "wx.ICON_WARNING"


def test_settings_dialog_prefers_the_public_popup_api():
	source = PLUGIN_PATH.read_text(encoding="utf-8-sig")

	assert 'getattr(gui.mainFrame, "popupSettingsDialog", None)' in source
	assert "wx.CallAfter(popup," in source
	assert "wx.CallAfter(gui.mainFrame._popupSettingsDialog" not in source


def test_voice_seeking_releases_modifiers_without_the_moved_win_user_constant():
	source = APP_MODULE_PATH.read_text(encoding="utf-8")
	module = ast.parse(source)
	constant = next(
		node
		for node in module.body
		if isinstance(node, ast.Assign)
		and any(isinstance(target, ast.Name) and target.id == "_KEYEVENTF_KEYUP" for target in node.targets)
	)

	# KEYEVENTF_KEYUP in WinUser.h.
	assert ast.literal_eval(constant.value) == 2
	moved_reads = [
		node
		for node in ast.walk(module)
		if isinstance(node, ast.Attribute)
		and node.attr == "KEYEVENTF_KEYUP"
		and isinstance(node.value, ast.Name)
		and node.value.id == "winUser"
	]
	assert moved_reads == []
