from  configobj  import  ConfigObj
from configobj.validate import Validator
import os
import globalVars
import languageHandler
import addonHandler
addonHandler.initTranslation()

lang = languageHandler.getLanguage().split("_")[0]

listLanguages = {
	"ar": _("Arabic"),
	"be": _("Belarus"),
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
	"hr": _("Croatian"),
	"sr": _("Serbian"),
	"zh": _("Chinese (Traditional)"),
}

spec = (
	f"lang = string(default={lang if lang in listLanguages else 'en'})",
	"voiceTypeAfterChatName = string(default=beforeName)",
	"unreadBeforeMessageContent = boolean(default=True)",
	"voiceFolderNames = boolean(default=True)",
	"voiceMessageRecordingIndicator = string(default=audio)",
	"voicingPerformanceIndicators = string(default=none)",
	"audioPlaybackWhenDeleted = boolean(default=False)",
	"confirmation_at_deletion = boolean(default=False)",
	"actionDescriptionForLinks = boolean(default=True)",
	"voiceFullDescriptionOfLinkToYoutube = boolean(default=True)",
	"isAnnouncesAnswers = boolean(default=True)",
	"is_automatically_check_for_updates = boolean(default=True)",
	"isFixedToggleButton = boolean(default=False)",
	"saySenderName = string(default=none)",
	"voice_the_presence_of_a_reaction = boolean(default=True)",
	"report premium accounts = boolean(default=True)",
	"automatically announce new messages = boolean(default=False)",
	"automatically announce activity in chats = boolean(default=False)",
	"notify administrators in messages = boolean(default=True)",
	"action_when_pressing_up_arrow_in_text_field = string(default=normal)",
)

class cnf:
	def __init__(self):
		self.path = os.path.join(globalVars.appArgs.configPath, "UnigramPlus.ini")
		self.conf = ConfigObj(self.path, configspec=spec )
		validator = Validator()
		self.conf.validate(validator, copy=True)
		self.conf.write()
	def get(self, key):
		return self.conf[key]
	def set(self, key, value):
		self.conf[key] = value
		self.conf.write()

try: conf = cnf()
except:
	path = os.path.join(globalVars.appArgs.configPath, "UnigramPlus.ini")
	os.remove(path)
	conf = cnf()