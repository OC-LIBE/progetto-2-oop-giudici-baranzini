import streamlit as st
from modules.game import Game


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

@st.dialog("bet")
def place_bet():
    with st.form("bet", clear_on_submit = True):
        st.write("place a bet")
        bet_ammount = st.slider("💰 Place a bet", min_value=0, max_value=game.human_player.wallet, step=10,)
        
        submitted = st.form_submit_button("place the bet")
        if submitted:
            game.bet(bet_ammount)
            st.rerun()

if st.button("bet"):
    place_bet()


st.image([card.image for card in game.human_player.hand.cards], width=card_width)
st.image([card.image for card in game.dealer.hand.cards], width=card_width)

st.write(game.human_player.hand.score())
st.write(game.dealer.hand.score())
st.write(game.human_player.wallet)
st.write(game.money_betted)