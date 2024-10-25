import wx
from GUI.Window import Window

app = wx.App()
mainWindow = Window('Language App')
mainWindow.Show()
mainWindow.Centre()
app.MainLoop()