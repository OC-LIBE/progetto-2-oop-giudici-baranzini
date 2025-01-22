from modules.card import Card
from modules.deck import Deck

class Hand:
    def __init__(self,deck):
        self.cards: list[Card] = []
        self.deck: Deck = deck
        self.cards_score: list[float] = [[].append(Card.card_scores) for Card in self.cards]   #attenzione
        self.score: float = sum(self.cards_score)
  

    def deal(self):
        self.cards.append(self.deck.draw())