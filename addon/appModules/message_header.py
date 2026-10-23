def _normalize_newlines(value):
	return value.replace("\r\n", "\n").replace("\r", "\n")


def _original_index_for_normalized_index(value, normalized_index):
	"""Map an LF-normalized string index back to the original string."""
	original_index = 0
	seen = 0
	while seen < normalized_index and original_index < len(value):
		if value.startswith("\r\n", original_index):
			original_index += 2
		else:
			original_index += 1
		seen += 1
	return original_index


def move_message_header_after_content(name, content_anchor):
	"""Move the newline-delimited message header after the message content.

	``content_anchor`` must come from the message's actual UIA content control.
	This prevents multiline message text from being mistaken for a header.
	"""
	if not name or not content_anchor:
		return name
	normalized_content_index = _normalize_newlines(name).rfind(_normalize_newlines(content_anchor))
	if normalized_content_index <= 0:
		return name
	content_index = _original_index_for_normalized_index(name, normalized_content_index)
	if name[:content_index].endswith("\r\n"):
		separator = "\r\n"
	elif name[:content_index].endswith("\n"):
		separator = "\n"
	elif name[:content_index].endswith("\r"):
		separator = "\r"
	else:
		return name
	separator_start = content_index - len(separator)
	header = name[:separator_start]
	content = name[content_index:]
	if not header.strip() or not content.strip():
		return name
	return content + separator + header


def move_profile_header_after_content(name, content_anchor=""):
	"""Move a confirmed profile-media sender prefix after its content summary."""
	if not name:
		return name
	if content_anchor:
		content_index = name.rfind(content_anchor)
	else:
		separator_index = name.find(": ")
		content_index = separator_index + 2 if separator_index >= 0 else -1
	if content_index <= 0 or content_index >= len(name):
		return name
	header = name[:content_index].strip().rstrip(":").rstrip()
	content = name[content_index:].strip()
	if not header or not content:
		return name
	separator = " " if content[-1] in ".?!,:;" else ", "
	return content + separator + header
