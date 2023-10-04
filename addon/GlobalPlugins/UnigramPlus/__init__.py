﻿# -*- coding: utf-8 -*-
import globalPluginHandler
import addonHandler
from scriptHandler import script
import api
import gui
from gui import guiHelper, nvdaControls
from gui.settingsDialogs import SettingsPanel
import wx
import urllib.request
import core
import globalVars
import os
addonHandler.initTranslation()
import languageHandler
import queueHandler
import threading, time, queue, random
from appModules.cnf import conf, listLanguages, lang
from appModules.unigram import AppModule
from ui import message

path_to_server = "http://46.254.107.124/addons/unigramplus/"

def no_updates_dialog():
	res = gui.messageBox(
		_("No updates available"),
		_("UnigramPlus update"),
		wx.OK | wx.ICON_INFORMATION)
def onCheckForUpdates(event = False, is_start = False):
	import versionInfo
	NVDAVersion = f"{versionInfo.version_year}.{versionInfo.version_major}.{versionInfo.version_minor}"
	NVDAVersion = int(NVDAVersion.replace(".", ""))
	fp = os.path.join(globalVars.appArgs.configPath, "unigramplus.nvda-addon")
	addon_version = addonHandler.getCodeAddon().manifest["version"]
	addon_version = int(addon_version.replace(".", ""))
	try: response = urllib.request.urlopen(path_to_server+"version.txt").read().decode('utf-8')
	except:
		if not is_start: wx.CallAfter(no_updates_dialog)
		return
	response = str(response)
	str_last_version = response.split("\n")[0]
	last_version = int(str_last_version.replace(".", ""))
	minimum_version = response.split("\n")[1]
	minimum_version = int(minimum_version.replace(".", ""))
	url = response.split("\n")[-1]
	if last_version > addon_version and NVDAVersion >= minimum_version:
		wx.CallAfter(window_for_update, None, str_last_version, url)
	elif not is_start: wx.CallAfter(no_updates_dialog)

