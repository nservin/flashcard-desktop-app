"""Documentame loco"""
import wx
import os
import sys
sys.path.append(os.getcwd())

class MainFrame(wx.Frame):
    def __init__(self, controller):
        super().__init__(parent=None, title='Language app', size=(650, 450))
        self.panel = StartPanel(self)
        self.controller = controller
        
        self._make_manu_bar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to myApp!")
        self.Show()

    def _make_manu_bar(self):
        menu_bar = wx.MenuBar()
        for each_menu_data in self._menu_data():
            menu_label = each_menu_data[0]
            menu_items = each_menu_data[1:]
            menu_bar.Append(self._create_menu(menu_items), menu_label)
        self.SetMenuBar(menu_bar)
    def _create_menu(self, menu_data):
        menu = wx.Menu()
        for each_label, each_status, each_handler in menu_data:
            menu_item = menu.Append(-1, each_label, each_status)
        self.Bind(wx.EVT_MENU, each_handler, menu_item)
        return menu

    def _menu_data(self):
        return (('&Settings',
                    ('&Text', "Un mensaje para mi amor...", self._on_text_btn), 
                    ('&Audio', "Audio options", self._on_audio_btn)),
                # ('&Help',
                #     (wx.ID_EXIT, "Exit" ,self.on_exit_btn)),
                ('&View',
                    ('&Romanizacion', "Activar/desactivar romanizacion", self._on_roma_btn)))

    def _hide_panel(self):
        self.panel.Hide()
    def _on_exit_btn(self, event):
        self.Close(True)
    def _on_text_btn(self, event):
        wx.MessageBox("I love you <3", "Mensaje", wx.ICON_HAND)
    def _on_audio_btn(self, event):
        wx.MessageBox("Ejemplo", "Algo pasa", wx.OK|wx.ICON_HAND)
    def _on_roma_btn(self):
        pass
    def _on_audio_btn(self):
        pass

class StartPanel(wx.Panel):
    def __init__(self, parent:MainFrame):
        wx.Panel.__init__(self, parent)
        self.sizer = wx.GridBagSizer(2, 1)
        self._make_main_title()
        self._make_button_bar()
        self.Show()
    
    def _make_main_title(self):
        st = wx.StaticText(self, label="Russian Flashcards", pos=(200, 10))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

    def _make_button_bar(self):
        button_label = self._button_bar_data()
        for i in range(8):
            for j in range(5):
                btn = wx.Button(self, label=button_label[5 * i + j])
                self.sizer.Add(btn, pos=(i + 3, j + 5), flag = wx.EXPAND)
                self.Bind(wx.EVT_BUTTON, self._set_study_panel, btn)
        self.SetSizer(self.sizer)
    def _button_bar_data(self):
        return ('Lvl.1\n','Lvl.2\n','Lvl.3\n','Lvl.4\n','Lvl.5\n',
                'Lvl.6\n','Lvl.7\n','Lvl.8\n','Lvl.9\n','Lvl.10\n',
                'Lvl.11\n','Lvl.12\n','Lvl.13\n','Lvl.14\n','Lvl.15\n',
                'Lvl.16\n','Lvl.17\n','Lvl.18\n','Lvl.19\n','Lvl.20\n',
                'Lvl.21\n','Lvl.22\n','Lvl.23\n','Lvl.24\n','Lvl.25\n',
                'Lvl.26\n','Lvl.27\n','Lvl.28\n','Lvl.29\n','Lvl.30\n',
                'Lvl.31\n','Lvl.32\n','Lvl.33\n','Lvl.34\n','Lvl.35\n',
                'Lvl.36\n','Lvl.37\n','Lvl.38\n','Lvl.39\n','Lvl.40\n',
                )
    def _set_study_panel(self, event):
        level = self._get_btn_lvl(event)
        self._set_flashcard(level)
        self._hide_start_menu()
    def _get_btn_lvl(self, event):
        # Label is a string 'Lvl.#', label[4:] gets the numerical part of the string
        return int(event.GetEventObject().GetLabel()[4:]) - 1
    def _set_flashcard(self, level):
        return self.Parent.controller.start_study_session(level)
    def _hide_start_menu(self):
        self.Hide()

class FlashcardPanel(wx.Panel):
    def __init__(self, parent, word):
        wx.Panel.__init__(self, parent, size=parent.Size)
        self.sizer = wx.GridBagSizer(5, 5)
        self.word = word
        self.st_word = self.display_word(word)
        self.st_meaning = self._display_meaning()
        self._make_btn_bar()
        self.Show()
    
    def display_word(self, word):
        st = wx.StaticText(self, label= word.name, pos=(200, 50))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)
        return st

    def _display_meaning(self):
        st = wx.StaticText(self, label= ' ', pos=(200, 100))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)
        return st
    def _make_btn_bar(self):
        for each_label, each_pos, each_foo, sizer_pos in self._btn_data():
            btn = self._create_btn(self, each_label, each_pos)
            self.sizer.Add(btn,pos=sizer_pos, flag = wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, each_foo, btn)
        self.SetSizer(self.sizer)
    def _create_btn(self, pnl, btn_label, btn_pos):
        return wx.Button(pnl, label=btn_label, pos=btn_pos)
    def _btn_data(self):
        return (('Repetir', (200, 350), self._on_repeat, (3,1))
                ,('Mostrar', (300, 350), self._on_show, (3,2))
                ,('Aprendida', (400, 350), self._on_next, (3,3))
                ,('Salir', (500, 350), self._on_fav, (3,4))
                )
    def _on_repeat(self, event):
        pass
    def _on_next(self, event):
        self.st_meaning.Hide()
        self.update_queue()
        self.word = self.Parent.controller.next_word()
        self.st_word.SetLabel(self.word.name)

    def _on_fav(self, event):
        pass
    def _on_show(self, event):
        self.st_meaning.SetLabel(self.word.meaning)
        self.st_meaning.Show()
    def _set_main_menu_panel(self,pnl):
        self.panel = StartPanel(self)
    def update_queue(self):
        self.Parent.controller.update_word_status(self.word)


class Dashboard(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        st = wx.StaticText(self, label = "Facil")
        st = wx.StaticText(self, label = "Medio")
        st = wx.StaticText(self, label = "Dificil")
        sizer = wx.GridBagSizer(2, 1)
        self.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App()
    window = wx.Frame()
    mainFrame = MainFrame(window)
    window.Show()
    app.MainLoop()