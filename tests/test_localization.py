import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCALE_DIR = ROOT / "addon" / "locale"
DOC_DIR = ROOT / "addon" / "doc"
VERSION_REPORT = "Unigram version: {unigramVersion}.\nUnigramPlus version: {addonVersion}."
VERSION_WINDOW_DESCRIPTION = "Open Unigram and UnigramPlus version information in a read-only window"
AUTO_FOCUS_LABEL = "Automatically move focus to the chat list when Unigram starts"
NAVIGATION_MENU_UNAVAILABLE = "Navigation menu not available"
OPEN_SETTINGS_DESCRIPTION = "Open Unigram settings"
SETTINGS_UNAVAILABLE = "Settings not available"
RELEASE_CHANGELOG = (
	"""- Space plays, opens and downloads the media of a message again in Unigram 13.0 and later, including voice messages.
- Space no longer opens stickers or link previews in Unigram 13.0.1 and later.
- Right and Left Arrow on a message with several attachments announce each photo, video, file or song again in Unigram 13.0 and later.
- Ctrl+Space now also selects chats in the chat list: the first press starts selection mode from the chat's context menu, and each press after that selects or unselects the focused chat.
- Alt+Shift+M is a new shortcut that opens Unigram's settings in Unigram 13.1 and later and moves the focus to the top of the settings."""
)
PREVIOUS_RELEASE_CHANGELOG = (
	"""- Alt+M opens the navigation menu again in Unigram 13.1 and later, where the menu button opens a menu instead of the side pane.
- Ctrl+Space selects and unselects messages again in Unigram's selection mode, the way Space does in Unigram 13.1.1. In selection mode, Space and Enter on a message also select or unselect it instead of playing its media or replying to it.
- Updated compatibility for NVDA 2026.3.
- Updated the Polish and Vietnamese translations."""
)
RECORDING_NOTIFICATION_LABEL = "Notification when a voice message recording starts or is sent:"

# The voice recording feature bullet said canceling was accompanied by a sound
# until Unigram 13.0 started announcing a canceled recording itself. Keyed by
# manual language; the root readme.md mirrors the English one.
RECORDING_CANCELED_FEATURE = {
	"en": "Recording, sending and canceling",
	"NE": "रेकर्ड गर्ने, पठाउने र रद्दगर्दा",
	"ar": "وإلغاء تسجيلها",
	"es": "envío y cancelación de mensajes de voz",
	"fa": "ضبط، ارسال و لغو ضبط",
	"fr": "l'envoi et l'annulation de l'enregistrement",
	"hr": "Snimanje, slanje i otkazivanje",
	"pt_BR": "gravar, enviar e cancelar",
	"pt_PT": "gravar, enviar e cancelar",
	"ro": "trimiterea și anularea înregistrării",
	"ru": "Запись, отправка и отмена записи",
	"sr": "i otkazivanje snimanja popraćeni",
	"tr": "kayıt iptaline farklı sesler",
	"uk": "Запис, надсилання та скасування запису",
	"zh_CN": "录制、发送和取消语音消息",
	"zh_TW": "錄製、傳送與取消語音訊息",
}

# The call duration feature bullet each manual carried before Unigram 12.10
# started announcing it natively. Keyed by manual language; the root readme.md
# mirrors the English one.
CALL_DURATION_FEATURE = {
	"en": "the duration of this call is announced",
	"NE": "कलको अवधि समेत घोषणा",
	"ar": "يتم الإعلان عن مدة هذه المكالمة",
	"es": "se anuncia la duración de dicha llamada",
	"fa": "مدت زمان این تماس اعلام می شود",
	"fr": "la durée de celui-ci est annoncée",
	"hr": "najavljuje se trajanje tog poziva",
	"pt_BR": "a duração dessa chamada é anunciada",
	"pt_PT": "a duração dessa chamada é anunciada",
	"ro": "se anunță durata acestui apel",
	"ru": "объявляется продолжительность этого звонка",
	"sr": "objavljuje se trajanje tog poziva",
	"tr": "bu çağrının süresi duyulur",
	"uk": "озвучується тривалість цьього дзвінка",
	# Chinese stated it inside a combined sentence, so the removed words are the marker.
	"zh_CN": "通话消息",
	"zh_TW": "通話訊息",
}

