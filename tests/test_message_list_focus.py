import ast
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"


def _focus_namespace(suppress=True):
	return {
		"Role": SimpleNamespace(LIST="list"),
		"conf": SimpleNamespace(get=lambda key: suppress),
	}


def _load_app_method(name, namespace):
	module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
	app_module = next(
		node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule"
	)
	method = next(
		node
		for node in app_module.body
		if isinstance(node, ast.FunctionDef) and node.name == name
	)
	method.decorator_list = []
	exec(compile(ast.Module(body=[method], type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace[name]


def test_messages_list_focus_ancestor_is_suppressed_before_nvda_can_announce_it():
	forwarded = []
	method = _load_app_method("event_focusEntered", _focus_namespace())
	instance = SimpleNamespace(isUnigramWindow=True)
	messages = SimpleNamespace(role="list", UIAAutomationId="Messages")

	method(instance, messages, lambda: forwarded.append(messages))

	assert forwarded == []


def test_other_list_ancestors_keep_their_standard_nvda_announcements():
	forwarded = []
	method = _load_app_method("event_focusEntered", _focus_namespace())
	instance = SimpleNamespace(isUnigramWindow=True)
	chat_list = SimpleNamespace(role="list", UIAAutomationId="ChatsList")

	method(instance, chat_list, lambda: forwarded.append(chat_list))

	assert forwarded == [chat_list]


def test_non_unigram_windows_continue_to_delegate_focus_entered_events_to_the_fallback():
	delegated = []
	method = _load_app_method("event_focusEntered", _focus_namespace())
	fallback = SimpleNamespace(
		event_focusEntered=lambda obj, next_handler: delegated.append((obj, next_handler))
	)
	instance = SimpleNamespace(isUnigramWindow=False, _fallbackAppModule=fallback)
	obj = SimpleNamespace(role="list", UIAAutomationId="Messages")
	next_handler = lambda: None

	method(instance, obj, next_handler)

	assert delegated == [(obj, next_handler)]


def test_the_messages_list_announcement_can_be_restored_from_settings():
	# Turning the setting off gives NVDA's standard behavior back.
	forwarded = []
	method = _load_app_method("event_focusEntered", _focus_namespace(suppress=False))
	instance = SimpleNamespace(isUnigramWindow=True)
	messages = SimpleNamespace(role="list", UIAAutomationId="Messages")

	method(instance, messages, lambda: forwarded.append(messages))

	assert forwarded == [messages]
