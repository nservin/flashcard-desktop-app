class Noun():
    def __init__(self, wordName:str, meaning:str, gender:str):
        self._name = wordName
        self._means = meaning
        self._gender = gender
        self._date = 0
        self._inter = 0

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name:str):
        self._name = new_name
    
    @property
    def means(self):
        return self._means
    @means.setter
    def means(self, new_meaning:str):
        self._means = new_meaning
    
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, new_gender:str):
        self._gender = new_gender
    
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, new_date:str):
        self._date = new_date
    
    @property
    def inter(self):
        return self._inter
    @inter.setter
    def inter(self, new_interval:str):
        self._inter = new_interval
    
    def __str__(self) -> str:
        return f'word: {self._name}\nMeaning: {self._means}\n'
    
    

