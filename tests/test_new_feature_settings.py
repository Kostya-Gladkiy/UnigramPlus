"""Every behavior added after 5.4 must be selectable from UnigramPlus settings.

Each of these settings defaults to the current behavior, so an upgrade changes
nothing, and turning one off restores what the add-on did in 5.4.
"""

import ast
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP_MODULE = ROOT / "addon" / "appModules" / "unigram.py"
CONFIG = ROOT / "addon" / "appModules" / "cnf.py"
SETTINGS_PANEL = ROOT / "addon" / "GlobalPlugins" / "UnigramPlus" / "__init__.py"

# setting name -> default it must ship with
NEW_FEATURE_SETTINGS = {
	"voiceRecordingButtonLabel": "withElapsedTime",
	"richMessageSupport": "True",
	"labelProfileIdentityButton": "True",
	"announceComposerState": "True",
	"suppressMessagesListAnnouncement": "True",
	"announceCallControlState": "True",
	"announceFolderUnreadCount": "True",
}


def _config_spec():
	tree = ast.parse(CONFIG.read_text(encoding="utf-8"))
	assignment = next(
		node
		for node in tree.body
		if isinstance(node, ast.Assign)
		and any(getattr(target, "id", "") == "spec" for target in node.targets)
	)
	return [item.value for item in assignment.value.elts if isinstance(item, ast.Constant)]


def test_every_new_setting_has_a_default_that_keeps_todays_behavior():
	spec = " ".join(_config_spec())
	for name, default in NEW_FEATURE_SETTINGS.items():
		match = re.search(r"%s = \w+\(default=([^),]+)" % re.escape(name), spec)
		assert match, "%s is missing from the config spec" % name
		assert match.group(1) == default, name


def test_every_new_setting_actually_gates_its_feature():
	source = APP_MODULE.read_text(encoding="utf-8")
	for name in NEW_FEATURE_SETTINGS:
		assert 'conf.get("%s")' % name in source, "%s is never read by the app module" % name


def test_every_new_setting_is_shown_and_saved_in_the_settings_panel():
	source = SETTINGS_PANEL.read_text(encoding="utf-8-sig")
	for name in NEW_FEATURE_SETTINGS:
		assert 'conf.get("%s")' % name in source, "%s has no control in settings" % name
		assert 'conf.set("%s"' % name in source, "%s is never saved" % name


def test_the_record_button_setting_offers_the_pre_55_behavior():
	source = SETTINGS_PANEL.read_text(encoding="utf-8-sig")
	tree = ast.parse(source)
	panel = next(
		node
		for node in tree.body
		if isinstance(node, ast.ClassDef) and node.name == "UnigramPlusSettings"
	)
	choices = next(
		node
		for node in panel.body
		if isinstance(node, ast.Assign)
		and any(getattr(target, "id", "") == "listVoiceRecordingButtonLabel" for target in node.targets)
	)
	keys = {key.value for key in choices.value.keys}
	assert keys == {"withElapsedTime", "labelOnly", "none"}
