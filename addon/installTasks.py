# -*- coding: UTF-8 -*-

import addonHandler
import gui
import wx
import os
import globalVars

addonHandler.initTranslation()

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.manifest['name'] == "UnigramPlus":
			addon.requestRemove()