# Only active runtime strings belong here. Historical release notes and removed
# features may correctly be absent from the newest translator-maintained catalogs.
REQUIRED_TRANSLATIONS = {
	"Interface language in Unigram:",
	"Speak the type of chat in the chat list:",
	AUTO_FOCUS_LABEL,
	NAVIGATION_MENU_UNAVAILABLE,
	OPEN_SETTINGS_DESCRIPTION,
	SETTINGS_UNAVAILABLE,
	"Say the sender's name in:",
	RECORDING_NOTIFICATION_LABEL,
	"Select the progress bar notification level:",
	"File transfer progress announcement interval (percent):",
	"Rich message",
	"Move to the next or previous chat with unread mentions",
	"No more chats with unread mentions in this direction",
	"No search results",
	"Toggle whether message headers are announced before or after the message content",
	"Message headers will be announced after the message content",
	"Message headers will be announced before the message content",
	"Announce message headers after the message content",
	"Play a sound when reaching the end of a chat",
	VERSION_WINDOW_DESCRIPTION,
	VERSION_REPORT,
}


def _parse_po(path: Path, obsolete: bool = False) -> dict[str, str]:
	"""Return singular gettext entries without external dependencies.

	Obsolete (#~) entries are left out unless ``obsolete`` asks for them.
	"""
	entries: dict[str, str] = {}
	msgid_parts: list[str] = []
	msgstr_parts: list[str] = []
	state = None

	def finish_entry():
		if msgid_parts:
			entries["".join(msgid_parts)] = "".join(msgstr_parts)

	for line in path.read_text(encoding="utf-8").splitlines() + [""]:
		if not line:
			finish_entry()
			msgid_parts.clear()
			msgstr_parts.clear()
			state = None
			continue
		if line.startswith("#~"):
			if not obsolete:
				continue
			line = line[2:].lstrip()
		if line.startswith("msgid "):
			msgid_parts.append(ast.literal_eval(line[6:]))
			state = "msgid"
		elif line.startswith("msgstr "):
			msgstr_parts.append(ast.literal_eval(line[7:]))
			state = "msgstr"
		elif line.startswith('"') and state == "msgid":
			msgid_parts.append(ast.literal_eval(line))
		elif line.startswith('"') and state == "msgstr":
			msgstr_parts.append(ast.literal_eval(line))
	return entries


def test_required_strings_are_translated_in_every_locale():
	locale_dirs = sorted(path for path in LOCALE_DIR.iterdir() if path.is_dir())
	assert len(locale_dirs) == 20
	for locale_dir in locale_dirs:
		entries = _parse_po(locale_dir / "LC_MESSAGES" / "nvda.po")
		missing = sorted(key for key in REQUIRED_TRANSLATIONS if not entries.get(key))
		assert not missing, f"{locale_dir.name} has missing translations: {missing}"
		for placeholder in ("{unigramVersion}", "{addonVersion}"):
			assert placeholder in entries[VERSION_REPORT], (
				f"{locale_dir.name} version report is missing {placeholder}"
			)
		assert "\n" in entries[VERSION_REPORT], (
			f"{locale_dir.name} version report does not put UnigramPlus on a new line"
		)


def test_release_version_is_586():
	build_vars = (ROOT / "buildVars.py").read_text(encoding="utf-8")
	pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
	lockfile = (ROOT / "uv.lock").read_text(encoding="utf-8")

	assert 'addon_version="5.8.6"' in build_vars
	assert 'addon_lastTestedNVDAVersion="2026.3.0"' in build_vars
	assert 'version = "5.8.6"' in pyproject
	assert 'name = "unigramplus"\nversion = "5.8.6"' in lockfile

	# addon/manifest.ini is a gitignored build artifact and may be stale, so the
	# template is what gets checked: it is what carries addon_version into the build.
	template = (ROOT / "manifest.ini.tpl").read_text(encoding="utf-8")
	assert "version = {addon_version}" in template


def test_catalogs_keep_the_586_translation_metadata():
	for locale_dir in sorted(path for path in LOCALE_DIR.iterdir() if path.is_dir()):
		catalog_path = locale_dir / "LC_MESSAGES" / "nvda.po"
		catalog = catalog_path.read_text(encoding="utf-8")
		assert '"Project-Id-Version: UnigramPlus 5.8.6\\n"' in catalog


