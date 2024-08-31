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
    LOST = 3

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

class Shoe:
    def __init__(self, decks, penetration):
        self.shoe = [Card(i, j) for i in range(4) for j in range(13) for k in range(decks)]
        random.shuffle(self.shoe)
        self.shoe.insert(penetration * 52, Card.CUT_CARD)
        self.cards_in_discard_tray = 0
        self.past_cut_card = False

    def deal(self):
        curr = self.shoe.pop()
        if curr == Card.CUT_CARD:
            self.past_cut_card = True
            curr = self.shoe.pop()
        self.cards_in_discard_tray += 1
        return curr

class Hand: 
    def __init__(self, card_1: Card, card_2: Card):
        self.hand = [card_1, card_2]
        self.hand_worth, self.hand_quality = self.calculate_hand_worth()

    def calculate_hand_worth(self):
        worth = 0
        hand_contains_ace = False
        for card in self.hand:
            worth += worth_dict.get(card.value)
            if card.value == 'A':
                hand_contains_ace = True
        if len(self.hand) == 2 and self.hand[0].value == self.hand[1].value:
            hand_quality = Hand_Quality.PAIR
        elif worth <= 11 and hand_contains_ace:
            worth += 10
            hand_quality = Hand_Quality.SOFT
        elif worth <= 21:
            hand_quality = Hand_Quality.HARD
        else:
            hand_quality = Hand_Quality.LOST
        return worth, hand_quality
        
    def add_card(self, card: Card):
        self.hand.append(card)
        self.hand_worth, self.hand_quality = self.calculate_hand_worth()

