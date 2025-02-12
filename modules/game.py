from modules.deck import Deck
from modules.player import Dealer,Human_player

class Game:
    def __init__(self, number_of_decks):
        self.deck: Deck = Deck(number_of_decks)
        self.dealer: Dealer = Dealer()
        self.human_player: Human_player = Human_player()
        self.state = 1
    
