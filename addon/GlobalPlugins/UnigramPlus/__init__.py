# -*- coding: utf-8 -*-
import globalPluginHandler
import globalVars
import addonHandler
from scriptHandler import script
import api
import gui
from gui.settingsDialogs import SettingsPanel
import wx
import urllib.request
import urllib.parse
import json
import core
import os
import re
addonHandler.initTranslation()
from logHandler import log
import threading
from appModules.cnf import conf, listLanguages
from appModules.unigram import baseDir
from ui import message

UPDATE_REPO = "keyang556/UnigramPlus"
UPDATE_API_URL = "https://api.github.com/repos/%s/releases/latest" % UPDATE_REPO

def _alert_dialog(text, caption, icon=wx.ICON_INFORMATION):
	# NVDA 2025.1 deprecated gui.messageBox in favour of MessageDialog.
	# Older NVDA versions have no MessageDialog, so they keep the message box.
	try:
		from gui.message import DialogType, MessageDialog
		from gui.guiHelper import wxCallOnMain
	except ImportError:
		gui.messageBox(text, caption, wx.OK | icon)
		return
	# MessageDialog.alert always shows a standard dialog. Build the same OK-only
	# dialog here so that a warning keeps its icon and sound.
	dialogType = DialogType.WARNING if icon == wx.ICON_WARNING else DialogType.STANDARD
	wxCallOnMain(lambda: MessageDialog(None, text, caption, dialogType).ShowModal())

def no_updates_dialog():
	_alert_dialog(_("No updates available"), _("UnigramPlus update"))

def _http_get(url, timeout=30):
	request = urllib.request.Request(url, headers={
		"User-Agent": "UnigramPlus-updater",
		"Accept": "application/vnd.github+json",
	})
	with urllib.request.urlopen(request, timeout=timeout) as response:
		return response.read()

def _parse_version(text):
	parts = []
	for piece in str(text).lstrip("vV").split("."):
		# Only take the leading digits of each segment, so a prerelease suffix
		# like "10-rc1" parses as 10, not as 101.
		match = re.match(r"\d+", piece)
		parts.append(int(match.group()) if match else 0)
	return tuple(parts) if parts else (0,)

def _addon_asset_url(release):
	# Only accept HTTPS download URLs served by GitHub itself, so a compromised
	# or spoofed API response can't redirect the installer to another host.
	for asset in release.get("assets") or ():
		name = str(asset.get("name") or "")
		url = str(asset.get("browser_download_url") or "")
		if not name.lower().endswith(".nvda-addon"):
			continue
		parsed = urllib.parse.urlsplit(url)
		host = (parsed.hostname or "").lower()
		if parsed.scheme == "https" and (host == "github.com" or host.endswith(".githubusercontent.com")):
			return url
	return None

def onCheckForUpdates(event = False, is_start = False):
	# Runs the network check on a background thread so a slow/unreachable
	# GitHub API doesn't freeze the NVDA UI, whether triggered at startup or
	# from the settings button.
	threading.Thread(target=_checkForUpdates, args=(is_start,), daemon=True).start()

def _checkForUpdates(is_start):
	addon_version = addonHandler.getCodeAddon().manifest["version"]
	try:
		release = json.loads(_http_get(UPDATE_API_URL).decode("utf-8"))
		str_last_version = str(release.get("tag_name") or "").lstrip("vV")
		url = _addon_asset_url(release)
	except Exception:
		log.debugWarning("UnigramPlus update check failed", exc_info=True)
		if not is_start: wx.CallAfter(no_updates_dialog)
		return
	if url and _parse_version(str_last_version) > _parse_version(addon_version):
		changelog = str(release.get("body") or "")
		wx.CallAfter(window_for_update, None, str_last_version, url, changelog)
	elif not is_start: wx.CallAfter(no_updates_dialog)


def openSoundFolder(event=False):
	try:
		os.startfile(os.path.normpath(baseDir))
	except Exception:
		message(_("Unable to open UnigramPlus sounds folder"))

