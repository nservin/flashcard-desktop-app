import wx

class Window(wx.Frame):
    def __init__(self, title):
        super().__init__(parent = None, title = title, size = (650, 450))
        
        # Create a panel in the frame
        pnl  = wx.Panel(self)
        
        # I don't know what a sizer is
        sizer = wx.GridBagSizer(2, 1)
        
        # Add buttons in two grids
        sizer.Add(wx.Button(pnl, label = 'Fácil'), pos = (2, 7), flag = wx.EXPAND)
        sizer.Add(wx.Button(pnl, label = 'Medio'), pos = (2, 8), flag = wx.EXPAND)
        sizer.Add(wx.Button(pnl, label = 'Difícil'), pos = (2, 9), flag = wx.EXPAND)
        for i in range(10):
            for j in range(3):
                aux = str(j*30+1 + i*90)+'-'+str(j*30+30 + i*90)
                sizer.Add(wx.Button(pnl, label = aux), pos = (i+3, j+5), flag = wx.EXPAND)
        for i in range(10, 20):
            for j in range(3):
                aux = str(j*30+1 + i*90)+'-'+str(j*30+30 + i*90)
                sizer.Add(wx.Button(pnl, label = aux), pos = (i-7, j+9), flag = wx.EXPAND)        
        pnl.SetSizer(sizer)
        self.makeMenuBar()
        
        # And a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to myApp!")
        
        # Put some Static Text(st) with a larger bold font on it
        st = wx.StaticText(pnl, label="Russian Flashcards")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

    def makeMenuBar(self):
        settingsMenu = wx.Menu()
        settingsItem1 = settingsMenu.Append(1, '&Kattia', "Un mensaje para mi amor...")
        settingsItem2 = settingsMenu.Append(2, '&Audio', "Audio options")
        settingsMenu.AppendSeparator()
        exitItem = settingsMenu.Append(wx.ID_EXIT)
        
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(settingsMenu, '&Settings')
        menuBar.Append(helpMenu, '&Help')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnText, settingsItem1)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)     
   
    def OnClickButton(self, event):
        self.label.SetLabelText("Texto")

    def OnExit(self, event):
        # Terminates the application
        self.Close(True)
    
    def OnText(self, event):
        wx.MessageBox("I love you <3", "Mensaje", wx.ICON_HAND)
    
    def OnAbout(self, event):
        wx.MessageBox("Ejemplo", "Algo pasa", wx.OK|wx.ICON_HAND)

        
if __name__ == '__main__':
    app = wx.App()
    window = Window('Language App')
    window.Show()
    window.Centre()
    app.MainLoop()