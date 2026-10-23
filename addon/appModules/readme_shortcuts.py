# -*- coding: utf-8 -*-
import re


SHORTCUT_TABLE_START = "<!-- shortcut-table-start -->"
SHORTCUT_TABLE_END = "<!-- shortcut-table-end -->"


def _cleanMarkdownCell(value):
	return value.strip().replace("**", "").replace("`", "").replace("\\|", "|")


def _extractMarkedShortcutTables(markdown):
	start = markdown.find(SHORTCUT_TABLE_START)
	if start < 0:
		return ""
	end = markdown.find(SHORTCUT_TABLE_END, start)
	if end < 0:
		return ""

	result = []
	lines = markdown[start + len(SHORTCUT_TABLE_START) : end].splitlines()
	for index, rawLine in enumerate(lines):
		line = rawLine.strip()
		if line.startswith("### "):
			if result:
				result.append("")
			result.append(line[4:].strip())
		elif line.startswith("|") and line.endswith("|"):
			cells = [_cleanMarkdownCell(cell) for cell in re.split(r"(?<!\\)\|", line[1:-1])]
			nextLine = lines[index + 1].strip() if index + 1 < len(lines) else ""
			if (
				len(cells) != 3
				or all(set(cell) <= {"-", ":"} for cell in cells)
				or nextLine.startswith("|---")
			):
				continue
			result.append(" - ".join(cells))
	return "\n".join(result).strip()


def _extractLegacyShortcutList(markdown):
	blocks = markdown.split("\n\n")
	if not blocks:
		return ""
	text = max(blocks, key=lambda block: len(block.splitlines()))
	return text.replace("* ", "").replace("## ", "").strip()


def extractShortcutText(markdown):
	"""Return readable plain text from the marked shortcut tables in a README."""
	return _extractMarkedShortcutTables(markdown) or _extractLegacyShortcutList(markdown)
