from card import *

class Strategy():

    def __init__(self, imported_dict=None):
        if imported_dict == None:
            self.strategy_dict = self.generate_basic_strategy()
        else:
            self.strategy_dict = imported_dict
    

    def generate_basic_strategy(self):
        hard_strategy = self.generate_hard_strategy()
        soft_strategy = self.generate_soft_strategy(hard_strategy)
        pair_strategy = self.generate_pair_strategy(hard_strategy, soft_strategy)
        strategy = {
            Hand_Quality.HARD : hard_strategy,
            Hand_Quality.SOFT : soft_strategy,
            Hand_Quality.PAIR : pair_strategy
        }
        return strategy

    def generate_hard_strategy(self):
        hard_strategy = {}
        for card in worth_dict:
            hard_strategy[(21, card)] = Action.STAND
        for current_worth in range(20, 10, -1):
            stats = {
                up_card : {
                    Action.STAND : 0,
                    Action.HIT : 0
                } for up_card in worth_dict
            }
            
            for shoe_num in range(10000):
                current_shoe = Shoe(6, 1.5)
                ticker = 0
                while not current_shoe.past_cut_card:
                    dealer_hand = Hand(current_shoe.deal(), current_shoe.deal())
                    if current_worth == 11:
                        player_hand = Hand(Card(0,9), Card(0, 2))
                    else:
                        player_hand = Hand(Card(0,10), Card(0, current_worth - 10))
                    if player_hand.hand_worth != current_worth:
                        continue
                    if ticker == 0:
                        self.dealer_finish_hand(dealer_hand, current_shoe)
                        if player_hand.hand_worth > dealer_hand.hand_worth or dealer_hand.hand_worth > 21:
                            stats[dealer_hand.hand[0]][Action.STAND] += 1
                        elif player_hand.hand_worth < dealer_hand.hand_worth:
                            stats[dealer_hand.hand[0]][Action.STAND] -= 1
                    else:
                        player_hand.add_card(current_shoe.deal())
                        while hard_strategy.get((player_hand.hand_worth, dealer_hand.hand[0].value), Action.STAND) == Action.HIT:
                            player_hand.add_card(current_shoe.deal())
                        self.dealer_finish_hand(dealer_hand)
                        if player_hand.hand_quality == Hand_Quality.LOST or player_hand.hand_worth < dealer_hand.hand_worth:
                            stats[dealer_hand.hand[0]][Action.HIT] -= 1
                        elif player_hand.hand_worth > dealer_hand.hand_worth or dealer_hand.hand_worth > 21:
                            stats[dealer_hand.hand[0]][Action.HIT] += 1
                    ticker = (ticker + 1) % 2
            
            for up_card in stats:
                proper_action = (Action.STAND if stats[up_card][Action.STAND] > stats[up_card][Action.HIT] else Action.HIT)
                hard_strategy[(current_worth, up_card)] = proper_action
            
        return hard_strategy                        
                        


    def generate_soft_strategy(self, hard_strategy):
        return None

    def generate_pair_strategy(self, hard_strategy, soft_strategy):
        return None

    def use_strategy(self, player_hand: Hand, dealer_up_card: Card):
        pass

    def dealer_finish_hand(self, hand: Hand, shoe: Shoe):
        while hand.hand_worth < 17:
            hand.add_card(shoe.deal())