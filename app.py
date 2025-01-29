import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.hand import Hand
from modules.player import Player


#with st.sidebar:
    #tutorial_clicked = st.button("Tutorial")
#if tutorial_clicked:
#    st.title("Video YouTube in Streamlit")
#    youtube_url = "https://www.youtube.com/watch?v=eyoh-Ku9TCI"
#    st.video(youtube_url, start_time=0)

st.set_page_config(
   layout="wide",
)
card_width=105


number_of_decks = st.number_input("Number of decks", min_value=1, max_value=10, value=1)

deck = Deck(number_of_decks)
hand = Hand(deck)
player = Player(deck, hand)

st.markdown(f"## Deck created with {number_of_decks} deck/s")

st.image([card.image for card in deck.cards], width=card_width)

st.markdown("## Shuffling deck")
shuffle_button = st.button("Shuffle")
if shuffle_button:
    deck.shuffle()
st.image([card.image for card in deck.cards], width=card_width)


deal_button = st.button("Deal")
if deal_button:
    player.deal()    #attenzione
st.image([card.image for card in player.hand.cards], width=card_width)
st.write(hand.score)



## Deal 
#st.button("Deal", help="Let's go gambling!", type="secondary")

## hit
#st.button("Hit", help="+1 card", type="secondary")
#layer.hand =+1 card

## stand
#st.button("Stand", help="No more cards, just check!", type="secondary")
#heck result



## x2

## split

## bet