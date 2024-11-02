'''
Create functions for:
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
from data.Database import Database
from gui.flashcard_gui import *

class Controller:
    def __init__(self):
        self._database = Database()
        self._view = MainFrame(self)


if __name__ == '__main__':
    app = wx.App()
    controller = Controller()
    app.MainLoop()

