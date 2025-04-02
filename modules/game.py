from modules.deck import Deck
from modules.player import Dealer,Human_player

class Game:
    def __init__(self, number_of_decks):
        self.deck: Deck = Deck(number_of_decks)
        self.dealer: Dealer = Dealer()
        self.human_player: Human_player = Human_player()
        self.state = 1
        self.money_betted: int = 0

    def begin_game(self):
        self.deck.shuffle()
        self.human_player.draw_card(self.deck) 
        self.dealer.draw_card(self.deck)
        self.human_player.draw_card(self.deck) 
        self.dealer.draw_card(self.deck)

    def hit(self):
        self.human_player.draw_card(self.deck)

    def dealer_play(self):
        self.dealer.play(self.deck)

    def bet(self, bet_ammount):
        self.human_player.bet(bet_ammount)
        self.money_betted += bet_ammount

    def control(self):
        pass