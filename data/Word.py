"""Documentame loco"""
from datetime import datetime
class Word():
    def __init__(self
                 ,word_id:int
                 ,word_name: str
                 ,word_meaning: str
                 ,word_gender: str
                 ,word_status: str
    ):
        self._id = word_id
        self._name = word_name
        self._meaning = word_meaning
        self._gender = word_gender
        self._ease_factor = 2.5
        self._interval = 1
        self._repetitions = 0
        self._status = word_status
        self._nextReview = datetime.today()
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name: str):
        self._name = new_name
    
    @property
    def meaning(self):
        return self._meaning
    @meaning.setter
    def means(self, new_meaning: str):
        self._meaning = new_meaning
    
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, new_gender: str):
        self._gender = new_gender
    
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, new_date:str):
        self._date = new_date
    
    @property
    def interval(self):
        return self._interval
    @interval.setter
    def interval(self, new_interval: str):
        self._interval = new_interval
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, new_status: str):
        self._status = new_status
        
    def __str__(self) -> str:
        return (
            f'word: {self._name}\n'
            f'Meaning: {self._meaning}\n'
            f'Status: {self._status}\n'
        )
    
    