def test_current_release_changelog_comes_from_the_changelog_source():
	changelog = (ROOT / "changelog.py").read_text(encoding="utf-8")
	namespace = {}
	exec(compile(changelog, "changelog.py", "exec"), namespace)

	assert namespace["value"] == RELEASE_CHANGELOG
	for marker in ("Space", "Unigram 13.0", "voice messages", "stickers or link previews", "Unigram 13.0.1", "Right and Left Arrow", "Ctrl+Space", "chat list", "Alt+Shift+M", "Unigram 13.1"):
		assert marker in changelog, marker


def test_every_catalog_translates_the_current_release_changelog():
	for locale_dir in sorted(path for path in LOCALE_DIR.iterdir() if path.is_dir()):
		entries = _parse_po(locale_dir / "LC_MESSAGES" / "nvda.po")
		assert entries.get(RELEASE_CHANGELOG), locale_dir.name
		assert entries[RELEASE_CHANGELOG].count("\n") == 4, locale_dir.name
		first, second, third, fourth, fifth = entries[RELEASE_CHANGELOG].split("\n")
		# Voice messages, the rest and album names work again from 13.0;
		# stickers and link previews were named like media buttons in 13.0.1.
		assert "13.0" in first and "13.0.1" not in first, locale_dir.name
		assert "13.0" in third and "13.0.1" not in third, locale_dir.name
		assert "13.0.1" in second, locale_dir.name
		# Ctrl+Space in the chat list is new, not a fix for a Unigram version.
		assert "Ctrl+Space" in fourth and "13." not in fourth, locale_dir.name
		# Alt+Shift+M needs the Settings tab that Unigram 13.1 added below the chat list.
		assert "Alt+Shift+M" in fifth and "13.1" in fifth, locale_dir.name
		# The 5.8.5 notes stay translated in each catalog's history. Poedit keeps
		# them as an obsolete entry once changelog.py moves on.
		history = _parse_po(locale_dir / "LC_MESSAGES" / "nvda.po", obsolete=True)
		assert history.get(PREVIOUS_RELEASE_CHANGELOG), locale_dir.name


def test_the_italian_selected_state_is_italian_only():
	"""It is said before selected messages and chats; it used to end in "Виділено"."""
	entries = _parse_po(LOCALE_DIR / "it" / "LC_MESSAGES" / "nvda.po")

	assert entries["Selected"] == "Selezionato"


def test_the_english_manual_carries_the_current_release():
	for manual in (ROOT / "readme.md", DOC_DIR / "en" / "readme.md"):
		text = manual.read_text(encoding="utf-8")
		version_586 = text.index("5.8.6")
		section_586 = text[version_586:text.index("5.8.5", version_586)]
		assert section_586.count("\n* ") == 6, manual
		assert "Unigram 13.0.1" in section_586, manual
		assert "voice-to-text button" in section_586, manual
		assert "Unigram 13.1.1" in section_586, manual
		assert "Escape" in section_586, manual
		assert "stickers or link previews" in section_586, manual
		assert "Right and Left Arrow" in section_586, manual
		assert '"Медіа"' in section_586, manual
		assert "Ctrl+Space now also works in the chat list" in section_586, manual
		assert '"Selected"' in section_586, manual
		assert "Alt+Shift+M" in section_586, manual
		assert "UnigramPlusRussianMod" in section_586, manual
		assert "Add account" in section_586, manual
		assert f'"{SETTINGS_UNAVAILABLE}"' in section_586, manual
		version_585 = text.index("5.8.5")
		section_585 = text[version_585:text.index("5.8.4", version_585)]
		assert section_585.count("\n* ") == 5, manual
		assert "Alt+M" in section_585, manual
		assert "Unigram 13.1" in section_585, manual
		assert "toggle button" in section_585, manual
		assert "Ctrl+Space" in section_585, manual
		assert "Unigram 13.1.1" in section_585, manual
		assert "no Select command" in section_585, manual
		assert "Space and Enter on a message" in section_585, manual
		assert "Backspace" in section_585, manual
		assert f'"{NAVIGATION_MENU_UNAVAILABLE}"' in section_585, manual
		assert "NVDA 2026.3" in section_585, manual
		assert "Polish and Vietnamese" in section_585, manual
		version_584 = text.index("5.8.4")
		section_584 = text[version_584:text.index("5.8.3", version_584)]
		assert section_584.count("\n* ") == 2, manual
		assert f'"{AUTO_FOCUS_LABEL}"' in section_584, manual
		assert "invite link" in section_584, manual
		assert "Since version 5.6.1" in section_584, manual
		assert "Vietnamese translation" in section_584, manual
		version_583 = text.index("5.8.3")
		section_583 = text[version_583:text.index("5.8.2", version_583)]
		assert section_583.count("\n* ") == 4, manual
		assert "version 4.8.0" in section_583, manual
		assert "Unigram 13.0" in section_583, manual
		assert "Emoji, GIFs and Stickers" in section_583, manual
		assert "Alt+1" in section_583, manual
		assert "Unigram 9.5" in section_583, manual
		assert "version 5.2.0" in section_583, manual
		assert "Polish and Vietnamese" in section_583, manual
		version_582 = text.index("5.8.2")
		version_581 = text.index("5.8.1", version_582)
		section_582 = text[version_582:version_581]
		assert section_582.count("\n* ") == 4, manual
		assert "WinUI 3" in section_582, manual
		assert "Since version 5.5.6" in section_582, manual
		assert "Telegram Desktop add-on" in section_582, manual
		assert "Unigram 13.0" in section_582, manual
		assert RECORDING_NOTIFICATION_LABEL.rstrip(":") in section_582, manual
		assert "Polish and Vietnamese" in section_582, manual
		version_581 = text.index("5.8.1")
		version_580 = text.index("5.8.0", version_581)
		section_581 = text[version_581:version_580]
		section_580 = text[version_580:text.index("5.7.3", version_580)]
		assert section_581.count("\n* ") == 4, manual
		assert "call duration workaround" in section_581, manual
		assert "utils.security" in section_581, manual
		assert section_580.count("\n* ") == 10, manual
		assert "main loop" in section_580, manual
		assert "version 5.4" in section_580, manual


