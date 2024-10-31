import wx
import os
import sys
sys.path.append(os.getcwd())

class MainFrame(wx.Frame):
    def __init__(self, controller):
        super().__init__(parent = None, title = 'Language app', size = (650, 450))
        self.panel = MainMenu(self)
        self.controller = controller
        
        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to myApp!")
        self.Show()

    def makeMenuBar(self):
        # Menu 1
        settingsMenu = wx.Menu()
        settingsItem1 = settingsMenu.Append(1, '&Text', "Un mensaje para mi amor...")
        settingsItem2 = settingsMenu.Append(2, '&Audio', "Audio options")
        settingsMenu.AppendSeparator()
        exitItem = settingsMenu.Append(wx.ID_EXIT)
        
        # Menu 2
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Menu 3
        viewMenu = wx.Menu()

        menuBar = wx.MenuBar()
        menuBar.Append(settingsMenu, '&Settings')
        menuBar.Append(helpMenu, '&Help')
        menuBar.Append(viewMenu, '&View')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnText, settingsItem1)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)     
        self.Bind(wx.EVT_MENU, self.OnClickButton, settingsItem2)
    
    def _hide_panel(self):
        self.panel.Hide()
    def OnClickButton(self, event):
        self.label.SetLabelText("Texto")
    def OnExit(self, event):
        self.Close(True)
    
    def OnText(self, event):
        wx.MessageBox("I love you <3", "Mensaje", wx.ICON_HAND)
    
    def OnAbout(self, event):
        wx.MessageBox("Ejemplo", "Algo pasa", wx.OK|wx.ICON_HAND)

class MainMenu(wx.Panel):
    def __init__(self, parent:MainFrame):
        wx.Panel.__init__(self, parent)
        
        # Put some Static Text(st) with a larger bold font on it
        st = wx.StaticText(self, label="Russian Flashcards")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)
        # Add buttons into two grids
        sizer = wx.GridBagSizer(2, 1)
        # Creates the buttoms for selecting a group of flashcards
        buttom1 = wx.Button(self, label = 'Mostrar flashcard')
        sizer.Add(buttom1, pos = (2, 9), flag = wx.EXPAND)
        for i in range(10):
            for j in range(3):
                aux = str(j*30+1 + i*90)+'-'+str(j*30+30 + i*90)
                sizer.Add(wx.Button(self, label = aux), pos = (i+3, j+5), flag = wx.EXPAND)
        for i in range(10, 20):
            for j in range(3):
                aux = str(j*30+1 + i*90)+'-'+str(j*30+30 + i*90)
                sizer.Add(wx.Button(self, label = aux), pos = (i-7, j+9), flag = wx.EXPAND)        
        self.SetSizer(sizer)
        # Event handler
        self.Bind(wx.EVT_BUTTON, self._set_flashcard_panel, buttom1)
    def _set_flashcard_panel(self, event):
        self.Hide()
        FlashcardPanel(self.Parent)

class FlashcardPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetSize(parent.Size)
        st = wx.StaticText(self, label="Word:\nmeaning:", pos = (200,50))
        sizer1 = wx.GridBagSizer(5, 5)
        sizer1.Add(wx.Button(self, label = 'Fácil', pos = (200, 350)), pos = (3, 1), flag = wx.EXPAND)
        sizer1.Add(wx.Button(self, label = 'Medio', pos = (300, 350)), pos = (3, 2), flag = wx.EXPAND)
        sizer1.Add(wx.Button(self, label = 'Difícil', pos = (400, 350)), pos = (3, 3), flag = wx.EXPAND)
        self.SetSizer(sizer1)
        self.Show()
    def _set_main_menu_panel(self,pnl):
        self.panel = MainMenu(self)


class Dashboard(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        st = wx.StaticText(self, label="Facil")
        st = wx.StaticText(self, label="Medio")
        st = wx.StaticText(self, label="Dificil")
        #font = st.GetFont()
        #font.PointSize += 10
        #font = font.Bold()
        #st.SetFont(font)
        sizer = wx.GridBagSizer(2, 1)
        self.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App()
    window = MainFrame()
    window.Show()
    app.MainLoop()