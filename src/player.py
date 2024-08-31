from card import *

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
                ticker = 0
                while not current_shoe.past_cut_card:
                    dealer_hand = Hand(current_shoe.deal(), current_shoe.deal())
                    player_hand = Hand(current_shoe.deal(), current_shoe.deal())
                    if player_hand.hand_worth != i:
                        continue
                    if ticker == 0:
                        dealer_worth = self.dealer_finish_hand(dealer_hand, current_shoe)
                        if player_hand.hand_worth > dealer_worth or dealer_worth > 21:
                            stats[dealer_hand.hand[0].value][Action.STAND] += 1
                        elif player_hand.hand_worth < dealer_worth:
                            stats[dealer_hand.hand[0].value][Action.STAND] -= 1
                    elif ticker == 1:
                        player_hand.add_card(Card())
                        if player_hand.hand_quality == Hand_Quality.LOST:
                            stats[dealer_hand.hand[0].value][Action.HIT] -= 1
                        else:
                            while(self.strategy[player_hand.hand_quality][(player_hand.hand_worth, dealer_hand.hand[0].value)]) != Action.STAND:
                                

    def dealer_finish_hand(self, hand: Hand, shoe: Shoe):
        while hand.hand_worth < 17:
            hand.add_card(Card())
        return hand.hand_worth
                        
                    
                    
                        


            