from modules.deck import Deck
from modules.hand import Hand


class Player:
    def __init__(self):
        self.hand:Hand = Hand()
        

    def draw_card(self,deck):
        self.hand.add_card(deck)

class Human_player(Player):
    def __init__(self):
        super().__init__()
        self.wallet:int = 1000
    
    def bet(self, bet_ammount):
        self.wallet -= bet_ammount



class Dealer(Player):
    def __init__(self):
        super().__init__() 

    def play(self,deck):
        while self.hand.score()[0] < 17:
            if self.hand.score()[1] < 17:
                self.draw_card(deck)

            elif self.hand.score()[1] > 21:
                self.draw_card(deck)

            else:
                break
