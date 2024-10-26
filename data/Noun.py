import time
class Noun():
    def __init__(self, wordName:str, meaning:str):
        self._name = wordName
        self._means = meaning
        self._date = 0
        self._inter = 0

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name:str):
        self._name = new_name
    @name.deleter
    def name(self):
        del self._name

    @property
    def means(self):
        return self._means
    @means.setter
    def means(self, new_meaning:str):
        self._means = new_meaning
    @means.deleter
    def means(self):
        del self._means
    
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, new_date:str):
        self._date = new_date
    @date.deleter
    def date(self):
        del self._date
    
    @property
    def inter(self):
        return self._inter
    @inter.setter
    def inter(self, new_interval:str):
        self._inter = new_interval
    @inter.deleter
    def inter(self):
        del self._inter
    
    