class window_for_update(wx.Frame):
	def __init__(self, parent, str_last_version, url):
		title = _("UnigramPlus update")
		text = _("A new version of the add-on is available. Do you want to update UnigramPlus to version %version?").replace("%version", str_last_version)
		no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
		wx.Frame.__init__(self, parent, title = title, size = (640, 360), style=no_resize)
		self.url = str(url)
		self.str_last_version = str_last_version
		self.Centre()
		panel = wx.Panel(self, wx.ID_ANY)
		self.text = wx.TextCtrl(panel, -1, text, style = wx.TE_MULTILINE | wx.TE_READONLY)
		self.text.SetValue(text)
		self.text.SetFocus()
		self.button_ok = wx.Button(panel, label=_("Yes, update"), id=-1)
		self.button_close= wx.Button(panel, label=_("No, not now"), id=-1)
		self.button_ok.Bind(wx.EVT_BUTTON,self.download_update)
		self.button_close.Bind(wx.EVT_BUTTON,self.window_close)
		sizer = wx.BoxSizer(wx.VERTICAL)
		buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
		buttons_sizer.Add(self.button_ok)
		buttons_sizer.Add(self.button_close)
		sizer.Add(self.text, 1, wx.EXPAND)
		sizer.Add(buttons_sizer, flag = wx.ALL | wx.ALIGN_RIGHT, border=5)
		panel.SetSizer(sizer)
		self.Raise()
		self.Show(True)
		self.get_documentation()

	def download_update(self, event):
		self.text.SetValue(_("Download in progress"))
		self.text.SetFocus()
		self.button_ok.Disable()
		self.button_close.Disable()
		try: response_addon = urllib.request.urlopen(self.url).read()
		except:
			no_updates_dialog()
			self.Close()
			return
		fp = os.path.join(globalVars.appArgs.configPath, "unigramplus.nvda-addon")
		with open(fp, 'wb') as addon:
			addon.write(response_addon)
		self.setup_update(fp)

	def window_close(self, event):
		self.Close()
	
	def get_documentation(self):
		doc = False
		url = path_to_server+"documentation/"+self.str_last_version+"/"+lang+".txt"
		try: doc = urllib.request.urlopen(url).read().decode('utf-8')
		except: pass
		try:
			url = path_to_server+"documentation/"+self.str_last_version+"/en.txt"
			if not doc: doc = urllib.request.urlopen(url).read().decode('utf-8')
		except: pass
		if doc: text = "\n"+_("Changes in this version:")+"\n"+str(doc)
		else: text = "\n"+_(_("No update information"))
		self.text.SetValue(self.text.GetValue()+text)

	def setup_update(self, fp):
		curAddons = addonHandler.getAvailableAddons()
		bundle = addonHandler.AddonBundle(fp)
		bundleName = bundle.manifest['name']
		prevAddon = next((addon for addon in curAddons if not addon.isPendingRemove and bundleName == addon.manifest['name']), None)
		if prevAddon: prevAddon.requestRemove()
		addonHandler.installAddonBundle(bundle)
		core.restart()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = "UnigramPlus"
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(UnigramPlusSettings)
		# Check if the user folder contains a temporary add-on file, if so, then delete it
		fp = os.path.join(globalVars.appArgs.configPath, "unigramplus.nvda-addon")
		if os.path.exists(fp): os.remove(fp)
		# Checking for updates
		if conf.get("is_automatically_check_for_updates"):
			threading.Thread(target=onCheckForUpdates, args=(False, True,)).start()

	@script(description=_("Open UnigramPlus settings window"), gesture="kb:NVDA+control+U")
	def script_open_settings_dialog(self, gesture, arg = False):
		wx.CallAfter(gui.mainFrame._popupSettingsDialog, gui.settingsDialogs.NVDASettingsDialog, UnigramPlusSettings)

	# Call answer
	@script(description=_("Accept call"), gesture="kb:ALT+Y")
	def script_answeringCall(self, gesture):
		gesture.send()
		desctop = api.getDesktopObject()
		# notification = next((item.firstChild.firstChild for item in desctop.children if item.firstChild and hasattr(item.firstChild, "UIAAutomationId") and item.firstChild.UIAAutomationId == "PriorityToastView"), False)
		notification = next((item.firstChild.firstChild for item in desctop.children if item.firstChild and hasattr(item.firstChild, "UIAAutomationId") and item.firstChild.UIAAutomationId == "ToastCenterScrollViewer"), False)
		if not notification:
			print("Панелі з дзвінком не знайдено")
			return
		button = next((item for item in notification.children if item.UIAAutomationId == "VerbButton"), None)
		if button: button.doAction()
		else: print("Кнопку не знайдено")

	# End a call, decline call, or leave a voice chat
	@script(description=_("Press \"Decline call\" button  if there is an incoming call, \"End call\" button if a call is in progress or leave voice chat if it is active."), gesture="kb:ALT+N")
	def script_callCancellation(self, gesture):
		gesture.send()
		desctop = api.getDesktopObject()
		# notification = next((item.firstChild for item in desctop.children if item.firstChild and hasattr(item.firstChild, "UIAAutomationId") and item.firstChild.UIAAutomationId == "PriorityToastView"), False)
		notification = next((item.firstChild.firstChild for item in desctop.children if item.firstChild and hasattr(item.firstChild, "UIAAutomationId") and item.firstChild.UIAAutomationId == "ToastCenterScrollViewer"), False)
		button = None
		if notification:
			button = next((item.next for item in notification.children if item.UIAAutomationId == "VerbButton"), None)
		else: print("Панель не знайдено")
		if button:
			button.doAction()
			return
		print("Кнопку не знайдено")
		AppModule.script_callCancellation(AppModule, gesture)


