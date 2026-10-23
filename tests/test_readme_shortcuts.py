from pathlib import Path
import sys

from markdown import markdown


sys.path.insert(0, str(Path(__file__).parents[1] / "addon" / "appModules"))

from readme_shortcuts import extractShortcutText  # noqa: E402


def test_extracts_all_marked_table_categories():
	markdown = """# Readme

<!-- shortcut-table-start -->
## Keyboard shortcuts

### Search

| Shortcut | Category | Action |
|---|---|---|
| **Ctrl+E** | Unigram | Chat search |
| **ALT+I** | UnigramPlus | Open search results |

### Calls

| Shortcut | Category | Action |
|---|---|---|
| **ALT+Y** | UnigramPlus | Accept call |
<!-- shortcut-table-end -->

## Changes
"""

	assert extractShortcutText(markdown) == (
		"Search\n"
		"Ctrl+E - Unigram - Chat search\n"
		"ALT+I - UnigramPlus - Open search results\n"
		"\n"
		"Calls\n"
		"ALT+Y - UnigramPlus - Accept call"
	)


def test_incomplete_markers_fall_back_to_legacy_list():
	markdown = """# Readme

## Hotkey list:
* ALT+1: Move focus to chat list
* ALT+2: Move focus to the last message
"""

	assert extractShortcutText(markdown) == (
		"Hotkey list:\n"
		"ALT+1: Move focus to chat list\n"
		"ALT+2: Move focus to the last message"
	)


def test_skips_localized_table_header():
	markdown = """<!-- shortcut-table-start -->
### 搜尋
| 快速鍵 | 類別 | 操作 |
|---|---|---|
| **Ctrl+E** | Unigram | 搜尋聊天 |
<!-- shortcut-table-end -->"""

	assert extractShortcutText(markdown) == "搜尋\nCtrl+E - Unigram - 搜尋聊天"


def test_preserves_escaped_pipes_in_table_cells():
	markdown = """<!-- shortcut-table-start -->
### Media
| Shortcut | Category | Action |
|---|---|---|
| **Space** | UnigramPlus | Play \\| pause |
<!-- shortcut-table-end -->"""

	assert extractShortcutText(markdown) == "Media\nSpace - UnigramPlus - Play | pause"


def test_all_readmes_have_complete_integrated_shortcut_tables():
	root = Path(__file__).parents[1]
	readmes = [root / "readme.md", *sorted((root / "addon" / "doc").glob("*/readme.md"))]
	reference_unigram_shortcuts = None

	assert len(readmes) == 17
	for readme in readmes:
		text = readme.read_text(encoding="utf-8")
		shortcut_table = text.split("<!-- shortcut-table-start -->", 1)[1].split(
			"<!-- shortcut-table-end -->", 1)[0]
		unigram_shortcuts = [
			line.split("|")[1].strip()
			for line in shortcut_table.splitlines()
			if "| Unigram |" in line
		]
		assert text.count("<!-- shortcut-table-start -->") == 1, readme
		assert text.count("<!-- shortcut-table-end -->") == 1, readme
		assert text.count("|---|---|---|") == 9, readme
		assert text.count("| Unigram |") == 44, readme
		assert text.count("| UnigramPlus |") == 54, readme
		assert "| **ALT+Shift+M** | UnigramPlus |" in shortcut_table, readme
		undocumented_shortcuts = [
			line
			for line in shortcut_table.splitlines()
			if line.startswith("|")
			and len(line.split("|")) == 5
			and line.split("|")[2].strip().startswith("Unigram")
			and line.split("|")[2].strip() not in ("Unigram", "UnigramPlus")
		]
		assert len(undocumented_shortcuts) == 18, readme
		assert "| **Ctrl+Shift+.** | Unigram |" in text, readme
		assert "| **Ctrl+U** | Unigram |" in text, readme
		assert any("**Ctrl+F4**" in line for line in undocumented_shortcuts), readme
		assert any("**Ctrl+Shift+Down**" in line for line in undocumented_shortcuts), readme
		assert any("**Ctrl+O**" in line for line in undocumented_shortcuts), readme
		assert any("**Ctrl+Shift+E**" in line for line in undocumented_shortcuts), readme
		assert any("**Ctrl+Shift+G**" in line for line in undocumented_shortcuts), readme
		assert any("**Ctrl+Shift+S**" in line for line in undocumented_shortcuts), readme
		assert any("**Ctrl+Shift+Z**" in line for line in undocumented_shortcuts), readme
		assert any("**Alt+X**" in line for line in undocumented_shortcuts), readme
		assert any("**Delete**" in line for line in undocumented_shortcuts), readme
		assert not any("**Ctrl+1 through Ctrl+5**" in line for line in undocumented_shortcuts), readme
		assert "| Search the current page || **ALT+T**" not in text, readme
		assert "| **ALT+End** |" not in text, readme
		assert "5.7.0" in text, readme
		assert "5.6.9" in text, readme
		assert "5.6.8" in text, readme
		assert "| **NVDA+Alt+V** | UnigramPlus |" in text, readme
		assert "5.7.2" in text, readme
		if reference_unigram_shortcuts is None:
			reference_unigram_shortcuts = unigram_shortcuts
		else:
			assert unigram_shortcuts == reference_unigram_shortcuts, readme


def test_chinese_readmes_use_unigram_interface_terms():
	root = Path(__file__).parents[1] / "addon" / "doc"
	traditional = (root / "zh_TW" / "readme.md").read_text(encoding="utf-8")
	simplified = (root / "zh_CN" / "readme.md").read_text(encoding="utf-8")

	assert "| **Ctrl+0** | Unigram | 我的收藏 |" in traditional
	assert "| **Ctrl+9** | Unigram | 封存 |" in traditional
	assert "| **Ctrl+0** | Unigram | 我的收藏 |" in simplified
	assert "| **Ctrl+9** | Unigram | 归档 |" in simplified


def test_markdown_tables_render_for_addon_documentation():
	rootReadme = (Path(__file__).parents[1] / "readme.md").read_text(encoding="utf-8")

	assert markdown(rootReadme, extensions=["markdown.extensions.tables"]).count("<table>") == 9
