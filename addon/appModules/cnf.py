from  configobj  import  ConfigObj
from configobj.validate import Validator
import os
import globalVars
import languageHandler
import addonHandler
addonHandler.initTranslation()

listLanguages = {
	"ar": _("Arabic"),
	"be": _("Belarus"),
	"my": _("Burmese"),
	"cs": _("Czech"),
	"en": _("English"),
	"fr": _("French"),
	"fi": _("Finnish"),
	"sl": _("Slovak"),
	"nb": _("Norwegian"),
	"de": _("German"),
	"it": _("Italian"),
	"fa": _("Persian"),
	"pl": _("Polish"),
	"pt": _("Portuguese"),
	"ru": _("Russian"),
	"es": _("Spanish"),
	"tr": _("Turkish"),
	"uk": _("Ukrainian"),
	"vi": _("Vietnamese"),
	"hr": _("Croatian"),
	"sr": _("Serbian"),
	"zh_TW": _("Chinese (Traditional)"),
	"zh_CN": _("Chinese (Simplified)"),
	"ro": _("Romanian"),
}

def getDefaultLang():
	lang = languageHandler.getLanguage()
	if lang in listLanguages:
		return lang
	baseLang = lang.split("_")[0]
	return baseLang if baseLang in listLanguages else "en"
lang = getDefaultLang()

spec = (
	f"lang = string(default={lang if lang in listLanguages else 'en'})",
	"voiceTypeAfterChatName = string(default=beforeName)",
	"autoFocusChatList = boolean(default=True)",
	"unreadBeforeMessageContent = boolean(default=True)",
	"voiceFolderNames = boolean(default=True)",
	"voiceMessageRecordingIndicator = string(default=audio)",
	"voicingPerformanceIndicators = string(default=upload_download)",
	"fileTransferProgressInterval = integer(default=1, min=1, max=100)",
	# One-shot marker so we can migrate users who had the old default of "none" to
	# the new "upload_download" mode the first time they launch 5.5.3.
	"voicingPerformanceIndicators_migrated_5_5_3 = boolean(default=False)",
	"audioPlaybackWhenDeleted = boolean(default=False)",
	"confirmation_at_deletion = boolean(default=False)",
	"actionDescriptionForLinks = boolean(default=True)",
	"voiceFullDescriptionOfLinkToYoutube = boolean(default=True)",
	"isAnnouncesAnswers = boolean(default=True)",
	"is_automatically_check_for_updates = boolean(default=True)",
	"isFixedToggleButton = boolean(default=False)",
	"saySenderName = string(default=none)",
	"messageHeaderAtTheEnd = boolean(default=False)",
	"voice_the_presence_of_a_reaction = boolean(default=True)",
	"report premium accounts = boolean(default=True)",
	"automatically announce new messages = boolean(default=False)",
	"automatically announce activity in chats = boolean(default=False)",
	"notify administrators in messages = boolean(default=True)",
	"action_when_pressing_up_arrow_in_text_field = string(default=normal)",
	"announce_endthe_message = boolean(default=True)",
	"play_end_of_chat_sound = boolean(default=True)",
	"play_typing_sound = boolean(default=True)",
	# Everything below was added after 5.4 and is on by default, so upgrading
	# changes nothing; each one can be turned off to get the older behavior back.
	# How the voice/video record button is announced (5.5.7).
	"voiceRecordingButtonLabel = string(default=withElapsedTime)",
	# Rich message detection for announcements and ALT+C (5.5.9).
	"richMessageSupport = boolean(default=True)",
	# Name the profile identity button after the chat instead of "Identity root" (5.5.6).
	"labelProfileIdentityButton = boolean(default=True)",
	# Say "Reply"/"Editing" in the message field instead of the usual prompt (5.5.5).
	"announceComposerState = boolean(default=True)",
	# Suppress the transient "list" announcement before a message (5.6.3).
	"suppressMessagesListAnnouncement = boolean(default=True)",
	# Announce the live state of the call Mute and Camera toggles (5.5.8).
	"announceCallControlState = boolean(default=True)",
	# Append the unread count when switching chat folders (5.7.0).
	"announceFolderUnreadCount = boolean(default=True)"
)

class cnf:
	def __init__(self):
		self.path = os.path.join(globalVars.appArgs.configPath, "UnigramPlus.ini")
		self.conf = ConfigObj(self.path, configspec=spec )
		validator = Validator()
		self.conf.validate(validator, copy=True)
		if self.conf.get("lang") == "zh":
			self.conf["lang"] = "zh_TW"
		self.conf.write()
	def get(self, key):
		return self.conf[key]
	def set(self, key, value):
		self.conf[key] = value
		self.conf.write()

try: conf = cnf()
except OSError:
	# Environmental failure (e.g. permissions, locked file, full disk): the
	# ini itself may still be valid, so don't destroy it - just propagate.
	raise
except Exception:
	# Anything else (parse/validation errors, unexpected values, etc.) means
	# the ini content itself is the problem: drop it and rebuild from defaults.
	from logHandler import log
	log.error("UnigramPlus.ini could not be loaded, recreating it with defaults", exc_info=True)
	path = os.path.join(globalVars.appArgs.configPath, "UnigramPlus.ini")
	if os.path.exists(path):
		os.remove(path)
	conf = cnf()
