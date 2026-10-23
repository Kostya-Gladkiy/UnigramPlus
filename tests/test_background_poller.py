import ast
import threading
import time
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "addon" / "appModules" / "unigram.py"


def _load_poller():
	module = ast.parse(SOURCE_PATH.read_text(encoding="utf-8"))
	node = next(
		item
		for item in module.body
		if isinstance(item, ast.ClassDef) and item.name == "_BackgroundPoller"
	)
	namespace = {
		"threading": threading,
		"time": time,
		"log": SimpleNamespace(debug=lambda *args, **kwargs: None),
	}
	exec(compile(ast.Module(body=[node], type_ignores=[]), str(SOURCE_PATH), "exec"), namespace)
	return namespace["_BackgroundPoller"]


def test_poller_repeats_a_job_without_a_thread_per_sample():
	poller = _load_poller()
	fired = []
	done = threading.Event()

	def sample():
		fired.append(time.monotonic())
		if len(fired) < 3:
			poller.schedule("job", 0.02, sample)
		else:
			done.set()

	poller.schedule("job", 0.02, sample)

	assert done.wait(5)
	assert len(fired) == 3
	workers = [thread for thread in threading.enumerate() if thread.name == "UnigramPlusPoller"]
	assert len(workers) <= 1


def test_canceling_a_job_stops_it_from_running():
	poller = _load_poller()
	ran = []

	poller.schedule("job", 0.2, lambda: ran.append(True))
	poller.cancel("job")
	time.sleep(0.4)

	assert ran == []


def test_a_failing_sample_does_not_kill_the_worker():
	poller = _load_poller()
	survived = threading.Event()

	def boom():
		raise RuntimeError("a UIA provider can fail at any time")

	poller.schedule("boom", 0.01, boom)
	poller.schedule("after", 0.1, survived.set)

	assert survived.wait(5)
