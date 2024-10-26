import sqlite3
import json
import Noun


def load_nouns(json_filename):
    with open(json_filename, 'r', encoding = 'cp1252') as jsonfile:
        data = json.load(jsonfile)
    nouns = [Noun(d['word'], d['meaning']) for d in data]
    return nouns

if __name__ == '__main__':
    nouns = load_nouns('data\database.json')

