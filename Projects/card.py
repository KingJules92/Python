import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        pass

    def shuffle(self):
        return random.shuffle(self.cards)

    def _deal(self, num):
        pass

    def deal_hand(self):
        pass

d = Deck()
d.shuffle()
print(d.cards)