class UnigramPlusSettings(SettingsPanel):
	title = "UnigramPlus"
	listVoiceTypeAfterChatName = {
		"beforeName": _("Before chat name"),
		"afterName": _("After chat name"),
		"don'tVoice": _("Do not speak chat type")
	}
	listVoiceMessageRecordingIndicator = {
		"none": _("Revert to standard voice message recording behavior"),
		"text": _("Text notification"),
		"audio": _("sound notification")
	}
	listVoicingPerformanceIndicators = {
		"all": _("Announce all progress bars"),
		"none": _("Do not announce any progress bars"),
		# "normal": _("Announce some progress bars")
	}
	listSaySenderName = {
		"none": _("Do not say at all"),
		"sent": _("Only in sent messages"),
		"received": _("Only in received messages"),
		"all": _("In all messages")
	}
	list_actions_when_pressing_up_arrow_in_text_field = {
		"block": _("Do nothing"),
		"normal": _("Activate editing of last sent message"),
		"to_messages": _("Move focus to the last message in a chat"),
	}
	
	def makeSettings(self, settingsSizer):
		settingsSizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Selecting an interface language
		# self.lang = settingsSizerHelper.addLabeledControl(_("Interface language in Unigram:"), wx.Choice, choices=[listLanguages[item] for item in listLanguages])
		self.lang = settingsSizerHelper.addLabeledControl(_("Interface language in Unigram:"), wx.Choice, choices=list(listLanguages.values()))
		self.lang.SetStringSelection(listLanguages[conf.get("lang")])
		# Chat type announce mode
		self.voiceTypeAfterChatName = settingsSizerHelper.addLabeledControl(_("Speak the type of chat in the chat list:"), wx.Choice, choices=[self.listVoiceTypeAfterChatName[item] for item in self.listVoiceTypeAfterChatName])
		self.voiceTypeAfterChatName.SetStringSelection(self.listVoiceTypeAfterChatName[conf.get("voiceTypeAfterChatName")])
		# Message sender announcement
		self.saySenderName = settingsSizerHelper.addLabeledControl(_("Say the sender's name in:"), wx.Choice, choices=[self.listSaySenderName[item] for item in self.listSaySenderName])
		self.saySenderName.SetStringSelection(self.listSaySenderName[conf.get("saySenderName")])
		# Selecting the action when pressing the up arrow in the text editor
		self.action_when_pressing_up_arrow_in_text_field = settingsSizerHelper.addLabeledControl(
			_("Action when pressing the up arrow in the message edit field"), wx.Choice, choices=list(self.list_actions_when_pressing_up_arrow_in_text_field.values()))
		self.action_when_pressing_up_arrow_in_text_field.SetStringSelection(self.list_actions_when_pressing_up_arrow_in_text_field[conf.get("action_when_pressing_up_arrow_in_text_field")])
		# Report not seen before message content
		self.unreadBeforeMessageContent = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Speak \"Not Seen\" before reading contents of a message")))
		self.unreadBeforeMessageContent.SetValue(conf.get("unreadBeforeMessageContent"))
		# Announce the phrases "Administrator" and "Owner" on messages in communities
		self.notify_administrators_in_messages = settingsSizerHelper.addItem(wx.CheckBox(
			self, label=_('Announce the phrases "Administrator" and "Owner" on messages in communities')))
		self.notify_administrators_in_messages.SetValue(
			conf.get("notify administrators in messages"))
		# Speak active folder name when switching between them
		self.voiceFolderNames = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Speak folder names when switching between them")))
		self.voiceFolderNames.SetValue(conf.get("voiceFolderNames"))
		# Delete alert type
		self.audioPlaybackWhenDeleted = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Notify about deleting a message and chat with a sound")))
		self.audioPlaybackWhenDeleted.SetValue(conf.get("audioPlaybackWhenDeleted"))
		# Show confirmation window when deleting
		self.confirmation_at_deletion = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Display confirmation dialog when deleting messages and chats")))
		self.confirmation_at_deletion.SetValue(conf.get("confirmation_at_deletion"))
		# Type of notification when recording voice messages
		self.voiceMessageRecordingIndicator = settingsSizerHelper.addLabeledControl(_("Set voice message recording notification method as:"), wx.Choice, choices=[self.listVoiceMessageRecordingIndicator[item] for item in self.listVoiceMessageRecordingIndicator])
		self.voiceMessageRecordingIndicator.SetStringSelection(self.listVoiceMessageRecordingIndicator[conf.get("voiceMessageRecordingIndicator")])
		# Progress bar announce
		self.voicingPerformanceIndicators = settingsSizerHelper.addLabeledControl(_("Select the progress bar notification level:"), wx.Choice, choices=[self.listVoicingPerformanceIndicators[item] for item in self.listVoicingPerformanceIndicators])
		self.voicingPerformanceIndicators.SetStringSelection(self.listVoicingPerformanceIndicators[conf.get("voicingPerformanceIndicators")])
		# Processing messages containing links
		self.actionDescriptionForLinks = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Read description of URLs attached to messages")))
		self.actionDescriptionForLinks.SetValue(conf.get("actionDescriptionForLinks"))
		# Announcement of the full description of YouTube links
		self.voiceFullDescriptionOfLinkToYoutube = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Read full video description in YouTube URLs")))
		self.voiceFullDescriptionOfLinkToYoutube.SetValue(conf.get("voiceFullDescriptionOfLinkToYoutube"))
		# Report if the group has replies for you
		# self.isAnnouncesAnswers = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Announce if there is a reply in the group")))
		# self.isAnnouncesAnswers.SetValue(conf.get("isAnnouncesAnswers"))
		# Report information about premium and verified accounts
		# self.report_premium_accounts = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Announce premium and confirmed accounts")))
		# self.report_premium_accounts.SetValue(conf.get("report premium accounts"))
		# Report if the message contains a reaction
		self.voice_the_presence_of_a_reaction = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Announce if the message contains a reaction")))
		self.voice_the_presence_of_a_reaction.SetValue(conf.get("voice_the_presence_of_a_reaction"))
		# Fix toggle buttons for some users
		self.isFixedToggleButton = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Check this box if the voice message recording function or the voice message playback speed change function does not work properly")))
		self.isFixedToggleButton.SetValue(conf.get("isFixedToggleButton"))
		# Checking for Updates on NVDA Startup
		self.is_automatically_check_for_updates = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Check for UnigramPlus updates on NVDA startup")))
		self.is_automatically_check_for_updates.SetValue(conf.get("is_automatically_check_for_updates"))
		# Button to check for updates
		self.checkForUpdates = settingsSizerHelper.addItem(wx.Button(self, label=_("Check for &updates")))
		self.checkForUpdates.Bind(wx.EVT_BUTTON, onCheckForUpdates)

	def get_key(self, d, value):
		for k, v in d.items():
			if v == value: return k

	def onSave(self):
		conf.set("voiceTypeAfterChatName", self.get_key(self.listVoiceTypeAfterChatName, self.voiceTypeAfterChatName.GetStringSelection()))
		conf.set("saySenderName", self.get_key(self.listSaySenderName, self.saySenderName.GetStringSelection()))
		conf.set("unreadBeforeMessageContent", self.unreadBeforeMessageContent.IsChecked())
		conf.set("notify administrators in messages",
		         self.notify_administrators_in_messages.IsChecked())
		conf.set("voiceFolderNames", self.voiceFolderNames.IsChecked())
		conf.set("confirmation_at_deletion", self.confirmation_at_deletion.IsChecked())
		conf.set("audioPlaybackWhenDeleted", self.audioPlaybackWhenDeleted.IsChecked())
		conf.set("voiceMessageRecordingIndicator", self.get_key(self.listVoiceMessageRecordingIndicator, self.voiceMessageRecordingIndicator.GetStringSelection()))
		conf.set("voicingPerformanceIndicators", self.get_key(self.listVoicingPerformanceIndicators, self.voicingPerformanceIndicators.GetStringSelection()))
		conf.set("lang", self.get_key(listLanguages, self.lang.GetStringSelection()))
		conf.set("action_when_pressing_up_arrow_in_text_field", self.get_key(self.list_actions_when_pressing_up_arrow_in_text_field, self.action_when_pressing_up_arrow_in_text_field.GetStringSelection()))
		conf.set("actionDescriptionForLinks", self.actionDescriptionForLinks.IsChecked())
		conf.set("voiceFullDescriptionOfLinkToYoutube", self.voiceFullDescriptionOfLinkToYoutube.IsChecked())
		# conf.set("isAnnouncesAnswers", self.isAnnouncesAnswers.IsChecked())
		# conf.set("report premium accounts", self.report_premium_accounts.IsChecked())
		conf.set("voice_the_presence_of_a_reaction", self.voice_the_presence_of_a_reaction.IsChecked())
		conf.set("isFixedToggleButton", self.isFixedToggleButton.IsChecked())
		conf.set("is_automatically_check_for_updates", self.is_automatically_check_for_updates.IsChecked())
