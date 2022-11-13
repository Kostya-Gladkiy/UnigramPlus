# -*- coding:utf-8 -*-
import winUser
import mouseHandler
from keyboardHandler import KeyboardInputGesture
import appModuleHandler
from ui import message, browseableMessage
import api
import controlTypes
import scriptHandler
from scriptHandler import script
from NVDAObjects.UIA import UIA
import languageHandler
import addonHandler
addonHandler.initTranslation()
import speech
from  threading import Timer
import time
import winsound
from nvwave import playWaveFile
import os
from logHandler import log
import queueHandler
import sys
import re
sys.path.insert(0, ".")
from .data import *
from .text_window import *
from .cnf import conf, lang

baseDir = os.path.join(os.path.dirname(__file__), "media\\")


class Audio_and_video_button:
	def script_enter(self, gesture):
		gesture.send()
		if self.UIAAutomationId == "Audio": new_name = self.next.next.name if self.next.next else self.name
		elif self.UIAAutomationId == "Video": new_name = _("Camera on") if self.firstChild.name == "\ue964" else _("Camera off") if self.firstChild.name == "\ue963" else self.name
		def spechState(): message(new_name)
		thr = Timer(.1, spechState).start()
		# if self.UIAAutomationId == "Audio": self.action_audio_button()
		# elif self.UIAAutomationId == "Video": self.action_video_button()
	def initOverlayClass(self):
		self.bindGesture("kb:Enter", "enter")
		# self.bindGesture("kb:space", "enter")


class Message_list_item:
	role = controlTypes.Role.LISTITEM
	UIAAutomationId = "Message_item"
	scriptCategory = "UnigramPlus"
	def script_fixed_down_arrow(self, gesture):
		self.appModule.keys["fixed_downArrow"].send()
	
	@script(description=_("Announce the original message, the message that was replied to"), gesture="kb:rightArrow")
	def script_voice_answer(self, gesture):
		answer = next((item for item in self.children if item.UIAAutomationId == "Reply"), None)
		if answer: message(answer.name)

	@script(description=_("Edit message"), gesture="kb:backspace")
	def script_edit_message(self, gesture):
		self.appModule.activate_option_for_menu((icons_from_context_menu["edit"]), "Messages")
	
	@script(description=_("Reply to message"), gesture="kb:enter")
	def script_reply_to_message(self, gesture):
		self.appModule.activate_option_for_menu((icons_from_context_menu["reply"]), "Messages")

	def initOverlayClass(self):
		if self.appModule.app_version == "8.8.7438.0": self.bindGesture("kb:downArrow", "fixed_down_arrow")
		self.positionInfo = self.parent.positionInfo
		self.states.discard(controlTypes.State.CHECKABLE)

	__gestures = {
		"kb:leftArrow": "voice_answer",
		"kb:backspace": "edit_message",
		"kb:enter": "reply_to_message",
	}


class Tab_folder_item:
	def script_next_tab(self, gesture):
		KeyboardInputGesture.fromName("control+rightArrow").send()
		# if self.parent.UIAAutomationId == "ChatFilters": KeyboardInputGesture.fromName("control+rightArrow").send()
		# else: KeyboardInputGesture.fromName("control+downArrow").send()
	def script_previous_tab(self, gesture):
		KeyboardInputGesture.fromName("control+leftArrow").send()
		# if self.parent.UIAAutomationId == "ChatFilters": KeyboardInputGesture.fromName("control+leftArrow").send()
		# else: KeyboardInputGesture.fromName("control+upArrow").send()
	__gestures = {
		"kb:rightArrow": "next_tab",
		"kb:downArrow": "next_tab",
		"kb:leftArrow": "previous_tab",
		"kb:upArrow": "previous_tab",
	}
	# def initOverlayClass(self):
	# pass


class Saved_items:
	# Зберігаємо деякі елементи вікна в пам'ять, до яких часто потрібно звертатись, щоб доступ до них відбувався швидше
	_items = {}
	def get(self, key):
		id = api.getFocusObject().windowHandle
		try: return self._items[id][key]
		except: return False
	def save(self, key, obj):
		# id = obj.windowHandle
		id = api.getFocusObject().windowHandle
		if id not in self._items: self._items[id] = {}
		self._items[id][key] = obj

class Title_change_tracking:
	active = False
	interval = .5
	saved_items = False
	def tick():
		if not Title_change_tracking.active: return
		title = Title_change_tracking.saved_items.get("profile name")
		last_profile_name = Title_change_tracking.saved_items.get("last profile name") or ("q",)
		if title and title.childCount > 1 and title.lastChild.name != last_profile_name[-1]:
			if title.firstChild.name == last_profile_name[0]:
				# ОЗвучуємо зміни тільки в тому випадку, коли ці зміни не пов'язані з переходом до іншого чату
				text = title.name
				queueHandler.queueFunction(queueHandler.eventQueue, message, text)
			new_title = [item.name for item in title.children]
			Title_change_tracking.saved_items.save("last profile name", new_title)
		Timer(Title_change_tracking.interval, Title_change_tracking.tick).start()
	def toggle(saved_items=False):
		if not Title_change_tracking.active or not saved_items:
			Title_change_tracking.saved_items = saved_items
			Timer(Title_change_tracking.interval, Title_change_tracking.tick).start()
			Title_change_tracking.active = True
			return True
		else:
			Title_change_tracking.active = False
			return False

class Chat_update:
	active = False
	interval = .3
	app = False
	def tick():
		if not Chat_update.active: return
		try : last_message = Chat_update.app.getMessagesElement().lastChild
		except: last_message = False
		# Перший елемент це назва чату, в якому було зафіксовано останнє повідомлення
		# Другий елемент це індекс повідомлення
		last_saved_message = Chat_update.app.saved_items.get("last message") or ("", "")
		# {'indexInGroup': 2, 'similarItemsInGroup': 20}
		# Якщо є проблеми з отриманням індекса повідомлення, тоді ми завершуємо функцію і викликаємо наступну ітерацію
		try:
			last_message.positionInfo["indexInGroup"]
			last_message.positionInfo["similarItemsInGroup"]
		except:
			Timer(Chat_update.interval, Chat_update.tick).start()
			return
		if last_message and last_message.positionInfo["indexInGroup"] != last_saved_message[1] and last_message.positionInfo["indexInGroup"] == last_message.positionInfo["similarItemsInGroup"]:
			try:
				title = Chat_update.app.saved_items.get("profile name").firstChild.name
			except:
				title = False
			keywords = keywordsInMessages.get(conf.get("lang"), keywordsInMessages["en"])
			if ((title == last_saved_message[0]) or not title) and keywords[3] in last_message.name[-60:]:
				text = Chat_update.app.action_message_focus(last_message)
				queueHandler.queueFunction(queueHandler.eventQueue, message, text)
			try:
				new_message = (title, last_message.positionInfo["indexInGroup"])
				Chat_update.app.saved_items.save("last message", new_message)
			except: pass
		Timer(Chat_update.interval, Chat_update.tick).start()
	def toggle(app=False):
		if not Chat_update.active or not app:
			Chat_update.active = True
			Chat_update.app = app
			Timer(Chat_update.interval, Chat_update.tick).start()
			return True
		else:
			Chat_update.active = False
			return False