def test_every_localized_manual_has_586_585_584_583_582_581_and_580_changelogs():
	manuals = [ROOT / "readme.md", *sorted(DOC_DIR.glob("*/readme.md"))]
	assert len(manuals) == 17
	for manual in manuals:
		text = manual.read_text(encoding="utf-8")
		language = manual.parent.name
		if manual == ROOT / "readme.md" or language == "en":
			entries = {
				AUTO_FOCUS_LABEL: AUTO_FOCUS_LABEL,
				NAVIGATION_MENU_UNAVAILABLE: NAVIGATION_MENU_UNAVAILABLE,
				OPEN_SETTINGS_DESCRIPTION: OPEN_SETTINGS_DESCRIPTION,
				SETTINGS_UNAVAILABLE: SETTINGS_UNAVAILABLE,
				"Selected": "Selected",
			}
		else:
			# Only the Nepali manual folder is named differently from its catalog.
			catalog = LOCALE_DIR / {"NE": "ne"}.get(language, language) / "LC_MESSAGES" / "nvda.po"
			entries = _parse_po(catalog)
		version_586 = text.index("5.8.6")
		section_586 = text[version_586:text.index("5.8.5", version_586)]
		assert section_586.count("\n* ") == 6, manual
		# Space, Escape and the arrows are named in each language's own words.
		# The album note quotes the placeholder word the add-on used to say.
		for marker in ("13.0", "13.0.1", "13.1.1", "GIF", "UnigramPlus", "Медіа", "Ctrl+Space"):
			assert marker in section_586, (manual, marker)
		# The chat-list note quotes what is said before a selected chat, as the
		# catalog translates it.
		chat_list_note = section_586.split("\n* ")[5]
		assert "Ctrl+Space" in chat_list_note, manual
		assert entries["Selected"].rstrip(".") in chat_list_note, manual
		# The Alt+Shift+M note quotes what is said without a Settings tab.
		settings_note = section_586.split("\n* ")[6]
		for marker in ("Alt+Shift+M", "13.1", "UnigramPlusRussianMod"):
			assert marker in settings_note, (manual, marker)
		assert entries[SETTINGS_UNAVAILABLE].rstrip(".") in settings_note, manual
		# The shortcut table names it as the catalog describes the script.
		row = f"| **ALT+Shift+M** | UnigramPlus | {entries[OPEN_SETTINGS_DESCRIPTION]} |"
		assert text.count(row) == 1, manual
		assert text.index(row) < text.index("<!-- shortcut-table-end -->"), manual
		version_585 = text.index("5.8.5")
		section_585 = text[version_585:text.index("5.8.4", version_585)]
		assert section_585.count("\n* ") == 5, manual
		# Single keys such as Backspace are named in each language's own words.
		for marker in ("Alt+M", "13.1", "Ctrl+Space", "13.1.1", "2026.3"):
			assert marker in section_585, (manual, marker)
		# Each manual quotes the message Alt+M spoke, as its catalog translates it.
		assert entries[NAVIGATION_MENU_UNAVAILABLE].rstrip(".") in section_585, manual
		version_584 = text.index("5.8.4")
		section_584 = text[version_584:text.index("5.8.3", version_584)]
		assert section_584.count("\n* ") == 2, manual
		assert "5.6.1" in section_584, manual
		# Each manual names the setting as its language's catalog translates it.
		assert entries[AUTO_FOCUS_LABEL] in section_584, manual
		version_583 = text.index("5.8.3")
		section_583 = text[version_583:text.index("5.8.2", version_583)]
		assert section_583.count("\n* ") == 4, manual
		for marker in ("4.8.0", "13.0", "Alt+1", "GIF", "9.5", "5.2.0"):
			assert marker in section_583, (manual, marker)
		assert "Enter" in section_583 or "Entrée" in section_583, manual
		version_582 = text.index("5.8.2")
		section_582 = text[version_582:text.index("5.8.1", version_582)]
		assert section_582.count("\n* ") == 4, manual
		for marker in ("WinUI 3", "5.5.6", "IME", "UWP", "Telegram Desktop", "13.0", "Ctrl+D"):
			assert marker in section_582, (manual, marker)
		version_581 = text.index("5.8.1")
		version_580 = text.index("5.8.0", version_581)
		version_573 = text.index("5.7.3", version_580)
		assert text[version_581:version_580].count("\n* ") == 4, manual
		assert text[version_580:version_573].count("\n* ") == 10, manual
		assert "12.10" in text[version_581:version_580], manual
		assert "utils.security" in text[version_581:version_580], manual


