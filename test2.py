import streamlit as st
from modules.game import Game
from modules.rule import rl


st.set_page_config(
   layout="wide",
)
card_width=105

def toggle_state(state_key):
    """Toggle a boolean session state value."""
    st.session_state[state_key] = not st.session_state[state_key]

def init_session_state():
    defaults = {
        "show_video": False,
        "show_rules": False  
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

if 'game' not in st.session_state:
    st.session_state.game = Game(6)

game = st.session_state.game

with st.sidebar:
    if st.button("Tutorial"):
        toggle_state("show_video")
    if st.button("Rules"):
        toggle_state("show_rules")

if st.session_state.show_video:
    st.title("Tutorial Video")
    st.video("https://www.youtube.com/watch?v=eyoh-Ku9TCI")

if st.session_state.show_rules:
    rl.show_rules()

@st.dialog("bet")
def place_bet():
    with st.form("bet", clear_on_submit = True):
        st.write("place a bet")
        bet_ammount = st.slider("💰 Place a bet", min_value=0, max_value=game.human_player.wallet, step=10,)
        
        submitted = st.form_submit_button("place the bet")
        if submitted:
            game.bet(bet_ammount)
            st.rerun()

deal_button = st.button("Begin game")
if deal_button:
      place_bet()
      game.begin_game()

hit_button = st.button("Hit")
if hit_button:
    game.hit()

stand_button = st.button("Stand")
if stand_button:
    game.dealer_play()
    game.control()

st.write("Yuor hand")
st.image([card.image for card in game.human_player.hand.cards], width=card_width)

st.write("Desler's hand")
st.image([card.image for card in game.dealer.hand.cards], width=card_width)

st.write(game.human_player.hand.score())
st.write(game.dealer.hand.score())
st.write(game.human_player.wallet)
st.write(game.money_betted)