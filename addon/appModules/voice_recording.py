"""State transitions for Unigram's native voice/video recording UI."""


RECORDING_BUTTON_AUTOMATION_ID = "btnVoiceMessage"
ELAPSED_LABEL_AUTOMATION_ID = "ElapsedLabel"
VOICE_MESSAGE_AUTOMATION_ID = "Recognize"
VIDEO_MESSAGE_AUTOMATION_IDS = frozenset(("Player", "Subtitle"))
EMPTY_MESSAGE_MARKER = ("empty",)


def _is_zero_elapsed_label(value):
	digits = "".join(character for character in str(value or "") if character.isdigit())
	return bool(digits) and not any(character != "0" for character in digits)


def is_recording_button(obj):
	try:
		return obj.UIAAutomationId == RECORDING_BUTTON_AUTOMATION_ID
	except Exception:
		return False


def recording_button_state(button):
	"""Return True while UnigramPlus can see the button's elapsed-time sibling.

	The same relationship is used when UnigramPlus labels the focused record
	button as "Recording ..., elapsed time". None means that the cached button
	is no longer readable and must be rediscovered.
	"""
	if not is_recording_button(button):
		return None
	try:
		next_element = button.next
	except Exception:
		return None
	try:
		return bool(next_element and next_element.UIAAutomationId == ELAPSED_LABEL_AUTOMATION_ID)
	except Exception:
		return None


def message_marker(obj):
	"""Build a stable marker for the last item in Unigram's message list."""
	if obj is None:
		return EMPTY_MESSAGE_MARKER
	try:
		position = obj.positionInfo
		index = position.get("indexInGroup")
		total = position.get("similarItemsInGroup")
		if index is not None or total is not None:
			# Unigram virtualizes the message list and can reuse the last item's
			# index while appending an outgoing message. The total still changes,
			# so both values are needed to distinguish the replacement.
			return ("position", index, total)
	except Exception:
		pass
	try:
		return ("runtime", tuple(obj.UIAElement.GetRuntimeId()))
	except Exception:
		return ("object", id(obj))


def is_recorded_message(obj, video=False, max_elements=64):
	"""Identify a voice/video message by controls fixed in Unigram's templates."""
	if obj is None:
		return False
	stack = [obj]
	automation_ids = set()
	for _ in range(max_elements):
		if not stack:
			break
		current = stack.pop()
		try:
			automation_id = current.UIAAutomationId
			automation_ids.add(automation_id)
		except Exception:
			automation_id = ""
		if not video and VOICE_MESSAGE_AUTOMATION_ID in automation_ids:
			return True
		if not video and automation_id == "Subtitle":
			try:
				subtitle = current.name or ""
				if len(subtitle) < 15 and " / " in subtitle:
					return True
			except Exception:
				pass
		try:
			stack.extend(reversed(current.children or ()))
		except Exception:
			continue
	return VIDEO_MESSAGE_AUTOMATION_IDS.issubset(automation_ids) if video else False


class VoiceRecordingOutcome:
	"""Tell when a stopped recording has been sent, without observing keys.

	A recording that produces no new message before the window closes simply
	stops being watched. Unigram 13.0 announces a canceled recording itself.
	"""

	_UNRECOGNIZED_MESSAGE_POLLS = 2

	def __init__(self, poll_limit=8):
		self.poll_limit = poll_limit
		self.pending = False
		self.baseline = None
		self.video = False
		self._pollsRemaining = 0
		self._changedMessagePolls = 0

	def started(self, baseline, video=False):
		self.pending = False
		self.baseline = baseline
		self.video = video
		self._pollsRemaining = 0
		self._changedMessagePolls = 0

	def stopped(self):
		self.pending = True
		self._pollsRemaining = self.poll_limit
		self._changedMessagePolls = 0

	def observe(self, marker, is_recorded):
		if not self.pending:
			return None
		marker_changed = self.baseline is not None and marker is not None and marker != self.baseline
		if marker_changed:
			if is_recorded:
				return self._finish("sent")
			# During encoding/upload Unigram can append the outgoing item before
			# its Recognize/Subtitle controls enter the UIA tree. A persistent new
			# last item is therefore sufficient evidence of sending; requiring the
			# finished voice-note template missed sends.
			self._changedMessagePolls += 1
			if self._changedMessagePolls >= self._UNRECOGNIZED_MESSAGE_POLLS:
				return self._finish("sent")
		else:
			self._changedMessagePolls = 0
		self._pollsRemaining -= 1
		if self._pollsRemaining <= 0:
			return self._finish(None)
		return None

	def _finish(self, transition):
		self.pending = False
		self._pollsRemaining = 0
		self._changedMessagePolls = 0
		return transition


class VoiceRecordingState:
	"""Convert native recording UI visibility into stable transitions."""

	def __init__(self):
		self.active = False
		self._seenProgress = False

	def shown(self):
		if self.active:
			return None
		self.active = True
		self._seenProgress = False
		return "start"

	def elapsedChanged(self, value):
		if not self.active:
			# Unigram resets the label after collapsing ChatRecord. That terminal
			# zero must not be mistaken for a new recording.
			if _is_zero_elapsed_label(value):
				return None
			self.active = True
			self._seenProgress = True
			return "start"
		if _is_zero_elapsed_label(value):
			# Unigram can emit the initial zero value just after showing the bar.
			# It is an end transition only after the timer has actually advanced.
			return self._finish() if self._seenProgress else None
		self._seenProgress = True
		return None

	def hidden(self):
		if not self.active:
			return None
		self.active = False
		self._seenProgress = False
		return "stopped"

	def visibilityChanged(self, visible):
		return self.shown() if visible else self.hidden()

	def _finish(self):
		self.active = False
		self._seenProgress = False
		return "stopped"
