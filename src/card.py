from enum import Enum

class Suit(Enum):
    SPADES = 0
    DIAMONDS = 1
    CLUBS = 2
    HEARTS = 3

class Value(Enum):
    TWO = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    ACE = 12

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

    def get_card_name(self):
        return (self.value + self.suit)
        

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(52):
            self.deck.append(Card((i % 4), (i % 13)))
        
        