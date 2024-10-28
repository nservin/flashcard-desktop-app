import json
import sys
import os
sys.path.append(os.getcwd())
from data.Noun import Noun

class Database:
    def __init__(self, ):
        self._data = []
        pass

    def read_data(self, json_filename):
        with open(json_filename, 'r', encoding= 'iso8859_5') as jsonfile:
            data = json.load(jsonfile)
        nouns = [Noun(d['word'], d['translation'], d['gender']) for d in data]
        self._data = nouns

    def update_data(self):
        pass
    

if __name__ == '__main__':
    nuevo = Noun('g','','')

