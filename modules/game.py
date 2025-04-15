from modules.deck import Deck
from modules.player import Dealer,Human_player

class Game:
    def __init__(self, number_of_decks):
        self.deck: Deck = Deck(number_of_decks)
        self.dealer: Dealer = Dealer()
        self.human_player: Human_player = Human_player()
        self.money_betted: int = 0
        self.victory:bool = False

    def begin_game(self):
        self.deck.shuffle()
        self.human_player.draw_card(self.deck) 
        self.dealer.draw_card(self.deck)
        self.human_player.draw_card(self.deck) 
        self.dealer.draw_card(self.deck)

    def next_hand(self):
        self.human_player.hand.cards = []
        self.dealer.hand.cards = []
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

        if self.human_player.hand.score()[0] > 21:
            #print("Il giocatore ha sballato! Ha perso.")
            self.money_betted = 0
            self.victory = False

        elif self.dealer.hand.score()[0] > 21:
            #print("Il mazziere ha sballato! Il giocatore vince.")
            self.human_player.wallet += self.money_betted*2
            self.money_betted = 0
            self.victory = True

        elif self.dealer.hand.score()[1] <= 21:

            if self.dealer.hand.score()[1] < self.human_player.hand.score()[0] and self.human_player.hand.score()[0] <= 21:
                #print("Il giocatore vince.")
                self.human_player.wallet += self.money_betted*2
                self.money_betted = 0
                self.victory = True

            elif self.dealer.hand.score()[1] < self.human_player.hand.score()[1] and self.human_player.hand.score()[1] <= 21:
                #print("Il giocatore vince.")
                self.human_player.wallet += self.money_betted*2
                self.money_betted = 0
                self.victory = True

            else:
                #print("Il giocatore ha perso.")
                self.money_betted = 0
                self.victory = False

        elif self.dealer.hand.score()[0] <= 21 and self.dealer.hand.score()[1] > 21:

            if self.dealer.hand.score()[0] < self.human_player.hand.score()[0] and self.human_player.hand.score()[0] <= 21:
                #print("Il giocatore vince.")
                self.human_player.wallet += self.money_betted*2
                self.money_betted = 0
                self.victory = True

            elif self.dealer.hand.score()[0] < self.human_player.hand.score()[1] and self.human_player.hand.score()[1] <= 21:
                #print("Il giocatore vince.")
                self.human_player.wallet += self.money_betted*2
                self.money_betted = 0
                self.victory = True

            else:
                #print("Il giocatore ha perso.")
                self.money_betted = 0
                self.victory = False

        else:
            #print("Il giocatore ha perso.")
            self.money_betted = 0
            self.victory = False
            