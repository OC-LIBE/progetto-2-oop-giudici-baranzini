from modules.card import Card

class Hand:
    def __init__(self):
        self.cards: list[Card] = []
  
    def add_card(self, deck):
        self.cards.append(deck.draw())

    def score(self):
        sums = [0,0]
        for card in self.cards:
            sums[0] += card.card_scores[0]
            sums[1] += card.card_scores[1]

        return sums 
