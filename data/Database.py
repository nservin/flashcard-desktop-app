"""Documentame loco"""
import json
import sys
import os
sys.path.append(os.getcwd())
from data.Word import Word

class Database:
    def __init__(self, scheduler ):
        self.data = self._read_data_file('data/nouns.json')
        self.scheduler = scheduler
    
    def _read_data_file(self, json_filename):
        with open(json_filename, 'r', encoding= 'utf-8') as jsonfile:
            data = json.load(jsonfile)
        nouns = [Word(d['translation'], d['word'], d['gender'], d['status']) for d in data]
        return nouns    
    def get_level_data(self, lvl: int):
        return self.data[(lvl + 49 * lvl):(49 + lvl + 49 * lvl)]
    def 
    def update_status(self, word):
        pass
    def set_default_data(self):
        default_data = self._read_data_file('default_database.json')
    
    
if __name__ == '__main__':
    nuevo = Database('scheduler')
    word = nuevo.data[0]
    print(word.name())

