import wx
# import os
# from gui.flashcard_gui import Window
# print(os.path)


app = wx.App()
mainWindow = Window()
mainWindow.Show()
mainWindow.Centre()
app.MainLoop()

