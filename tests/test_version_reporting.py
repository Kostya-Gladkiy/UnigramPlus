import ast
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"


def _version_script_node():
	module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
	app_module = next(
		node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule"
	)
	return next(
		node
		for node in app_module.body
		if isinstance(node, ast.FunctionDef) and node.name == "script_announceVersions"
	)


def _load_version_script(addon_handler, text_windows):
	method = _version_script_node()
	method.decorator_list = []
	namespace = {
		"addonHandler": addon_handler,
		"TextWindow": lambda *args, **kwargs: text_windows.append((args, kwargs)),
		"_": lambda text: text,
	}
	exec(compile(ast.Module(body=[method], type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace["script_announceVersions"]


def test_nvda_alt_v_opens_both_installed_versions_in_a_read_only_window():
	text_windows = []
	addon_handler = SimpleNamespace(
		getCodeAddon=lambda: SimpleNamespace(manifest={"version": "5.6.7"}),
	)
	script = _load_version_script(addon_handler, text_windows)

	script(SimpleNamespace(app_version="12.9.1.0"), None)

	assert text_windows == [
		(
			("Unigram version: 12.9.1.0.\nUnigramPlus version: 5.6.7.", "UnigramPlus"),
			{"readOnly": True},
		)
	]


def test_version_window_uses_nvda_product_version_and_handles_missing_metadata():
	text_windows = []
	addon_handler = SimpleNamespace(getCodeAddon=lambda: (_ for _ in ()).throw(RuntimeError()))
	script = _load_version_script(addon_handler, text_windows)

	script(SimpleNamespace(app_version=" ", productVersion="12.9.1"), None)

	assert text_windows == [
		(
			("Unigram version: 12.9.1.\nUnigramPlus version: -.", "UnigramPlus"),
			{"readOnly": True},
		)
	]


def test_version_script_has_the_requested_gesture_and_input_help_description():
	method = _version_script_node()
	decorator = next(
		decorator
		for decorator in method.decorator_list
		if isinstance(decorator, ast.Call)
		and isinstance(decorator.func, ast.Name)
		and decorator.func.id == "script"
	)
	keywords = {keyword.arg: keyword.value for keyword in decorator.keywords}

	assert keywords["gesture"].value == "kb:NVDA+alt+V"
	assert "read-only window" in ast.unparse(keywords["description"])
