import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player

st.set_page_config(
   layout="wide",
)
card_width=105


number_of_decks = st.number_input("Number of decks", min_value=1, max_value=10, value=1)

deck = Deck(number_of_decks)
player = Player(deck)

st.markdown(f"## Deck created with {number_of_decks} deck/s")

st.image([card.image for card in deck.cards], width=card_width)

st.markdown("## Shuffling deck")
shuffle_button = st.button("Shuffle")
if shuffle_button:
    deck.shuffle()
st.image([card.image for card in deck.cards], width=card_width)

st.write(st.session_state)
deal_button = st.button("Deal")
if deal_button:
    player.deal(deck)    #attenzione
st.image([card.image for card in player.hand], width=card_width)


## Deal 
st.button("Deal", help="Let's go gambling!", type="secondary")

## hit
st.button("Hit", help="+1 card", type="secondary")
player.hand =+1 card

## stand
st.button("Stand", help="No more cards, just check!", type="secondary")
check result



## x2

## split

## bet