class window_for_update(wx.Frame):
	def __init__(self, parent, str_last_version, url, changelog=""):
		title = _("UnigramPlus update")
		text = _("A new version of the add-on is available. Do you want to update UnigramPlus to version %version?").replace("%version", str_last_version)
		if changelog: text += "\n"+_("Changes in this version:")+"\n"+changelog
		else: text += "\n"+_("No update information")
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

	def download_update(self, event):
		self.text.SetValue(_("Download in progress"))
		self.text.SetFocus()
		self.button_ok.Disable()
		self.button_close.Disable()
		threading.Thread(target=self._download, daemon=True).start()

	def _download(self):
		try:
			response_addon = _http_get(self.url, timeout=120)
		except Exception:
			log.error("UnigramPlus update download failed", exc_info=True)
			wx.CallAfter(self._download_failed)
			return
		fp = os.path.join(globalVars.appArgs.configPath, "unigramplus.nvda-addon")
		try:
			with open(fp, 'wb') as addon:
				addon.write(response_addon)
		except Exception:
			log.error("Could not save the UnigramPlus update bundle", exc_info=True)
			wx.CallAfter(self._download_failed)
			return
		wx.CallAfter(self.setup_update, fp)

	def _download_failed(self):
		no_updates_dialog()
		self.Close()

	def window_close(self, event):
		self.Close()

	def setup_update(self, fp):
		try:
			bundle = addonHandler.AddonBundle(fp)
			bundleName = bundle.manifest['name']
			# Refuse bundles that aren't this add-on or that target a newer NVDA.
			if bundleName != addonHandler.getCodeAddon().manifest['name']:
				raise ValueError("Downloaded bundle %r does not match this add-on" % bundleName)
			try:
				from addonHandler import addonVersionCheck
				compatible = addonVersionCheck.isAddonCompatible(bundle)
			except ImportError:
				compatible = True
			if not compatible:
				_alert_dialog(
					_("The new version of UnigramPlus is not compatible with this version of NVDA. Please update NVDA first."),
					_("UnigramPlus update"),
					wx.ICON_WARNING)
				self.Close()
				return
		except Exception:
			log.error("The downloaded UnigramPlus update bundle failed validation", exc_info=True)
			try: os.remove(fp)
			except OSError: pass
			self._download_failed()
			return
		curAddons = addonHandler.getAvailableAddons()
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
		if conf.get("is_automatically_check_for_updates") and not globalVars.appArgs.secure:
			onCheckForUpdates(False, True)

	@script(description=_("Open UnigramPlus settings window"), gesture="kb:NVDA+ALT+U")
	def script_open_settings_dialog(self, gesture, arg = False):
		# popupSettingsDialog is public since NVDA 2023.2; the underscore name is
		# deprecated, so it is only the fallback for older versions.
		popup = getattr(gui.mainFrame, "popupSettingsDialog", None) or gui.mainFrame._popupSettingsDialog
		wx.CallAfter(popup, gui.settingsDialogs.NVDASettingsDialog, UnigramPlusSettings)

	# Call answer
	@script(description=_("Accept call"), gesture="kb:ALT+Y")
	def script_answeringCall(self, gesture):
		gesture.send()
		desctop = api.getDesktopObject()
		notification = next((item.firstChild.firstChild for item in desctop.children if item.firstChild and hasattr(item.firstChild, "UIAAutomationId") and item.firstChild.UIAAutomationId == "ToastCenterScrollViewer"), False)
		if not notification:
			return
		button = next((item for item in notification.children if item.UIAAutomationId == "VerbButton"), None)
		if button: button.doAction()

	# End a call, decline call, or leave a voice chat
	@script(description=_("Press \"Decline call\" button  if there is an incoming call, \"End call\" button if a call is in progress or leave voice chat if it is active."), gesture="kb:ALT+N")
	def script_callCancellation(self, gesture):
		gesture.send()
		desctop = api.getDesktopObject()
		notification = next((item.firstChild.firstChild for item in desctop.children if item.firstChild and hasattr(item.firstChild, "UIAAutomationId") and item.firstChild.UIAAutomationId == "ToastCenterScrollViewer"), False)
		if not notification:
			# No incoming-call toast: hand off to the app module to end an ongoing call or leave
			# a voice chat. Use the live instance so its helper methods resolve correctly.
			appMod = getattr(api.getFocusObject(), "appModule", None)
			if appMod is not None and hasattr(appMod, "script_callCancellation"):
				appMod.script_callCancellation(gesture)
			return
		button = next((item.next for item in notification.children if item.UIAAutomationId == "VerbButton"), None)
		if button:
			button.doAction()
			return
		


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
		"upload_download": _("Only announce progress bars during file uploads and downloads"),
		"none": _("Do not announce any progress bars"),
		# "normal": _("Announce some progress bars")
	}
	listSaySenderName = {
		"none": _("Do not say at all"),
		"sent": _("Only in sent messages"),
		"received": _("Only in received messages"),
		"all": _("In all messages")
	}
	listVoiceRecordingButtonLabel = {
		"withElapsedTime": _("Say \"Recording a voice message\" and the elapsed time"),
		"labelOnly": _("Say \"Recording a voice message\" without the elapsed time"),
		"none": _("Like version 5.4: keep the focus in the message field and never announce the button"),
	}
	list_actions_when_pressing_up_arrow_in_text_field = {
		"block": _("Do nothing"),
		"normal": _("Activate editing of last sent message"),
		"to_messages": _("Move focus to the last message in a chat"),
		"to_last_focused_message": _("Move focus to the last focused message in a chat"),
	}
	
	def makeSettings(self, settingsSizer):
		settingsSizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Selecting an interface language
		# self.lang = settingsSizerHelper.addLabeledControl(_("Interface language in Unigram:"), wx.Choice, choices=[listLanguages[item] for item in listLanguages])
		self.lang = settingsSizerHelper.addLabeledControl(_("Interface language in Unigram:"), wx.Choice, choices=list(listLanguages.values()))
		self.lang.SetStringSelection(listLanguages[conf.get("lang")])
		# Move focus to the chat list after Unigram's main UI finishes loading
		self.autoFocusChatList = settingsSizerHelper.addItem(
			wx.CheckBox(self, label=_("Automatically move focus to the chat list when Unigram starts"))
		)
		self.autoFocusChatList.SetValue(conf.get("autoFocusChatList"))
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
		# Alt+[ toggles this setting directly; expose the persistent default-off
		# behavior in settings as well so it can be selected without the shortcut.
		self.messageHeaderAtTheEnd = settingsSizerHelper.addItem(wx.CheckBox(
			self, label=_("Announce message headers after the message content")))
		self.messageHeaderAtTheEnd.SetValue(conf.get("messageHeaderAtTheEnd"))
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
		# Type of notification when a voice message recording starts or is sent.
		# Unigram 13.0 announces a canceled recording itself.
		self.voiceMessageRecordingIndicator = settingsSizerHelper.addLabeledControl(_("Notification when a voice message recording starts or is sent:"), wx.Choice, choices=[self.listVoiceMessageRecordingIndicator[item] for item in self.listVoiceMessageRecordingIndicator])
		self.voiceMessageRecordingIndicator.SetStringSelection(self.listVoiceMessageRecordingIndicator[conf.get("voiceMessageRecordingIndicator")])
		# Progress bar announce
		self.voicingPerformanceIndicators = settingsSizerHelper.addLabeledControl(_("Select the progress bar notification level:"), wx.Choice, choices=[self.listVoicingPerformanceIndicators[item] for item in self.listVoicingPerformanceIndicators])
		self.voicingPerformanceIndicators.SetStringSelection(self.listVoicingPerformanceIndicators[conf.get("voicingPerformanceIndicators")])
		self.fileTransferProgressInterval = settingsSizerHelper.addLabeledControl(
			_("File transfer progress announcement interval (percent):"), wx.SpinCtrl, min=1, max=100)
		self.fileTransferProgressInterval.SetValue(conf.get("fileTransferProgressInterval"))
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
		# Play an audible notification when navigating past the final message in a chat
		self.play_end_of_chat_sound = settingsSizerHelper.addItem(wx.CheckBox(
			self, label=_("Play a sound when reaching the end of a chat")))
		self.play_end_of_chat_sound.SetValue(conf.get("play_end_of_chat_sound"))
		# Play looped Typing.wav while the other side is typing/recording in the open chat
		self.play_typing_sound = settingsSizerHelper.addItem(wx.CheckBox(self, label=_("Play a sound while the other side is typing in the open chat")))
		self.play_typing_sound.SetValue(conf.get("play_typing_sound"))
		# Everything below was added after version 5.4. Group it under one heading so
		# it is easy to find, and let each item be turned off to get 5.4 back.
		newFeaturesSizer = wx.StaticBoxSizer(
			wx.VERTICAL, self,
			label=_("Behavior added after version 5.4 (uncheck an item to use the version 5.4 behavior)"))
		newFeaturesBox = newFeaturesSizer.GetStaticBox()
		newFeaturesHelper = settingsSizerHelper.addItem(
			gui.guiHelper.BoxSizerHelper(self, sizer=newFeaturesSizer))
		# How the record button itself is announced (added in 5.5.7)
		self.voiceRecordingButtonLabel = newFeaturesHelper.addLabeledControl(
			_("When the focus is on the voice message record button, announce it as:"), wx.Choice,
			choices=list(self.listVoiceRecordingButtonLabel.values()))
		self.voiceRecordingButtonLabel.SetStringSelection(
			self.listVoiceRecordingButtonLabel[conf.get("voiceRecordingButtonLabel")])
		# Announce rich messages and open their text with ALT+C (added in 5.5.9)
		self.richMessageSupport = newFeaturesHelper.addItem(wx.CheckBox(
			newFeaturesBox, label=_(
				"Read the full text of rich messages with ALT+C. "
				"When unchecked, ALT+C works like version 5.4 and shows only the plain message text")))
		self.richMessageSupport.SetValue(conf.get("richMessageSupport"))
		# Name the profile identity button after the chat (added in 5.5.6)
		self.labelProfileIdentityButton = newFeaturesHelper.addItem(wx.CheckBox(
			newFeaturesBox, label=_(
				"In a group or channel profile, announce the chat name and member count instead of "
				"\"Identity root\" when tabbing past the name. When unchecked, version 5.4 behavior is used "
				"and the button is announced as \"Identity root\"")))
		self.labelProfileIdentityButton.SetValue(conf.get("labelProfileIdentityButton"))
		# Say "Reply"/"Editing" in the message field (added in 5.5.5)
		self.announceComposerState = newFeaturesHelper.addItem(wx.CheckBox(
			newFeaturesBox, label=_(
				"Announce \"Reply\" or \"Editing\" in the message edit field when a message is being "
				"replied to or edited. When unchecked, version 5.4 behavior is used and the usual "
				"message prompt is announced instead")))
		self.announceComposerState.SetValue(conf.get("announceComposerState"))
		# Suppress the transient "list" announcement before a message (added in 5.6.3)
		self.suppressMessagesListAnnouncement = newFeaturesHelper.addItem(wx.CheckBox(
			newFeaturesBox, label=_(
				'Do not announce "list" before a message when moving through a chat with the arrow keys. '
				'When unchecked, version 5.4 behavior is used and NVDA announces the message list as usual')))
		self.suppressMessagesListAnnouncement.SetValue(conf.get("suppressMessagesListAnnouncement"))
		# Live state of the call Mute and Camera toggles (added in 5.5.8)
		self.announceCallControlState = newFeaturesHelper.addItem(wx.CheckBox(
			newFeaturesBox, label=_(
				"During a call, announce whether the microphone and camera are currently on or off. "
				"When unchecked, version 5.4 behavior is used and Unigram's own fixed button names are announced")))
		self.announceCallControlState.SetValue(conf.get("announceCallControlState"))
		# Unread count when switching chat folders (added in 5.7.0)
		self.announceFolderUnreadCount = newFeaturesHelper.addItem(wx.CheckBox(
			newFeaturesBox, label=_(
				"When switching between chat folders, announce the number of unread chats after the folder name. "
				"When unchecked, version 5.4 behavior is used and only the folder name is announced")))
		self.announceFolderUnreadCount.SetValue(conf.get("announceFolderUnreadCount"))
		# Button to open the bundled sounds folder
		self.openSoundsFolder = settingsSizerHelper.addItem(wx.Button(self, label=_("Open UnigramPlus sounds folder")))
		self.openSoundsFolder.Bind(wx.EVT_BUTTON, openSoundFolder)
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
		conf.set("autoFocusChatList", self.autoFocusChatList.IsChecked())
		conf.set("saySenderName", self.get_key(self.listSaySenderName, self.saySenderName.GetStringSelection()))
		conf.set("unreadBeforeMessageContent", self.unreadBeforeMessageContent.IsChecked())
		conf.set("messageHeaderAtTheEnd", self.messageHeaderAtTheEnd.IsChecked())
		conf.set("notify administrators in messages",
		         self.notify_administrators_in_messages.IsChecked())
		conf.set("voiceFolderNames", self.voiceFolderNames.IsChecked())
		conf.set("confirmation_at_deletion", self.confirmation_at_deletion.IsChecked())
		conf.set("audioPlaybackWhenDeleted", self.audioPlaybackWhenDeleted.IsChecked())
		conf.set("voiceMessageRecordingIndicator", self.get_key(self.listVoiceMessageRecordingIndicator, self.voiceMessageRecordingIndicator.GetStringSelection()))
		conf.set("voicingPerformanceIndicators", self.get_key(self.listVoicingPerformanceIndicators, self.voicingPerformanceIndicators.GetStringSelection()))
		conf.set("fileTransferProgressInterval", self.fileTransferProgressInterval.GetValue())
		conf.set("lang", self.get_key(listLanguages, self.lang.GetStringSelection()))
		conf.set("action_when_pressing_up_arrow_in_text_field", self.get_key(self.list_actions_when_pressing_up_arrow_in_text_field, self.action_when_pressing_up_arrow_in_text_field.GetStringSelection()))
		conf.set("actionDescriptionForLinks", self.actionDescriptionForLinks.IsChecked())
		conf.set("voiceFullDescriptionOfLinkToYoutube", self.voiceFullDescriptionOfLinkToYoutube.IsChecked())
		# conf.set("isAnnouncesAnswers", self.isAnnouncesAnswers.IsChecked())
		# conf.set("report premium accounts", self.report_premium_accounts.IsChecked())
		conf.set("voice_the_presence_of_a_reaction", self.voice_the_presence_of_a_reaction.IsChecked())
		conf.set("isFixedToggleButton", self.isFixedToggleButton.IsChecked())
		conf.set("play_end_of_chat_sound", self.play_end_of_chat_sound.IsChecked())
		conf.set("play_typing_sound", self.play_typing_sound.IsChecked())
		conf.set("is_automatically_check_for_updates", self.is_automatically_check_for_updates.IsChecked())
		conf.set("voiceRecordingButtonLabel", self.get_key(self.listVoiceRecordingButtonLabel, self.voiceRecordingButtonLabel.GetStringSelection()))
		conf.set("richMessageSupport", self.richMessageSupport.IsChecked())
		conf.set("labelProfileIdentityButton", self.labelProfileIdentityButton.IsChecked())
		conf.set("announceComposerState", self.announceComposerState.IsChecked())
		conf.set("suppressMessagesListAnnouncement", self.suppressMessagesListAnnouncement.IsChecked())
		conf.set("announceCallControlState", self.announceCallControlState.IsChecked())
		conf.set("announceFolderUnreadCount", self.announceFolderUnreadCount.IsChecked())
		# Sync the typing-sound tracker with the new setting
		try:
			from appModules.unigram import Typing_sound_tracking
			if self.play_typing_sound.IsChecked():
				# Will resume on the next focus event in Unigram; nothing to do here.
				Typing_sound_tracking.pouse = True
			else:
				Typing_sound_tracking.active = False
				Typing_sound_tracking.stop_sound()
		except Exception: pass
		# Sync the file-transfer progress tracker with the new progress-bar setting
		try:
			from appModules.unigram import File_transfer_progress_tracking
			if conf.get("voicingPerformanceIndicators") == "none":
				File_transfer_progress_tracking.stop()
			elif not File_transfer_progress_tracking.active:
				File_transfer_progress_tracking.start()
		except Exception: pass