class AppModule(appModuleHandler.AppModule):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.app_version = self.productVersion
		self.saved_items = Saved_items()
		# призначаємо гарячі клавіші для функції прочитування повідомлення за порядковим номером
		for i in range(10): self.bindGesture("kb:NVDA+control+%d" % i, "reviewRecentMessage")
		# ВПрив'язуємо реакції до відповідних гарячих клавіш
		# for i in range(1,6): self.bindGesture("kb:NVDA+ALT+%d" % i, "set_reaction")


	scriptCategory = "UnigramPlus"
	lastSavedMessage = False
	profile_panel_element = False
	isDelete = False
	isOpenProfile = False
	isSkipName = 0
	isRecord = False
	execute_context_menu_option = False
	scheduledMessages = []
	is_set_reaction = False
	keys = {
		"upArrow": KeyboardInputGesture.fromName("upArrow"),
		"downArrow": KeyboardInputGesture.fromName("downArrow"),
		"fixed_downArrow": KeyboardInputGesture.fromName("shift+downArrow"),
		"Applications": KeyboardInputGesture.fromName("Applications"),
		"escape": KeyboardInputGesture.fromName("escape"),
	}


	def getMessagesElement(self):
		obj = self.saved_items.get("messages")
		if not obj or not obj.location or not obj.location.width:
			obj = next((item for item in self.getElements() if item.UIAAutomationId == "Messages"), False)
			if obj: self.saved_items.save("messages", obj)
		return obj

	def getChatsListElement(self):
		targetList = self.saved_items.get("chats")
		if not targetList or not targetList.location or not targetList.location.width:
			targetList = next((item for item in reversed(self.getElements()) if item.role == controlTypes.Role.TABCONTROL and item.UIAAutomationId == "rpMasterTitlebar"), False)
			if not targetList: return False
			targetList = next((item for item in targetList.firstChild.children if item.role == controlTypes.Role.LIST and 	item.UIAAutomationId == "ChatsList"), False)
			if targetList: self.saved_items.save("chats", targetList)
		return targetList

	def getElements(self):
		try: return api.getForegroundObject().lastChild.previous.children
		except: return []

	def is_message_object(self, obj):
		try:
			if obj.UIAAutomationId == "Message_item": return True
			else: return False
		except: return False

	# Функція прискорення голосового повідомлення
	@script(description=_("Increase/decrease the playback speed of voice messages"), gesture="kb:ALT+S")
	def script_voiceMessageAcceleration(self, gesture):
		targetButton = next((item for item in self.getElements() if item.role == controlTypes.Role.TOGGLEBUTTON and item.UIAAutomationId == "RateButton"), False)
		if targetButton:
			lastFocus = api.getFocusObject()
			if not conf.get("isFixedToggleButton"): targetButton.doAction()
			else: self.fixedDoAction(targetButton)
			lastFocus.setFocus()
		else: message(_("Nothing is playing right now"))

	# Функція закриття аудіопрогравача
	@script(description=_("Close audio player"), gesture="kb:ALT+E")
	def script_closingVoiceMessage(self, gesture, isMessage = True):
		try: targetButton = next((item for item in self.getElements()[1:] if item.previous.role == controlTypes.Role.TOGGLEBUTTON and item.previous.UIAAutomationId == "ShuffleButton"), False)
		except: targetButton = False
		if targetButton:
			lastFocus = api.getFocusObject()
			targetButton.doAction()
			lastFocus.setFocus()
			message(_("The audio player has been closed"))
		else: message(_("Nothing is playing right now"))

	# Функція призупинення голосового повідомлення
	@script(description=_("Play/pause the voice message currently playing"), gesture="kb:ALT+P")
	def script_pauseVoiceMessage(self, gesture):
		targetButton = next((item for item in self.getElements() if item.role == controlTypes.Role.BUTTON and item.UIAAutomationId == "PlaybackButton"), False)
		if targetButton:
			lastFocus = api.getFocusObject()
			targetButton.doAction()
			lastFocus.setFocus()
		else: message(_("Nothing is playing right now"))

	# Відтворення і відкриття медіа клавішою пробіл
	# @script(description=_("Play/stop the focused voice or video message, or open a media file attached to the current message"), gesture="kb:space")
	def script_actionMediaInMessage(self, gesture):
		lastFocus = api.getFocusObject()
		obj = lastFocus
		isSavedFocus = True
		if self.is_message_object(obj.parent):
			obj = obj.parent
			isSavedFocus = False
		message_states = obj.states
		gesture.send()
		if not self.is_message_object(obj): return
		lastFocus.location
		actionButton = False
		def spechState():
			if obj.states != message_states: return
			targetButton = next((item for item in obj.children if item.role == controlTypes.Role.LINK and item.UIAAutomationId == "Button"), False)
			if not targetButton: return
			if (targetButton.previous and targetButton.previous.role == controlTypes.Role.GRAPHIC) or (targetButton.previous and targetButton.previous.previous and targetButton.previous.previous.role == controlTypes.Role.GRAPHIC): actionButton = "save"
			else: actionButton = "focus"
			if isSavedFocus: targetButton.doAction()
			if actionButton == "focus": lastFocus.setFocus()
			elif actionButton == "save": self.lastSavedMessage = {"obj": lastFocus}
		thr = Timer(.1, spechState).start()

	# Перейти до списку чатів
	@script(description=_("Move focus to chat list"), gesture="kb:ALT+1")
	def script_toChatList(self, gesture, arg = False):
		obj = api.getFocusObject()
		lastFocusChatElement = self.saved_items.get("last focused chat")
		lastFocusSelectedChatElement = self.saved_items.get("last selected chat")
		if lastFocusSelectedChatElement and lastFocusSelectedChatElement.location and lastFocusSelectedChatElement.location.width:
			if obj == lastFocusSelectedChatElement: message(obj.name)
			else: lastFocusSelectedChatElement.setFocus()
			return
		if lastFocusChatElement and lastFocusChatElement.location and lastFocusChatElement.location.width:
			if obj == lastFocusChatElement: message(obj.name)
			else: lastFocusChatElement.setFocus()
			return
		try: targetList = self.getChatsListElement()
		except: targetList = None
		if not targetList:
			if not arg: message(_("Chat list not found"))
			return
		if targetList.firstChild:
			targetList = targetList.firstChild
			if targetList.role == controlTypes.Role.BUTTON and targetList.next: targetList =  targetList.next
			if targetList.role and targetList.role == controlTypes.Role.LISTITEM:
				targetList.setFocus()
				return
		if not arg: message(_("Chat list is empty"))

	# Перейти до останнього повідомлення в чаті
	@script(description=_("Move focus to the last message in an open chat"), gesture="kb:ALT+2")
	def script_toLastMessage(self, gesture):
		focusObj = api.getFocusObject()
		if self.is_message_object(focusObj):
			if focusObj.parent.next: KeyboardInputGesture.fromName("end").send()
			else: message(focusObj.name)
			return True
		obj = self.getMessagesElement()
		try:
			obj.lastChild.setFocus()
			KeyboardInputGesture.fromName("end").send()
		except:
			if obj and not obj.lastChild: message(_("This chat is empty"))
			else: message(_("No open chat"))

	# Перенести фокус до списку папок чатів 
	@script(description=_("Move focus to list of chat folders"), gesture="kb:ALT+4")
	def script_to_tabs_folder(self, gesture):
		obj = self.saved_items.get("tabs folder")
		if obj and obj.location and obj.location.width:
			el = next((item for item in self.tabs_folder_element.children if controlTypes.State.SELECTED in item.states), None)
			if el: el.setFocus()
			else: message(_("Chat folder list not found"))
		else:
			list = self.getChatsListElement()
			if list:
				obj = list.previous
				self.saved_items.save("tabs folder", obj)
				el = next((item for item in obj.children if controlTypes.State.SELECTED in item.states), None)
				if el: el.setFocus()
				else: message(_("Chat folder list not found"))
			else: message(_("Chat folder list not found"))

	# Перенести фокус до відкритого профілю
	@script(description=_("Move focus to open profile"), gesture="kb:ALT+5")
	def script_to_open_prifile(self, gesture):
		list = self.profile_panel_element
		if not list or not list.location.width:
			# list = next((item for item in self.getElements() if item.role == controlTypes.Role.LIST and item.UIAAutomationId == "ScrollingHost" and item.firstChild.UIAAutomationId == "Photo"), None)
			list = next((item for item in self.getElements() if (item.role == controlTypes.Role.LIST and item.UIAAutomationId == "ScrollingHost" and item.firstChild.UIAAutomationId == "Photo") or (item.role == controlTypes.Role.LINK and item.UIAAutomationId == "Photo" and item.next.UIAAutomationId == "Title")), None)
		if not list:
			message(_("There is no open profile"))
			return
		if list.UIAAutomationId == "Photo":
			# Якщо профіль не містить жодної вкладки, тоді фокус встановлюємо на фото профілю
			list.setFocus()
			return
		self.profile_panel_element = list
		list2 = list.firstChild
		for i in range(15):
			if list2.role == controlTypes.Role.LIST:
				# Тепер знайдемо виділений елемент, щоб саме на нього встановити фокус
				next((item for item in list2.children if controlTypes.State.SELECTED in item.states), list2.firstChild).setFocus()
				return True
			else: list2 = list2.next
		list.firstChild.setFocus()	

	# Озвучує назву і статус профілю, в відкритому чаті
	@script(description=_("Announce the name and status of an open chat"), gesture="kb:ALT+T")
	def script_read_prifile_name(self, gesture):
		if scriptHandler.getLastScriptRepeatCount() == 1:
			if Title_change_tracking.toggle(self.saved_items): message(_("Chat activity tracking is enabled"))
			else: message(_("Chat activity tracking is disabled"))
			return
		isGroupCall = False
		title = False
		obj = self.saved_items.get("profile name")
		if obj and obj.location.width != 0:
			title = obj
			message(obj.name)
		for item in self.getElements():
			if not title and item.role == controlTypes.Role.LINK and item.UIAAutomationId == "Profile":
				message(item.name)
				title = item
			elif item.role == controlTypes.Role.LINK and item.UIAAutomationId == "GroupCall": isGroupCall = item.firstChild.name
		if title:
			self.saved_items.save("profile name", title)
			if isGroupCall: message(isGroupCall)
		else: message(_("No open chat"))

	# Перейти до мітки "непрочитані повідомлення"
	@script(description=_("Move focus to 'unread messages' label"), gesture="kb:ALT+3")
	def script_goToTheLastUnreadMessage(self, gesture):
		messages = self.getMessagesElement()
		try: lastObj = messages.lastChild
		except:
			if not messages: message(_("No open chat"))
			elif not messages.lastChild: message(_("This chat is empty"))
			return False
		targetButton = False
		while lastObj:
			if lastObj.firstChild.role== controlTypes.Role.GROUPING:
				targetButton = lastObj
				break
			else: lastObj = lastObj.previous
		if targetButton: targetButton.setFocus()
		else: message(_("There are no unread messages in this chat"))

	# Зателефонувати якщо це контакт, або увійти до голосового чату, якщо це група
	@script(description=_("Call if it's a contact, or enter a voice chat if it's a group"), gesture="kb:shift+alt+C")
	def script_call(self, gesture):
		try: targetButton = next((item for item in self.getElements() if (item.role == controlTypes.Role.BUTTON and item.UIAAutomationId == "Call") or (item.role == controlTypes.Role.LINK and item.UIAAutomationId == "GroupCall") or (item.next and item.next.UIAAutomationId == "Audio" and item.firstChild and item.firstChild.UIAAutomationId == "TitleInfo") ), False)
		except: targetButton =False
		if targetButton: targetButton.doAction()
		else: message(_("Call unavailable"))

	# Зателефонувати по відеозв'язку якщо це контакт
	@script(description=_("Press the video call button"), gesture="kb:shift+alt+V")
	def script_videoCall(self, gesture):
		targetButton = next((item for item in self.getElements() if item.role == controlTypes.Role.BUTTON and item.UIAAutomationId == "VideoCall"), False)
		if targetButton: targetButton.doAction()
		else: message(_("Video call not available"))

	# Функція відкриття миттєвого перегляду статті
	@script(description=_("Press \"Instant view\" button, if it is included in the current message"), gesture="kb:ALT+Q")
	def script_instantIew(self, gesture):
		obj = api.getFocusObject()
		if not self.is_message_object(obj): return
		targetButton = next((item for item in obj.children if item.role == controlTypes.Role.BUTTON and item.UIAAutomationId == "Button"), False)
		if targetButton:
			targetButton.doAction()
			targetList = next((item for item in self.getElements() if item.role == controlTypes.Role.LIST and item.UIAAutomationId == "ScrollingHost"), False)
			if targetList:
				item = next((item for item in targetList.children if item.name != ""), None)
				if item: item.setFocus()
		else: message(_("Button not found"))

	# Відповідь на дзвінок
	@script(description=_("Accept call"), gesture="kb:ALT+Y")
	def script_answeringCall(self, gesture):
		targetButton = next((item for item in self.getElements() if item.role == controlTypes.Role.BUTTON and item.UIAAutomationId == "Accept" and item.previous.UIAAutomationId == "Discard"), False)
		if targetButton:
			lastFocus = api.getFocusObject()
			self.fixedDoAction(targetButton)
			lastFocus.setFocus()

	# Завершити дзвінок, відхилити дзвінок, або покинути голосовий чат
	@script(description=_("Press \"Decline call\" button  if there is an incoming call, \"End call\" button if a call is in progress or leave voice chat if it is active."), gesture="kb:ALT+N")
	def script_callCancellation(self, gesture):
		# Перша первірка стосується ситуації, коли дзвінок вже триває
		# Друга перевірка стосується ситуації, коли користувач хоче покинути голосовий чат, перебуваючи у вікні голосового чату
		# Третя перевірка стосується ситуації, коли вхідний дзвінок
		# Четверта перевірка стосується ситуації, коли користувач хоче покинути голосовий чат, перебуваючи в оновному вікні програми, а не у вікні голосового чату
		targetButton = next((item for item in self.getElements()[1:] if (item.UIAAutomationId == "Accept" and item.previous.UIAAutomationId == "Audio") or (item.UIAAutomationId == "Leave" and item.firstChild.name == "\ue711") or (item.UIAAutomationId == "Discard" and item.next.UIAAutomationId == "Accept") or (item.previous.UIAAutomationId == "Audio" and item.firstChild.name == "\ue711")), False)
		if targetButton:
			lastFocus = api.getFocusObject()
			message(targetButton.name)
			self.fixedDoAction(targetButton)
			lastFocus.setFocus()

	# Вимкнення/увімкнення мікрофону
	@script(description=_("Press \"Mute/unmute microphone\" button"), gesture="kb:ALT+A")
	def script_microphone(self, gesture):
		obj = api.getFocusObject()
		targetButton = False
		isVoiceChat = False
		for item in self.getElements():
			if item.UIAAutomationId == "Audio" and item.previous.UIAAutomationId == "Video" and item.next.UIAAutomationId == "Accept":
				targetButton = item
				break
			elif item.UIAAutomationId == "Audio" and item.next.next.UIAAutomationId == "AudioInfo":
				targetButton = item
				isVoiceChat = True
				break
		if targetButton:
			if isVoiceChat:
				targetButton.doAction()
				obj.setFocus()
				def spechState(): message(targetButton.next.next.name)
				thr = Timer(.1, spechState).start()
				return True
			self.fixedDoAction(targetButton)
			obj.setFocus()
			def spechState(): message(targetButton.name)
			thr = Timer(.1, spechState).start()

	# Вимкнення/увімкнення камери
	@script(description=_("Press \"Enable/disable camera\" button"), gesture="kb:ALT+V")
	def script_video(self, gesture):
		obj = api.getFocusObject()
		targetButton = False
		isVoiceChat = False
		for item in self.getElements():
			if item.UIAAutomationId == "Video" and item.next.UIAAutomationId == "Audio" and item.next.next.UIAAutomationId == "Accept":
				targetButton = item
				break
			elif item.UIAAutomationId == "Video" and item.next.UIAAutomationId == "VideoInfo":
				targetButton = item
				isVoiceChat = True
				break
		if targetButton:
			if isVoiceChat:
				targetButton.doAction()
				obj.setFocus()
				def spechState():
					if targetButton.firstChild.name == "\ue964": message(_("Camera on"))
					elif targetButton.firstChild.name == "\ue963": message(_("Camera off"))
				thr = Timer(.1, spechState).start()
				return
			self.fixedDoAction(targetButton)
			obj.setFocus()
			def spechState(): message(targetButton.name)
			thr = Timer(.1, spechState).start()

	# Скопіювати поточне повідомлення в буфер обміну
	@script(description=_("Copy the message if it contains text. If the focus is on a link, the link will be copied"), gesture="kb:control+C")
	def script_copyMessage(self, gesture):
		gesture.send()
		obj = api.getFocusObject()
		if self.is_message_object(obj):
			textMessage = next((item.name for item in obj.children if item.UIAAutomationId in ("TextBlock", "Message", "Question", "RecognizedText")), False)
			mes = _("Message copied")
		elif obj.parent.UIAAutomationId in ("Message", "TextBlock"):
			textMessage = obj.name
			mes = _("Link copied")
		else: return
		if textMessage:
			api.copyToClip(textMessage.strip())
			message(mes)
		else: message(_("This message does not contain text"))

	# Скопіювати повідомлення через контекстне меню
	@script(description=_("Copy messages with formatting preserved"), gesture="kb:control+shift+C")
	def script_copy(self, gesture):
		self.activate_option_for_menu("copy", "Messages")

	# Показати текст повідомлення в спливаючому вікні
	@script(description=_("Show message text in popup window"), gesture="kb:ALT+C")
	def script_show_text_message(self, gesture):
		obj = api.getFocusObject()
		if not self.is_message_object(obj): return False
		textMessage = next((item.name for item in obj.children if item.UIAAutomationId in ("TextBlock", "Message", "Question")), False)
		if textMessage: TextWindow(textMessage.strip(), _("message text"), readOnly=False)
		else: message(_("This message does not contain text"))

	# Перенести фокус в поле вводу повідомлення. Якщо фокус вже знаходиться в цьому полі, тоді перенести його на останній елемент який був в фокусі перед цим полем
	@script(description=_("Move the focus to the edit field. If the focus is already in the edit field, then after pressing the hotkey, it will move to where it was before"), gesture="kb:ALT+D")
	def script_moveFocusToTextMessage(self, gesture):
		obj = api.getFocusObject()
		lastFocusObject = self.saved_items.get("last focus object")
		if (obj.role == controlTypes.Role.EDITABLETEXT and obj.UIAAutomationId == "TextField") or (obj.role == controlTypes.Role.BUTTON and obj.UIAAutomationId == "ButtonAction"):
			if lastFocusObject and lastFocusObject.location: lastFocusObject.setFocus()
			return
		targetButton = self.saved_items.get("message box")
		if not targetButton or not targetButton.location or not targetButton.location.width:
			targetButton = False
			for item in reversed(self.getElements()):
				if item.role == controlTypes.Role.EDITABLETEXT and item.UIAAutomationId == "TextField":
					targetButton = item
					self.saved_items.save("message box", item)
					break
		if targetButton: targetButton.setFocus()
		elif lastFocusObject and lastFocusObject.location : lastFocusObject.setFocus()
		else: message(_("Message input field not found"))

	# Натиснути кнопку "Вкласти медіа"
	@script(description=_("Press \"Attach file\" button"), gesture="kb:control+shift+A")
	def script_add_files(self, gesture):
		button = next((item for item in self.getElements() if item.UIAAutomationId and item.UIAAutomationId == "ButtonAttach"), None)
		if button: button.doAction()
		else: message(_("Button not found"))

	# Натиснути кнопку "Нова розмова"
	@script(description=_("Press \"New conversation\" button"), gesture="kb:control+N")
	def script_new_conversation(self, gesture):
		button = next((item for item in self.getElements() if item.UIAAutomationId and item.UIAAutomationId == "ComposeButton"), None)
		if button: button.doAction()
		else: message(_("Button not found"))

	# Натиснути кнопку "Більше опцій" в відкритому чаті
	# @script(description=_("Press \"More Options\" button in an open chat, voice chat, or call window"), gesture="kb:ALT+O")
	def script_showMoreOptions(self, gesture):
		labels_for_button = labels_for_button_more_options.get(conf.get("lang"), labels_for_button_more_options["en"])
		targetButton = next((item for item in self.getElements() if item.role == controlTypes.Role.BUTTON and (item.UIAAutomationId in ("Options", "Menu", "Settings") or item.name in labels_for_button) ), False)
		if targetButton: targetButton.doAction()
		else: message(_("Button not found"))

	# Відкриває меню навігації
	@script(description=_("Open navigation menu"), gesture="kb:ALT+M")
	def script_showMenu(self, gesture):
		try: targetButton = next((item for item in self.getElements() if (item.UIAAutomationId == "PhotoSide") or (item.UIAAutomationId == "Photo" and item.previous and item.previous.UIAAutomationId == "FocusTarget")), False)
		except: targetButton = False
		if targetButton: targetButton.doAction()
		else: message(_("Navigation menu not available"))

	# Функція відкриття коментарів
	@script(description=_("Open comments"), gesture="kb:control+ALT+C")
	def script_openComentars(self, gesture):
		obj = api.getFocusObject()
		if not self.is_message_object(obj): return
		targetButton = next((item for item in reversed(obj.children) if item.role == controlTypes.Role.LINK and item.UIAAutomationId == "Thread"), False)
		if targetButton:
			self.isSkipName = 1
			targetButton.doAction()
		else: message(_("Button to open comments not found"))

	# Функція відкриття профілю поточного чату
	@script(description=_("Open current chat profile"), gesture="kb:control+P")
	def script_openProfile(self, gesture):
		profile = self.saved_items.get("profile name")
		if profile and profile.location.width != 0:
			self.isOpenProfile = api.getFocusObject()
			profile.doAction()
		else: message(_("No open chat"))

	# Функція запису і надсилання голосового повідомлення
	@script(gesture="kb:control+R")
	def script_recordingVoiceMessage(self, gesture):
		if conf.get("voiceMessageRecordingIndicator") == "none":
			gesture.send()
			return
		obj = False
		log.debug("Ми потрапили в функцію запису голосового повідомлення")
		for item in reversed(self.getElements()):
			if item.role == controlTypes.Role.TOGGLEBUTTON and item.UIAAutomationId == "btnVoiceMessage":
				log.debug("Кнопку запису голосового повідомлення знайдено")
				obj = item
				break
			elif item.role == controlTypes.Role.BUTTON and item.UIAAutomationId in ("btnSendMessage", "btnEdit"):
				message(_("Recording a voice message will not be available until the edit field is empty"))
				return
		if not obj: return
		log.debug(obj.name)
		if obj.next and obj.next.UIAAutomationId == "ElapsedLabel":
			log.debug("Друге натиснення кнопки запису голосового повідомлення")
			if conf.get("voiceMessageRecordingIndicator") == "audio": winsound.PlaySound(baseDir+"send_voice_message.wav", winsound.SND_ASYNC)
			else: message(_("Record sent"))
		else:
			log.debug("Перше натиснення комбінації для запису")
			if conf.get("voiceMessageRecordingIndicator") == "audio" and controlTypes.State.PRESSED in obj.states: winsound.PlaySound(baseDir+"start_recording_video_message.wav", winsound.SND_ASYNC)
			elif conf.get("voiceMessageRecordingIndicator") == "audio": winsound.PlaySound(baseDir+"start_recording_voice_message.wav", winsound.SND_ASYNC)
			elif conf.get("voiceMessageRecordingIndicator") == "text" and controlTypes.State.PRESSED in obj.states: message(_("Video"))
			else: message(_("Audio"))
		lastFocus = api.getFocusObject()
		if conf.get("isFixedToggleButton"):
			log.debug("Відбувається стандартне натиснення кнопки")
			self.isRecord = lastFocus
			gesture.send()
		else:
			log.debug("Імітуємо натискання на кнопку запису")
			obj.doAction()
			lastFocus.setFocus()

	# Фунція скасовування запису голосового повідомлення
	# @script(gesture="kb:control+D")
	def script_cancelVoiceMessageRecording(self, gesture):
		if scriptHandler.getLastScriptRepeatCount() == 1:
			if conf.get("voiceMessageRecordingIndicator") == "none":
				conf.set("voiceMessageRecordingIndicator", "text")
				message(_("Voice recording notifications set to text"))
			elif conf.get("voiceMessageRecordingIndicator") == "text":
				conf.set("voiceMessageRecordingIndicator", "audio")
				message(_("Voice recording notifications set to sounds"))
			elif conf.get("voiceMessageRecordingIndicator") == "audio":
				conf.set("voiceMessageRecordingIndicator", "none")
				message(_("Recording voice messages has standard behavior"))
			return
		if conf.get("voiceMessageRecordingIndicator") == "none":
			gesture.send()
			return
		obj = next((item for item in reversed(self.getElements()) if (item.UIAAutomationId == "ElapsedLabel") or (item.role == controlTypes.Role.BUTTON and item.UIAAutomationId == "ComposerHeaderCancel")), False)
		lastFocus = api.getFocusObject()
		if obj and obj.UIAAutomationId == "ComposerHeaderCancel":
			obj.doAction()
			lastFocus.setFocus()
			if obj.previous.previous.name == "\ue248": message(_("Reply canceled"))
			else: message(_("Edit canceled"))
		elif obj and obj.UIAAutomationId == "ElapsedLabel":
			if conf.get("voiceMessageRecordingIndicator") == "audio": winsound.PlaySound(baseDir+"cancel_voice_message_recording.wav", winsound.SND_ASYNC)
			else: message(_("Recording canceled"))
		gesture.send()
		lastFocus.setFocus()
		lastFocus.setFocus()

	# Обробляємо повідомлення яке потрапило в фокус
	def action_message_focus(self, obj):
		keywords = keywordsInMessages.get(conf.get("lang"), keywordsInMessages["en"])
		obj.sender = ""
		forward = ""
		reactions = []
		# Визначаємо повідомлення було надісланим чи отриманим
		sender_message = "received" if keywords[3] in obj.name[-80:] else "send" if keywords[2] in obj.name[-80:] else ""
		# obj.children
		for item in obj.children:
			if (item.UIAAutomationId in ("TextBlock", "Message") and item.name.strip() not in obj.name) or item.UIAAutomationId == "RecognizedText":
				# Обробляємо підпис до повідомлення, в якому вкладено кілька медіа
				try: obj.name =re.sub(r"[\.,]?{}|{}".format(keywords[3], keywords[2]), fr". {item.name}\g<0>", obj.name)
				except: pass
			elif item.UIAAutomationId == "Question":
				# Обробляємо повідомлення які містять опитування
				options, votes = "", ""
				for el in obj.children:
					if el.UIAAutomationId == "Votes": votes = ". "+el.name+". "
					elif el.role == controlTypes.Role.TOGGLEBUTTON and el.firstChild.role == controlTypes.Role.PROGRESSBAR:
						if el.childCount == 4: options += self.processing_of_answer_options_in_surveys(el)
						elif el.childCount == 3: options+=el.children[1].name+", "
				if options: options = _("Answer options")+": "+options
				obj.name = obj.name.replace(item.name+", ", item.name+votes+options)
			elif item .UIAAutomationId in ("TextBlock", "Message") and conf.get("actionDescriptionForLinks") and item.next.UIAAutomationId == "Label" and (len(item.next.name) > 30 or "‎:‎" not in item.next.name):
				# Обробляємо підпис до посилання яке міститься в повідомлені
				description = item.next.name.strip()
				if not conf.get("voiceFullDescriptionOfLinkToYoutube") and description.startswith("YouTube "):
					description = description.split("\n")
					description = "\n".join(description[:2])
				if description not in item.name: obj.name = obj.name.replace(item.name.strip(), item.name+"\n"+description)
				for link in item.children:
					# if link.role == controlTypes.Role.LINK and link.name.startswith("http") and len(link.name) > 30: obj.name = obj.name.replace(link.name, link.name[0:30]+"...")
					if link.role == controlTypes.Role.LINK and link.name.startswith("http") and len(link.name) > 30:
						result = re.match(r"(http.{10,40})/", obj.name)
						if result: obj.name = obj.name.replace(link.name.strip(), result.group(1))
			elif item.UIAAutomationId == "Subtitle" and len(item.name) < 15 and " / " in item.name:
				# Провіряємо чи дане повідомлення є голосовим повідомленням
				obj.name = item.name+", "+obj.name.replace(item.name[-5:], "")
			elif item.role == controlTypes.Role.TOGGLEBUTTON and item.UIAAutomationId != "Recognize" and item.firstChild.UIAAutomationId == "Presenter": reactions.append(item.name)
			elif item.UIAAutomationId == "ForwardLabel": forward = item

		# Провіряємо чи дане повідомлення є дзвінком
		try:
			if obj.firstChild.role == controlTypes.Role.LINK and obj.childCount == 4 and obj.children[1].UIAAutomationId == "TitleLabel" and obj.children[2].role == controlTypes.Role.STATICTEXT:
				a = obj.children[1].name
				b = ",".join(obj.children[2].name.split(",")[1:])
				obj.name = obj.name.replace(a, a+b)
		except: pass

		if forward:
			forward_from = forward.name.split("\n")[-1]
			forward_from = forward_from[0].lower()+forward_from[1:]
			if forward_from not in obj.name[:100]:
				obj.name = forward.name+". \n"+obj.name

		# Перевіряємо чи потрібно добавити ім'я відправника повідомлення
		profile_name = self.saved_items.get("profile name")
		if conf.get("saySenderName") in ("sent", "all") and sender_message == "send": obj.sender = _("You")+".\n"
		elif conf.get("saySenderName") in ("received", "all") and profile_name and obj.firstChild.UIAAutomationId not in ("Photo", "1HeaderLabel") and obj.firstChild.location.left != 0 and obj.firstChild.location.left - obj.location.left < 30: obj.sender = profile_name.firstChild.name+".\n"
		
		# Провіряємо стан повідомлення, чи є воно прочитаним і надісланим
		# Перевірку робимо тільки в надісланих повідомленнях
		if obj.name.endswith(". ."):
			obj.name = obj.name[:-3]
			if sender_message == "send": obj.name = _("Not sent")+". " + obj.name
		else:
			if keywords[0] in obj.name[-40:]:
				# Якщо повідомлення прочитане, видаляємо інформацію про це
				obj.name = obj.name.replace(keywords[0], ".", -1)
			elif keywords[1] in obj.name[-40:]:
				# Якщо повідомлення не прочитане, перевіряємо чи потрібно відображати інформацію про це
				if (sender_message == "received") or (profile_name and profile_name.childCount == 1):
					obj.name = obj.name.replace(keywords[1], ".", -1)
				elif conf.get("unreadBeforeMessageContent"):
					obj.name = obj.name.replace(keywords[1], ".", -1)
					obj.name = keywords[1][2:]+" "+obj.name
			if conf.get("voice_the_presence_of_a_reaction") and reactions:
				# Озвучуємо реакції, якщо вони містяться в повідомленні
				pattern_replay_in_reaction = re.compile(r"^(.+)reactionTypeEmoji.+\"(.)\".+", flags=re.S)
				reactions = [re.sub(pattern_replay_in_reaction, "\g<1>\g<2>", item) for item in reactions]
				reactions = _("Reactions")+": "+", ".join(reactions)
				obj.name += "\n"+reactions
				# if sender_message == "received": obj.name = obj.name.replace(keywords[3], ".\n"+reactions+keywords[3], -1)
				# elif sender_message == "send": obj.name = obj.name.replace(keywords[2], ".\n"+reactions+keywords[2], -1)

		obj.name = obj.sender+obj.name
		# Перевіряємо чи повідомлення є виділеним
		if controlTypes.State.CHECKED in obj.states: obj.name = _("Selected")+". "+obj.name
		return obj.name

	# Обробляємо елемент зі списку чатів, який потрапив в фокус
	def actionChatElementInFocus(self, obj):
		# Записуємо тип і назву чату , після ймовірних змін, щоб регулярний вираз коректно обробляв повідомлення про те, що в групі є сповіщення для мене
		name = ""
		for item in obj.children:
			if item.UIAAutomationId == "TitleLabel":
				premium = _("Premium") if item.next and item.next.name == "\ue9b5" else _("Verified") if item.next.name == "" else ""
				title = item.name
				type = obj.name.split(", ")[0] if item.previous.UIAAutomationId == "TypeIcon" else ""
				name = type+", "+title if type else title
				if type and conf.get("voiceTypeAfterChatName") == "afterName":
					obj.name = obj.name.replace(name, title+", "+type, 1)
					name = title+", "+type
				elif type and conf.get("voiceTypeAfterChatName") == "don'tVoice":
					obj.name = obj.name.replace(type+", ", "", 1)
					name = title
				if premium and conf.get("report premium accounts"):
					obj.name = obj.name.replace(name, name+", "+premium, 1)
					name = name+premium
			elif item.UIAAutomationId == "UnreadMentionsLabel" and conf.get("isAnnouncesAnswers"):
				text = _("there are replies for you")
				obj.name = re.sub(r"%s, \d{1,3} [\w ]{5,20},"%re.escape(name), r"\g<0> %s,"%text, obj.name)
		return obj.name

	# Змінити рівень озвучення індикаторів виконання
	@script(description=_("Toggle progress bar announcements"), gesture="kb:ALT+U")
	def script_toggleVoicingPerformanceIndicators(self, gesture):
		if conf.get("voicingPerformanceIndicators") == "none":
			conf.set("voicingPerformanceIndicators", "all")
			message(_("Announce all progress bars"))
		else:
			conf.set("voicingPerformanceIndicators", "none")
			message(_("Do not announce any progress bars"))

	def script_reviewRecentMessage(self, gesture):
		try: index = int(gesture.mainKeyName[-1])
		except (AttributeError, ValueError): return
		if index == 0: index = 10
		obj = self.getMessagesElement()
		if not obj:
			message(_("No open chat"))
			return
		target = obj.lastChild
		if not target:
			message(_("This chat is empty"))
			return
		i = 0
		while target:
			child = target.firstChild
			if child.role not in (controlTypes.Role.BUTTON, controlTypes.Role.GROUPING):
				i += 1
				if i == index:
					message(self.action_message_focus(target))
					api.setNavigatorObject(target)
					break
			target = target.previous
		if i < index:
			message(_("This chat is empty"))
			return


	# Відстежуємо зміну фокуса
	def event_gainFocus(self, obj, nextHandler):
		if self.lastSavedMessage:
			if "obj" in self.lastSavedMessage:
				if api.getForegroundObject().lastChild.previous.firstChild.role == controlTypes.Role.WINDOW:
					nextHandler()
					return
				self.lastSavedMessage["obj"].setFocus()
				self.lastSavedMessage = False
				return
		elif self.isSkipName:
			speech.cancelSpeech()
			self.isSkipName -= 1
			return True
		elif self.isOpenProfile:
			self.isOpenProfile = False
			panel = next((item for item in self.getElements() if item.UIAAutomationId == "ScrollingHost"), None)
			if panel:
				self.profile_panel_element = panel
				panel.firstChild.setFocus()
		elif self.execute_context_menu_option:
			try: targetButton = next((item for item in obj.parent.children if item.firstChild.name in self.execute_context_menu_option), False)
			except: targetButton = False
			self.execute_context_menu_option = False
			if targetButton: targetButton.doAction()
			else: self.keys["escape"].send()
			return
		elif self.isRecord:
			self.isRecord.setFocus()
			self.isRecord = False
			self.isSkipName = 1
			return True
		elif self.isDelete:
			self.deleteMessageAndChat(obj)
			return
		elif self.is_set_reaction:
			index = self.is_set_reaction-1
			self.is_set_reaction = False
			list_reactions = "👍👎❤🔥🥰"
			try:
				reaction_panel = api.getForegroundObject().firstChild.previous.previous.firstChild.firstChild.children
				item = reaction_panel[index]
				message(list_reactions[index])
				time.sleep(.5)
				item.doAction()
				return True
			except: pass
		if obj.role == controlTypes.Role.LISTITEM:
			speech.cancelSpeech()
			if self.is_message_object(obj):
				self.saved_items.save("last focus object", obj)
				obj.name = self.action_message_focus(obj)
			elif obj.parent.UIAAutomationId == "ChatsList":
				obj.name = self.actionChatElementInFocus(obj)
				self.saved_items.save("last focused chat", obj)
			elif obj.parent.UIAAutomationId == "ScrollingHost":
				if obj.name == "" and obj.childCount != 0:
					for item in obj.children: obj.name+=item.name
				elif obj.name.startswith("inlineQueryResult"):
					# Обробляємо інлайн результати
					name = [item.name for item in obj.children if item.name != ""]
					obj.name = ". ".join(name)
			elif obj.name == "Unigram.ViewModels.MessageViewModel": obj.name = obj.firstChild.name
			elif obj.name.startswith("EETypeRva"): obj.name = ", ".join([item.name for item in obj.children[1:]])
			elif obj.name == "Unigram.Entities.StoragePhoto": obj.name = _("Image")
			elif obj.name == "Unigram.ViewModels.Folders.FilterFlag": obj.name = obj.children[1].name
			elif obj.name.startswith("chatTheme {"): obj.name = obj.firstChild.name
		elif obj.role == controlTypes.Role.EDITABLETEXT:
			try:
				# Визначаємо чи є дане поле вводу полем для введеня повідомлень. Якщо так, тоді перевіряємо, чи потрібного змінити його назву
				if obj.UIAAutomationId == "TextField" and (obj.previous.UIAAutomationId == "ComposerHeaderCancel" or obj.previous.previous.UIAAutomationId == "ComposerHeaderCancel"):
					label = obj.previous.previous.previous if obj.previous.UIAAutomationId != "ButtonMore" else obj.previous.previous.previous.previous
					if label.name == "\ue104": obj.name = _("Editing")
					elif label.name == "\ue248": obj.name = _("Reply")
			except: pass
		elif obj.role == controlTypes.Role.LINK:
			try:
				if obj.UIAAutomationId in ("Button", "Download") and obj.parent.parent.parent.UIAAutomationId == "Messages":
					# Озвучуємо назву і розмір файла, коли фокус потрапив на кнопку відкриття або завантаження цього файлу
					def action(title, subtitle):
						arr = subtitle.split(" - ")
						for index, value in enumerate(arr):
							if ":" in value: arr[index] = _("Duration")+": "+arr[index]
							else: arr[index] = _("Size")+": "+arr[index]
						subtitle = ". ".join(arr)
						return ": "+title+". "+subtitle
					if obj.next.UIAAutomationId == "Title" and obj.next.next.UIAAutomationId == "Subtitle": obj.name += action(obj.next.name, obj.next.next.name)
					elif obj.next.next.UIAAutomationId == "Title" and obj.next.next.next.UIAAutomationId == "Subtitle": obj.name += action(obj.next.next.name, obj.next.next.next.name)
				elif obj.parent.UIAAutomationId in ("TextBlock", "Message"): speech.cancelSpeech()
			except: pass
		elif obj.role == controlTypes.Role.BUTTON:
			try:
				# Підписуємо кнопку увімкнення мікрофону у голосовому чаті
				# Підписуємо кнопку увімкнення камери у голосовому чаті
				if obj.UIAAutomationId == "Audio" and obj.firstChild.name == "\ue720": obj.name = obj.next.next.name
				elif obj.UIAAutomationId == "Video" and obj.firstChild.name == "\ue963": obj.name = _("Enable video")
				elif obj.UIAAutomationId == "Video" and obj.firstChild.name == "\ue964": obj.name = _("Disable video")
			except: pass
		elif obj.role == controlTypes.Role.TOGGLEBUTTON:
			try:
				# Перевіряємо чи не є цей перемикач варіантом відповіді в опитуванні
				if "reactionTypeEmoji {" in obj.name:
					obj.name = re.sub(r"^(.+)reactionTypeEmoji.+\"(.)\".+", "\g<1>\g<2>", obj.name, flags=re.S)
				if obj.firstChild.UIAAutomationId == "Loading"  and obj.lastChild.UIAAutomationId == "Votes" and obj.childCount == 4: obj.name = self.processing_of_answer_options_in_surveys(obj)
			except: pass
		if obj.name == "":
			if obj.firstChild and obj.firstChild.name in labels_in_buttons: # Якщо кнопка в собі містить значок, перевіряємо чи в словнику є підпис до такого знчка
				obj.name = labels_in_buttons[obj.firstChild.name]
			elif obj.UIAAutomationId in labels_for_buttons: # Якщо кнопка має мітку, розділяємо її по словах і призначаємо її як ім'я елемента
				obj.name = labels_for_buttons[obj.UIAAutomationId]
			elif obj.UIAAutomationId:
				obj.name = ''.join(' ' + char.lower() if char.isupper() else char for char in obj.UIAAutomationId)
				obj.name = "".join(obj.name[1:]).capitalize()
			elif obj.childCount > 1:
				name = [item.name for item in obj.children if item.name != ""]
				obj.name = "/. ".join(name)
		nextHandler()

	# def event_NVDAObject_init(self,obj):
		# if obj.role == controlTypes.Role.LISTITEM and controlTypes.State.SELECTED in obj.states: message(obj.name)

	# Обробляємо ініціалізацію елементів
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		try:
			if obj.role == controlTypes.Role.CHECKBOX and  (obj.parent.role == controlTypes.Role.WINDOW or obj.parent.parent.UIAAutomationId == "Messages" or obj.next.name == "Xg"):
				clsList.insert(0, Message_list_item)
			elif obj.role == controlTypes.Role.LISTITEM:
				
				# Тут відстежуємо зміну папки з чатами
				# Також відстежуємо виділення чатів в списку чатів, щоб запам'ятати останнє виділення
				parent = obj.parent
				if parent.UIAAutomationId in ("ChatFilters", "ChatFiltersSide"):
					self.tabs_folder_element = parent
					clsList.insert(0, Tab_folder_item)
					if conf.get("voiceFolderNames") and controlTypes.State.SELECTED in obj.states: self.change_chats_folder(obj, parent.UIAAutomationId)
				elif parent.UIAAutomationId == "ChatsList" and controlTypes.State.SELECTED in obj.states: self.saved_items.save("last selected chat", obj)
			elif obj.UIAAutomationId == "Profile":
				self.saved_items.save("profile name", obj)
			elif obj.UIAAutomationId in ("Audio", "Video"):
				clsList.insert(0, Audio_and_video_button)
			elif obj.role == controlTypes.Role.SLIDER and obj.UIAAutomationId == "Slider":
				self.saved_items.save("slider", obj)
			elif conf.get("voicingPerformanceIndicators") == "none" and obj.role == controlTypes.Role.PROGRESSBAR:
				clsList.pop(0)
		except: pass

	def deleteMessageAndChat(self, obj):
		if not conf.get("confirmation_at_deletion"): speech.cancelSpeech()
		if self.isDelete["state"] == 0 and obj.role == controlTypes.Role.MENUITEM:
			for item in obj.parent.children:
				if item.firstChild.name == icons_from_context_menu["delete"]:
					self.isDelete["state"] = 1
					item.doAction()
					if conf.get("confirmation_at_deletion"): self.isDelete = False
					return
			self.isDelete = False
			self.keys["escape"].send()
		elif self.isDelete["state"] == 1 and obj.role in (controlTypes.Role.CHECKBOX, controlTypes.Role.BUTTON):
			targetButton = next((x for x in self.isDelete["elements"] if x.location and x.location.width), False)
			if obj.role == controlTypes.Role.CHECKBOX:
				# Перевіряємо чи потрібно відмітити прапорець для видалення в обох співрозмовників
				if obj.UIAAutomationId in ("CheckBox", "RevokeCheck") and ((self.isDelete["isCompleteDeletion"] and controlTypes.State.CHECKED not in obj.states) or (not self.isDelete["isCompleteDeletion"] and controlTypes.State.CHECKED in obj.states)): obj.doAction()
				obj.parent.next.doAction()
			elif obj.role == controlTypes.Role.BUTTON:
				obj.doAction()
			if targetButton: targetButton.setFocus()
			elif self.isDelete["list"] == "messages": self.script_toLastMessage(False)
			elif self.isDelete["list"] == "chats": self.script_toChatList(False)
			self.isDelete["state"] = 2
		elif self.isDelete["state"] != 1:
			if self.isDelete["message"] == "audio": winsound.PlaySound(baseDir+"delete.wav", winsound.SND_ASYNC)
			else: message(self.isDelete["message"])
			# if self.isDelete["list"] == "messages": message(self.action_message_focus(obj))
			if self.isDelete["list"] == "messages": message(obj.name)
			elif self.isDelete["list"] == "chats": message(self.actionChatElementInFocus(obj))
			self.isDelete = False

	@script(description=_("Delete a message or chat"), gesture="kb:ALT+delete")
	def script_deletion(self, gesture):
		if not self.isDelete and not self.startDeleteMessage(False): gesture.send()
	@script(description=_("Delete message or chat from both sides"), gesture="kb:shift+delete")
	def script_completeDeletion(self, gesture):
		if not self.isDelete and not self.startDeleteMessage(True): gesture.send()
	def script_BACK(self, gesture):
		try:
			obj = api.getFocusObject()
			nav = api.getNavigatorObject()
			if (obj == nav or nav.location == None) and obj.UIAAutomationId in ("TextField", "ButtonAttach", "ButtonStickers", "btnVoiceMessage", "ButtonAction") or obj.parent.parent.UIAAutomationId == "Messages" or obj.parent.parent.UIAAutomationId == "Messages":
				self.script_toChatList(gesture, True)
		except: pass
		gesture.send()
	def script_downArrow(self, gesture):
		obj = api.getFocusObject()
		try:
			if obj.role == controlTypes.Role.BUTTON and obj.firstChild.role == controlTypes.Role.GRAPHIC and obj.lastChild.role == controlTypes.Role.STATICTEXT and obj.next.role == controlTypes.Role.BUTTON: obj.next.setFocus()
			elif obj.role == controlTypes.Role.EDITABLETEXT and obj.UIAAutomationId == "TextField":
				targetButton = obj.previous
				if targetButton.role == controlTypes.Role.LIST and targetButton.UIAAutomationId == "ScrollingHost" and targetButton.firstChild.name.startswith("inlineQueryResult"): targetButton.lastChild.setFocus()
				else: message(_("Inline results not found"))
			else: gesture.send()
		except: 
			gesture.send()
	def script_upArrow(self, gesture):
		obj = api.getFocusObject()
		try:
			if obj.role == controlTypes.Role.BUTTON and obj.firstChild.role == controlTypes.Role.GRAPHIC and obj.lastChild.role == controlTypes.Role.STATICTEXT and obj.previous.role == controlTypes.Role.BUTTON: obj.previous.setFocus()
			elif obj.role == controlTypes.Role.EDITABLETEXT and obj.UIAAutomationId == "TextField":
				targetButton = obj.previous
				if targetButton.role == controlTypes.Role.LIST and targetButton.UIAAutomationId == "ScrollingHost" and targetButton.firstChild.name.startswith("inlineQueryResult"): targetButton.firstChild.setFocus()
				else: message(_("Inline results not detected"))
			else: gesture.send()
		except: gesture.send()
	@script(description=_("Switch to selection mode"), gesture="kb:control+space")
	def script_selectMessage(self, gesture):
		self.activate_option_for_menu((icons_from_context_menu["select"]), "Messages")
	@script(description=_("Forward message"), gesture="kb:ALT+F")
	def script_forwardMessage(self, gesture):
		self.activate_option_for_menu((icons_from_context_menu["forward"]), "Messages")
	@script(description=_("Mark a chat as read"), gesture="kb:ALT+shift+R")
	def script_readMessage(self, gesture):
		self.activate_option_for_menu((icons_from_context_menu["read"], icons_from_context_menu["unread"]), "ChatsList")
	@script(description=_("Save file as..."))
	def script_save_file(self, gesture):
		self.activate_option_for_menu((icons_from_context_menu["save_as"]), "Messages")
	@script(description=_("Pin a message or chat"))
	def script_attach(self, gesture):
		self.activate_option_for_menu((icons_from_context_menu["attach"], icons_from_context_menu["unpin"]))
	def activate_option_for_menu(self, option, list_name=False):
		if self.execute_context_menu_option: return False
		obj = api.getFocusObject()
		if list_name == "Messages" and not self.is_message_object(obj): return False
		elif list_name == "ChatsList" and obj.parent.UIAAutomationId and obj.parent.UIAAutomationId != list_name: return False
		elif not list_name and (not self.is_message_object(obj) and obj.parent.UIAAutomationId and obj.parent.UIAAutomationId != "ChatsList"): return
		self.execute_context_menu_option = option
		self.keys["Applications"].send()

	__gestures = {
		"kb:escape": "BACK",
		"kb:control+downArrow": "downArrow",
		"kb:control+upArrow": "upArrow",
		"kb:space": "actionMediaInMessage",
		"kb:control+D": "cancelVoiceMessageRecording",
	}

	def startDeleteMessage(self, isCompleteDeletion = False):
		obj = api.getFocusObject()
		if self.is_message_object(obj) or obj.parent.UIAAutomationId == "ChatsList":
			self.isDelete = {"isCompleteDeletion": isCompleteDeletion, "elements": [], "message": "", "list": "", "state": 0}
			if self.is_message_object(obj):
				self.isDelete["list"] = "messages"
				if self.isDelete["isCompleteDeletion"]: self.isDelete["message"] = _("Message deleted on both sides")
				else: self.isDelete["message"] = _("Message deleted")
			elif obj.parent.UIAAutomationId == "ChatsList":
				self.isDelete["list"] = "chats"
				if obj.children[1].name == "": self.isDelete["message"] = _("You left the group")
				elif obj.children[1].name == "": self.isDelete["message"] = _("You left the channel")
				elif obj.children[1].name == "" and self.isDelete["isCompleteDeletion"]: self.isDelete["message"] = _("Bot removed and blocked")
				elif obj.children[1].name == "": self.isDelete["message"] = _("Bot removed")
				elif self.isDelete["isCompleteDeletion"]: self.isDelete["message"] = _("Chat deleted on both sides")
				else: self.isDelete["message"] = _("Chat deleted")
			if conf.get("audioPlaybackWhenDeleted"): self.isDelete["message"] = "audio"
			if obj.next and obj.next.role == controlTypes.Role.LISTITEM and obj.next.childCount > 1: self.isDelete["elements"].append(obj.next)
			if obj.previous and obj.previous.role == controlTypes.Role.LISTITEM and obj.previous.childCount > 1: self.isDelete["elements"].append(obj.previous)
			if obj.previous and obj.previous.previous and obj.previous.previous.role == controlTypes.Role.LISTITEM and obj.previous.previous.childCount > 1: self.isDelete["elements"].append(obj.previous.previous)
			if obj.next and obj.next.next and obj.next.next.role == controlTypes.Role.LISTITEM and obj.next.next.childCount > 1: self.isDelete["elements"].append(obj.next.next)
			self.keys["Applications"].send()
			return True
		else: return False


	def fixedDoAction(self, obj):
		p = obj.location.center
		oldX, oldY = winUser.getCursorPos()
		winUser.setCursorPos(p.x, p.y)
		mouseHandler.executeMouseEvent(winUser.MOUSEEVENTF_LEFTDOWN, 0, 0)
		mouseHandler.executeMouseEvent(winUser.MOUSEEVENTF_LEFTUP, 0, 0)
		winUser.setCursorPos(oldX, oldY)

	def change_chats_folder(self, obj, parent):
		tab_items = obj.name.split(", ")
		count_chats = None
		last_selected_folder = self.saved_items.get("last selected folder")
		if parent == "ChatFilters" and last_selected_folder != tab_items[0]:
			self.saved_items.save("last selected folder", tab_items[0])
			if len(tab_items) >= 2 and tab_items[1] != "0": count_chats = tab_items[1]
		elif parent== "ChatFiltersSide" and last_selected_folder != tab_items[-1]:
			self.saved_items.save("last selected folder", tab_items[-1])
			if len(tab_items) > 2 and tab_items[2] != "0": count_chats = tab_items[2]
		else: return False
		text = self.saved_items.get("last selected folder")
		if count_chats: text+= ", "+count_chats
		queueHandler.queueFunction(queueHandler.eventQueue, message, text)

	# Функція копіювання даних для проведення трансляції
	@script(description=_("Copy data for broadcasting to the clipboard"), gesture="kb:ALT+shift+L")
	def script_copy_data_for_broadcast(self, gesture):
		dialog = next((item for item in self.getElements() if item.role == controlTypes.Role.DIALOG), False)
		if not dialog:
			message(_("Broadcast window not found"))
			return False
		data_area = next((item for item in dialog.children if item.role == controlTypes.Role.PANE and item.UIAAutomationId == "ContentScrollViewer"), False)
		if not data_area:
			message(_("Broadcast window not found"))
			return False
		url = next((item for item in data_area.children if item.UIAAutomationId == "Presenter"), False)
		key = url.next.next
		result_message = f"{url.previous.name}: {url.name}\n{key.previous.name}: {key.name}"
		api.copyToClip(result_message.strip())
		text_message = _("%url and %key copied to clipboard")
		text_message = text_message.replace("%url", url.previous.name)
		text_message = text_message.replace("%key", key.previous.name)
		message(text_message)


	def rewind_voice_message(self, direction):
		slider = self.saved_items.get("slider")
		if not slider or slider.location.width == 0:
			message(_("Nothing is playing right now"))
			return False
		obj = api.getFocusObject()
		slider.setFocus()
		KeyboardInputGesture.fromName(direction).send()
		obj.setFocus()
	
	@script(description=_("Fast forward a voice message"), gesture="kb:control+ALT+rightArrow")	
	def script_rewindVoiceMessageForward(self, gesture):
		self.rewind_voice_message("rightArrow")

	@script(description=_("Rewind voice message"), gesture="kb:control+ALT+leftArrow")
	def script_rewindVoiceMessageBack(self, gesture):
		self.rewind_voice_message("leftArrow")

	def script_set_reaction(self, gesture):
		obj = api.getFocusObject()
		if not self.is_message_object(obj): return
		p = obj.location.center
		winUser.setCursorPos(p.x, p.y)
		mouseHandler.executeMouseEvent(winUser.MOUSEEVENTF_RIGHTDOWN, 0, 0)
		mouseHandler.executeMouseEvent(winUser.MOUSEEVENTF_RIGHTUP, 0, 0)
		# mouseHandler.doSecondaryClick()
		try: index = int(gesture.mainKeyName[-1])
		except (AttributeError, ValueError): return
		self.is_set_reaction = index


	def processing_of_answer_options_in_surveys(self, obj):
		tmp_el = obj.firstChild
		processing_of_answer_options_in_surveys = False # Чи є цей варіант правильною відповіддю у вікторині
		while tmp_el.next: # Пробігаємось по елементах первіряючи, чи не є цей варіант правильною відповіддю у вікторині
			tmp_el = tmp_el.next
			if tmp_el.name == "\uf13e": processing_of_answer_options_in_surveys = True
		_("Right answer") # Це потрібно щоб ця фраза появилась в словнику для перекладу
		return f'{_("Right answer")+": " if processing_of_answer_options_in_surveys else ""}{obj.children[2].name} - {obj.children[1].name}, '

	# Таймер, який перевіряє, чи закінчено перетвореня голосового повідомлення в текст
	def waiting_for_recognition(self, obj):
		interval = .5
		def tick(obj):
			if not obj or not obj.next: return
			if obj.next.UIAAutomationId == "RecognizedText" and obj.next.name:
				def speak_result():
					if obj and obj.next: text = obj.next.name
					else: text = ""
					queueHandler.queueFunction(queueHandler.eventQueue, message, text)
				Timer(.4, speak_result).start()
				try: playWaveFile(baseDir+"RecognitionFinish.wav")
				except: pass
				return
			else: 
				Timer(interval, tick, [obj]).start()
		Timer(interval, tick, [obj]).start()


	# Перетворення голосових повідомлень в текст
	@script(description=_("Convert voice message to text"), gesture="kb:NVDA+ALT+R")
	def script_Recognize_voice_message(self, gesture):
		obj = api.getFocusObject()
		button = next((item for item in obj.children if item.UIAAutomationId == "Recognize"), None)
		if button:
			# if button.next and button.next.UIAAutomationId == "RecognizedText":
			if controlTypes.State.PRESSED in button.states or button.next and button.next.UIAAutomationId == "RecognizedText":
				if button.next.UIAAutomationId == "RecognizedText" and button.next.name: message(_("This voice message is already converted to text"))
				elif button.next.UIAAutomationId == "RecognizedText" and button.next.name == "": message(_("Converting this voice message is already in process"))
				return
			button.doAction()
			obj.setFocus()
			try: playWaveFile(baseDir+"RecognitionStart.wav")
			except: message("Conversion started")
			self.waiting_for_recognition(button)
		else: message(_("Button not found"))


	@script(description=_("Enable automatic reading of new messages in the current chat"), gesture="kb:ALT+L")
	def script_toggle_live_chat(self, gesture):
		if Chat_update.toggle(self): message(_("Automatic reading of messages is enabled"))
		else: message(_("Automatic reading of new messages is disabled"))

