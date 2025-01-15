from modules.card import Card
from modules.deck import Deck


class Player:
    def __init__(self, deck):
        self.hand:list[Card] = []
        self.deck:Deck = deck

    def deal(self, deck):
        self.hand.append(deck.cards[0])