from modules.deck import Deck
from modules.hand import Hand


class Player:
    def __init__(self):
        self.hand:Hand = Hand()
        

    def draw_card(self):
        self.hand.deal()