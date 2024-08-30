from card import Shoe
from card import Card

class Shoe_Game:
    def __init__(self, number_of_decks=6, 
                 deck_penetration=1.5, 
                 blackjack_payout=1.5, 
                 dealer_hit_soft_17=False,
                 surrendur=True,
                 double_after_split=True,
                 charlie=None
                 ):
        self.shoe = Shoe(number_of_decks, deck_penetration)
        self.blackjack_payout = blackjack_payout
        self.dealer_hit_soft_17 = dealer_hit_soft_17
        self.surrendur = surrendur
        self.double_after_split = double_after_split
        self.charlie = charlie

    def hand_sum(self, hand):
        pass


    def play_game(self, player):
        dealer_top_card = self.shoe.deal()
        dealer_bottom_card = self.shoe.deal()
        player_hand = [self.shoe.deal(), self.shoe.deal()]

    def enact_strategy(self, player, hand):

