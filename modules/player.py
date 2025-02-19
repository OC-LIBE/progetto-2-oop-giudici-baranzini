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


class Dealer(Player):
    def __init__(self):
        super().__init__() 

    def play(self,deck):
        while self.hand.score[0] < 17:
            while self.hand.score[1] < 17 or self.hand.score[1] > 21:    #attenzione
                self.draw_card(deck) 
        
       