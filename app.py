import streamlit as st
from modules.game import Game


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

if 'game' not in st.session_state:
    st.session_state.game = Game(number_of_decks)

game = st.session_state.game

st.markdown(f"## Deck created with {number_of_decks} deck/s")

st.image([card.image for card in game.deck.cards], width=card_width)

st.markdown("## Shuffling deck")
shuffle_button = st.button("Shuffle")
if shuffle_button:
    game.deck.shuffle()
st.image([card.image for card in game.deck.cards], width=card_width)


deal_button = st.button("Begin game")
if deal_button:
      game.begin_game()

play_button = st.button("play")
if play_button:
      game.dealer_play()

st.image([card.image for card in game.human_player.hand.cards], width=card_width)
st.image([card.image for card in game.dealer.hand.cards], width=card_width)

st.write(game.human_player.hand.score())
st.write(game.dealer.hand.score())




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