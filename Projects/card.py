import random

allowed_suite = ["Hearts", "Diamonds", "Clubs", "Spades"]
allowed_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suite}"

class Deck:

    def __init__(self):
        suite = ["Hearts", "Diamonds", "Clubs", "Spades"]
        value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suite) for value in value and suite in suite]

    def __repr__(self):
        pass

    def shuffle(self):
        pass

    def _deal(self):
        pass

    def deal_hand(self):
        pass