def test_the_call_duration_workaround_is_gone_everywhere():
	"""Unigram 12.10 names the duration itself, so the add-on must not add it."""
	source = (ROOT / "addon" / "appModules" / "unigram.py").read_text(encoding="utf-8-sig")
	assert "Checking if a message is a call" not in source

	for manual in [ROOT / "readme.md", *sorted(DOC_DIR.glob("*/readme.md"))]:
		language = "en" if manual.parent == ROOT else manual.parent.name
		text = manual.read_text(encoding="utf-8")
		# Everything before the current release notes: the feature list, the
		# shortcut tables and every historical changelog entry. The phrase only
		# ever appeared in the feature list, so it must not appear here at all.
		# The 5.8.1 notes themselves do describe the removal, in Chinese using
		# the same words, which is why they are excluded.
		assert CALL_DURATION_FEATURE[language] not in text[:text.index("5.8.1")], manual


def test_feature_lists_leave_canceled_recordings_to_unigram():
	"""Unigram 13.0 announces a canceled recording, so the add-on no longer claims to."""
	for manual in [ROOT / "readme.md", *sorted(DOC_DIR.glob("*/readme.md"))]:
		language = "en" if manual.parent == ROOT else manual.parent.name
		text = manual.read_text(encoding="utf-8")
		# The feature list ends at the first ### heading. Older release notes,
		# which some manuals keep above 5.8.2, still describe the sound.
		features = text[:text.index("###")]
		assert RECORDING_CANCELED_FEATURE[language] not in features, manual
		assert "Unigram 13.0" in features, manual


