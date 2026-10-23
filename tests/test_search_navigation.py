import ast
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"


def _module_ast():
	return ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))


def _load_search_script(messages, queued):
	module = _module_ast()
	parse_counter = next(
		node
		for node in module.body
		if isinstance(node, ast.FunctionDef) and node.name == "_parse_search_result_counter"
	)
	app_module = next(
		node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule"
	)
	method = next(
		node
		for node in app_module.body
		if isinstance(node, ast.FunctionDef) and node.name == "script_go_to_list_search_results"
	)
	method.decorator_list = []
	namespace = {
		"Role": SimpleNamespace(
			EDITABLETEXT="editableText",
			BUTTON="button",
			STATICTEXT="staticText",
		),
		"_SEARCH_RESULT_COUNTER_RE": __import__("re").compile(r"^\s*(\d+)\s*/\s*(\d+)\s*$"),
		"_SEARCH_RESULT_COUNTER_SIBLING_LIMIT": 6,
		"message": messages.append,
		"_": lambda text: text,
		"queueHandler": SimpleNamespace(
			eventQueue=object(),
			queueFunction=lambda queue, callback: queued.append((queue, callback)),
		),
	}
	exec(
		compile(
			ast.Module(body=[parse_counter, method], type_ignores=[]),
			str(SOURCE_PATH),
			"exec",
		),
		namespace,
	)
	return namespace["script_go_to_list_search_results"]


def _link(*items):
	for index, item in enumerate(items):
		item.next = items[index + 1] if index + 1 < len(items) else None
	return items


def _field(focused, width=300, set_focus=None, role="editableText", controller_for=None):
	return SimpleNamespace(
		role=role,
		UIAAutomationId="Field",
		name="query",
		value="query",
		location=SimpleNamespace(width=width, height=32),
		setFocus=set_focus or (lambda: focused.append(True)),
		controllerFor=controller_for or [],
	)


def _counter(role, name, invoked):
	return SimpleNamespace(
		role=role,
		UIAAutomationId="",
		name=name,
		value="",
		location=SimpleNamespace(width=60, height=24),
		doAction=lambda: invoked.append(True),
	)


def _run(elements):
	messages = []
	queued = []
	sent = []
	method = _load_search_script(messages, queued)
	instance = SimpleNamespace(
		getElements=lambda: elements,
		keys={"downArrow": SimpleNamespace(send=lambda: sent.append(True))},
	)
	result = method(instance, None)
	return result, messages, queued, sent


def test_alt_i_invokes_the_legacy_search_results_button():
	focused = []
	invoked = []
	field, button = _link(
		_field(focused),
		_counter("button", "1 / 5", invoked),
	)

	result, messages, queued, sent = _run([field, button])

	assert result is True
	assert invoked == [True]
	assert focused == []
	assert queued == []
	assert sent == []
	assert messages == []


def test_alt_i_enters_the_current_inline_results_list():
	focused = []
	invoked = []
	field, counter = _link(
		_field(focused),
		_counter("staticText", "2/8", invoked),
	)

	result, messages, queued, sent = _run([field, counter])

	assert result is True
	assert focused == [True]
	assert len(queued) == 1
	queued[0][1]()
	assert sent == [True]
	assert invoked == []
	assert messages == []


def test_alt_i_uses_the_search_fields_controller_for_relation():
	focused = []
	results_list = SimpleNamespace(
		role="list",
		UIAAutomationId="ListAutocomplete",
		name="",
		location=SimpleNamespace(width=400, height=300),
	)
	field = _field(focused, role="unknown", controller_for=[results_list])
	field.next = None

	result, messages, queued, sent = _run([field])

	assert result is True
	assert focused == [True]
	assert len(queued) == 1
	queued[0][1]()
	assert sent == [True]
	assert messages == []


def test_alt_i_tolerates_a_bounded_peer_between_field_and_counter():
	focused = []
	invoked = []
	field, peer, counter = _link(
		_field(focused),
		SimpleNamespace(role="pane", UIAAutomationId="Autocomplete", name="", value=""),
		_counter("staticText", "1 / 3", invoked),
	)

	result, _messages, queued, _sent = _run([field, peer, counter])

	assert result is True
	assert focused == [True]
	assert len(queued) == 1


def test_alt_i_reports_an_empty_result_set_without_sending_down():
	focused = []
	invoked = []
	field, counter = _link(
		_field(focused),
		_counter("staticText", "0 / 0", invoked),
	)

	result, messages, queued, sent = _run([field, counter])

	assert result is False
	assert messages == ["No search results"]
	assert focused == []
	assert queued == []
	assert sent == []


def test_alt_i_ignores_unrelated_slash_text_and_reports_missing_control():
	focused = []
	field = _field(focused)
	peers = [
		SimpleNamespace(role="staticText", UIAAutomationId="", name=f"peer {index}", value="")
		for index in range(6)
	]
	_link(field, *peers)
	unrelated = SimpleNamespace(
		role="staticText",
		UIAAutomationId="Message",
		name="12 / 31",
		value="",
		location=SimpleNamespace(width=100, height=20),
		next=None,
	)

	result, messages, queued, sent = _run([field, *peers, unrelated])

	assert result is False
	assert messages == ["No search results"]
	assert focused == []
	assert queued == []
	assert sent == []


def test_alt_i_skips_hidden_and_stale_fields_before_a_live_search_field():
	focused = []
	invoked = []
	hidden, hidden_counter = _link(
		_field(focused, width=0),
		_counter("staticText", "1 / 9", invoked),
	)
	stale, stale_counter = _link(
		_field(
			focused,
			set_focus=lambda: (_ for _ in ()).throw(RuntimeError("stale field")),
		),
		_counter("staticText", "1 / 7", invoked),
	)
	live, live_counter = _link(
		_field(focused),
		_counter("staticText", "1 / 5", invoked),
	)

	result, messages, queued, _sent = _run([hidden, hidden_counter, stale, stale_counter, live, live_counter])

	assert result is True
	assert focused == [True]
	assert len(queued) == 1
	assert messages == []


def test_alt_i_remains_bound_to_the_search_results_script():
	module = _module_ast()
	app_module = next(
		node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "AppModule"
	)
	method = next(
		node
		for node in app_module.body
		if isinstance(node, ast.FunctionDef) and node.name == "script_go_to_list_search_results"
	)

	assert any(
		isinstance(keyword.value, ast.Constant)
		and keyword.arg == "gesture"
		and keyword.value.value.casefold() == "kb:alt+i"
		for decorator in method.decorator_list
		for keyword in decorator.keywords
	)
