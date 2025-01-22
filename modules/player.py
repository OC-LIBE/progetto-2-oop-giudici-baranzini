from modules.deck import Deck
from modules.hand import Hand


class Player:
    def __init__(self, deck, hand):
        self.hand:Hand = hand
        self.deck:Deck = deck

    def deal(self):
        self.hand.deal()