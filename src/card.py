from enum import Enum
import random

class Action(Enum):
    STAND = 0
    HIT = 1
    DOUBLE = 2
    SPLIT = 3
    SURRENDUR = 4

class Hand_Quality(Enum):
    HARD = 0
    SOFT = 1
    PAIR = 2


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
    8: 'T',
    9: 'J',  # Jack
    10: 'Q', # Queen
    11: 'K', # King
    12: 'A'  # Ace
}

worth_dict = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 1
}

class Card:
    CUT_CARD = None
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
        self.shoe.insert(penetration * 52, Card.CUT_CARD)
        self.cards_in_discard_tray = 0

    def deal(self):
        self.cards_in_discard_tray += 1
        return self.shoe.pop()
    
class Hand:
    def __init__(self):
        self.hand = [Card()]


class Player:
    def __init__(self):
        self.strategy = {
            Hand_Quality.HARD : {},
            Hand_Quality.SOFT : {},
            Hand_Quality.PAIR : {}
        }
        
        for i in range(1, 11):
            self.strategy[Hand_Quality.HARD][(21, i)] = Action.STAND
            self.strategy[Hand_Quality.SOFT][(21, i)] = Action.STAND
        
        for i in range(20, 4, -1):
            stats = {up_card : {
                Action.STAND : 0,
                Action.HIT : 0,
                Action.DOUBLE : 0,
                Action.SURRENDUR : 0
            } for up_card in worth_dict.keys()}

            possible_actions = [
                Action.STAND,
                Action.HIT,
                Action.DOUBLE,
                Action.SURRENDUR
            ]

            for shoe_num in range(10000):
                current_shoe = Shoe(6, 1.5)
                past_cut_card = False
                while not past_cut_card:
                    current_up_card = current_shoe.deal()
                    if current_up_card 
                    for action in possible_actions:



            
