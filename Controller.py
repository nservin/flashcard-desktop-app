"""Documentame loco"""
'''Create functions for:
    Processing user input
        Getting the list of nouns for each level
        Selecting Window
        Refreshing the GUI
    Updating data    
        Setting  a Noun date of last review
        Updating a Noun interval of review
    Calling the SRS Algorithm
        Defining a new interval of review for a Noun
'''
import wx
from gui.flashcard_gui import *
from src.Scheduler import Scheduler
from data.Database import Database

class Controller:
    def __init__(self):
        self.view = MainFrame(self)
        self.scheduler = Scheduler(self)
        self.database = Database(self)
        self.fs_queue = []
    
    def start_study_session(self, level):
        self.fs_queue = self.database.get_level_data(level)
        for word in self.fs_queue:
            if word.status == False:
                self.view.panel = FlashcardPanel(self.view, word)
                return True
        print('NIVEL COMPLETADO')
    def next_word(self):
        for word in self.fs_queue:
            if word.status == False:
                return word
        print('NIVEL COMPLETADO, TODAS LAS PALABRAS APRENDIDAS')
    def start_review_session(self):
        pass
    def update_word_status(self, word):
        for each_word in self.fs_queue:
            if each_word.name == word.name:
                each_word.status = True
                print(each_word)
                break

if __name__ == '__main__':
    app = wx.App()
    controller = Controller()
    #controller.getData(0)
    app.MainLoop()

