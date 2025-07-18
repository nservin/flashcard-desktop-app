"""Documentame loco"""
import sys
import os
from datetime import date
sys.path.append(os.getcwd())
from data.Database import Database

class Scheduler:
    def __init__(self, controller) -> None:
        self.database = Database(self)
        self.controller = controller
    
    def get_today_review(self, level):
        """ Return nouns that need review today."""
        today = date.today()
        return [noun for noun in self.words if noun.nextReview <= today]
    def update_schedule(self, noun, rating):
        """Update the noun based on user rating and recalculate next review date."""
        noun.update_review(rating)    