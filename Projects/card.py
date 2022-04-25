class Card:
   # allowed_suite = ["Hearts", "Diamonds", "Clubs", "Spades"]
   # allowed_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suite}"

class Deck:
    def __init__(self):
        pass
