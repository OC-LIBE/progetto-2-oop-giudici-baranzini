from modules.deck import Deck
from modules.hand import Hand


class Player:
    def __init__(self):
        self.hand:Hand = Hand()
        

    def draw_card(self):
        self.hand.deal()

class Dealer(Player):
    def __init__(self):
        super().__init__() 

    def play(self):
        while [0; 1]
        if self.hand.score[0] < 17:
            pass
        if self.hand.score[1] < 17:
            pass 
        if self.hand.score[0] > 21:
            pass
        if self.hand.score[1] > 21:
            pass
        else:
            pass
       