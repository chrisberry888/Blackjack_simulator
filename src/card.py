from enum import Enum
import random

suit_dict = {
    0: 's', # Spades
    1: 'd', # Diamonds
    2: 'c', # Clubs
    3: 'h'  # Hearts
}

value_dict = {
    0: '2',
    1: '3',
    2: '4',
    3: '5',
    4: '6',
    5: '7',
    6: '8',
    7: '9',
    8: '10',
    9: 'J',  # Jack
    10: 'Q', # Queen
    11: 'K', # King
    12: 'A'  # Ace
}

class Card:
    def __init__(self, suit_number, value_number):
        self.suit_number = suit_number
        self.value_number = value_number
        self.suit = suit_dict.get(suit_number)
        self.value = value_dict.get(value_number)

    def __repr__(self):
        return f"{self.value}{self.suit}"

    def get_card_name(self):
        return (self.value + self.suit)
    
        

class Deck:
    def __init__(self):
        self.deck = [Card(i, j) for i in range(4) for j in range(13)]

    def shuffle(self):
        random.shuffle(self.deck)
        

class Shoe:
    def __init__(self, decks, penetration):
        self.shoe = [Card(i, j) for i in range(4) for j in range(13) for k in range(decks)]
        random.shuffle(self.shoe)
        self.shoe.insert(penetration * 52, "CUTOFF")

    def deal(self):
        return self.shoe.pop()


class Player:
    def __init__(self) -> None:
        pass