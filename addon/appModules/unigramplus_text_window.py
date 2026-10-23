import wx
import gui


class TextWindow(wx.Frame):

	def __init__(self, text, title, readOnly=True, insertionPoint=0):
		super(TextWindow, self).__init__(gui.mainFrame, title=title)
		sizer = wx.BoxSizer(wx.VERTICAL)
		style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH
		self.outputCtrl = wx.TextCtrl(self, style=style)
		self.outputCtrl.Bind(wx.EVT_KEY_DOWN, self.onOutputKeyDown)
		sizer.Add(self.outputCtrl, proportion=1, flag=wx.EXPAND)
		self.SetSizer(sizer)
		sizer.Fit(self)
		self.outputCtrl.SetValue(text)
		self.outputCtrl.SetFocus()
		self.outputCtrl.SetInsertionPoint(insertionPoint)
		self.Raise()
		self.Maximize()
		self.Show()

	def onOutputKeyDown(self, event):
		if event.GetKeyCode() == wx.WXK_ESCAPE:
			self.Close()
		event.Skip()
