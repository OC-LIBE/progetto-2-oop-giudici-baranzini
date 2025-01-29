from modules.card import Card
from modules.deck import Deck

class Hand:
    def __init__(self):
        self.cards: list[Card] = []
  
    def add_card(self, deck):
        self.cards.append(deck.draw())

    @property
    def score(self):
        sums = [0,0]
        for i in range(len(self.cards)):
            sums[0] =+ self.cards[i].card_scores[0]
            sums[1] =+ self.cards[i].card_scores[1]

        return sums 