def test_every_localized_manual_has_573_through_559_and_updated_558_changelogs():
	manuals = [ROOT / "readme.md", *sorted(DOC_DIR.glob("*/readme.md"))]
	assert len(manuals) == 17
	for manual in manuals:
		text = manual.read_text(encoding="utf-8")
		version_573 = text.index("5.7.3")
		version_572 = text.index("5.7.2", version_573)
		version_571 = text.index("5.7.1", version_572)
		version_570 = text.index("5.7.0", version_571)
		version_569 = text.index("5.6.9", version_570)
		version_568 = text.index("5.6.8", version_569)
		version_567 = text.index("5.6.7", version_568)
		version_566 = text.index("5.6.6", version_567)
		version_565 = text.index("5.6.5", version_566)
		version_564 = text.index("5.6.4", version_565)
		version_563 = text.index("5.6.3", version_564)
		version_562 = text.index("5.6.2", version_563)
		version_561 = text.index("5.6.1", version_562)
		version_560 = text.index("5.6.0", version_561)
		version_559 = text.index("5.5.9", version_560)
		version_558 = text.index("5.5.8", version_559)
		section_573 = text[version_573:version_572]
		section_572 = text[version_572:version_571]
		section_571 = text[version_571:version_570]
		section_570 = text[version_570:version_569]
		section_569 = text[version_569:version_568]
		section_568 = text[version_568:version_567]
		section_567 = text[version_567:version_566]
		section_566 = text[version_566:version_565]
		section_565 = text[version_565:version_564]
		section_564 = text[version_564:version_563]
		section_563 = text[version_563:version_562]
		section_562 = text[version_562:version_561]
		section_561 = text[version_561:version_560]
		section_560 = text[version_560:version_559]
		assert section_573.count("\n* ") == 1, manual
		assert "NVDA+Alt+V" in section_573, manual
		assert section_572.count("\n* ") == 1, manual
		assert "NVDA+Alt+V" in section_572, manual
		assert section_571.count("\n* ") == 1, manual
		assert "12.10.2" in section_571, manual
		assert section_570.count("\n* ") == 2, manual
		assert "12.10.1+" in section_569, manual
		assert section_569.count("\n* ") == 5, manual
		assert "Alt+C" in section_568, manual
		assert "WhatsApp Enhancer" in section_568, manual
		assert section_568.count("\n* ") == 1, manual
		assert "NVDA+Alt+V" in section_567, manual
		assert "Shift+Delete" in section_567 or "Shift+Suppr" in section_567, manual
		assert section_567.count("\n* ") == 2, manual
		assert "NVDA+Shift+V" in section_566 or "NVDA+Maj+V" in section_566, manual
		assert "12.9.1" in section_566, manual
		assert section_566.count("\n* ") == 3, manual
		assert "Enter" in section_565 or "Entrée" in section_565, manual
		assert "Alt+Shift+R" in section_565 or "Alt+Maj+R" in section_565, manual
		assert "Alt+C" in section_565, manual
		assert section_565.count("\n* ") == 3, manual
		assert "Shift+Delete" in section_564, manual
		assert "Alt+2" in section_564, manual
		assert "Alt+C" in section_564, manual
		assert "12.9" in section_564, manual
		assert section_564.count("\n* ") == 6, manual
		assert "NVDA" in section_563, manual
		assert "Alt+[" in section_563, manual
		assert section_563.count("\n* ") == 3, manual
		assert "Ctrl+Alt+Left/Right" in section_562, manual
		assert "Alt+I" in section_562, manual
		assert "Alt+[" in section_562, manual
		assert section_562.count("\n* ") == 3, manual
		assert "Ctrl+Alt+Up/Down" in section_561, manual
		assert section_561.count("\n* ") == 3, manual
		assert "Ctrl+R" in section_560, manual
		assert section_560.count("\n* ") == 3, manual
		assert "Alt+C" in text[version_559:version_558], manual
		assert "GitHub" in text[version_558:text.find("5.5.7", version_558)], manual


def test_every_manual_still_documents_the_file_duration_it_does_announce():
	"""The audio file's own duration is a separate, still-present feature."""
	kept = {
		"en": "name and duration",
		"es": "nombre y duración",
		"fr": "son nom et sa durée",
		"hr": "naziv i trajanje",
		"ro": "numele și durata",
		"ru": "название и продолжительность",
		"uk": "назва і тривалість",
	}
	for language, phrase in kept.items():
		manual = ROOT / "readme.md" if language == "en" else DOC_DIR / language / "readme.md"
		assert phrase in manual.read_text(encoding="utf-8"), language


def test_removed_web_view_setting_is_absent_but_historical_changelogs_remain():
	setting = "Display message text in a web view when pressing Alt+C"
	runtime_hint = "Rich message. Press Alt+C to browse"
	for locale_dir in sorted(path for path in LOCALE_DIR.iterdir() if path.is_dir()):
		entries = _parse_po(locale_dir / "LC_MESSAGES" / "nvda.po")
		assert setting not in entries, locale_dir
		assert runtime_hint not in entries, locale_dir
	manuals = [ROOT / "readme.md", *sorted(DOC_DIR.glob("*/readme.md"))]
	for manual in manuals:
		text = manual.read_text(encoding="utf-8")
		section_564 = text[text.index("5.6.4"):text.index("5.6.3", text.index("5.6.4"))]
		section_559 = text[text.index("5.5.9"):text.index("5.5.8", text.index("5.5.9"))]
		assert "Alt+C" in section_564, manual
		assert "Alt+C" in section_559, manual
