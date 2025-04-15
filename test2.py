import streamlit as st
from modules.game import Game
from streamlit_extras.let_it_rain import rain


st.set_page_config(
   layout="wide",
)
card_width=105

def toggle_state(state_key):
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

    st.title("🃏 Blackjack Game Rules")

    st.header("🎯 Objective of the Game")
    st.write("""
    Blackjack is a card game played between players and a dealer. The objective is to achieve a total card value that is **as close as possible to 21** without exceeding it. 
    If a player exceeds 21, they automatically lose the hand (this is known as a **bust**).
    """)

    st.header("🃎 Card Values")
    st.markdown("""
    - **Number cards** (2-10) are worth their face value.
    - **Face cards** (Jack, Queen, King) are worth **10 points** each.
    - **Ace** can be worth **1** or **11** points, depending on which value benefits the player the most.
    """)

    st.header("🃏 Dealing the Cards")
    st.markdown("""
    - Each player receives **two cards face up** (visible to them), while the dealer receives **one card face up** and **one card face down** (the "hole card").
    - If a player is dealt a **Blackjack** (an Ace and a 10-point card), they win automatically with a payout of **3:2**, unless the dealer also has a Blackjack, resulting in a **push** (a tie).
    """)

    st.header("🎮 Gameplay")

    st.subheader("Player’s Turn")
    st.markdown("""
    - **Hit** – Request another card to increase your total.
    - **Stand** – Keep your current total and end your turn.
    - **Double Down** – Double your bet and receive only **one more card**.
    - **Split** – If you have two cards of the same value, split them into two hands, doubling your bet. Each hand is played separately.
    """)

    st.subheader("Dealer’s Turn")
    st.markdown("""
    - After all players finish, the dealer plays their hand.
    - The dealer must **Hit** until they reach at least **17 points**.
    - If the dealer exceeds **21 points**, all remaining players win.
    - If the dealer has **17 or more points**, they must **Stand**.
    """)

    st.header("🧮 Scoring")
    st.markdown("""
    - If a player's total exceeds **21**, they **bust** and lose automatically.
    - After all players have finished, the dealer's hand is compared to the players':
    - If the dealer has a higher score, the **dealer wins**.
    - If the player has a higher score, the **player wins**.
    - If both have the same score, it's a **push** (tie), and the player keeps their bet.
    """)

    st.header("💸 Payouts")
    st.markdown("""
    - **Regular Win:** Player receives their original bet back.
    - **Blackjack Win:** Paid at **3:2** (e.g., a £10 bet wins £15).
    - **Push:** Player gets their original bet back.
    - **Double Down:** Payout is **1:1** on the original bet.
    """)

    st.markdown("---")
    st.markdown("Enjoy your game of Blackjack! 🎲")


@st.dialog("bet")
def place_bet():
    with st.form("bet", clear_on_submit = True):
        st.write("place a bet")
        bet_ammount = st.slider("💰 Place a bet", min_value=0, max_value=game.human_player.wallet, step=10,)
        
        submitted = st.form_submit_button("place the bet")
        if submitted:
            game.bet(bet_ammount)
            st.rerun()

begin_button = st.button("Begin game")
if begin_button:
    place_bet()
    game.begin_game()

st.write("Your hand:")
st.image([card.image for card in game.human_player.hand.cards], width=card_width)
st.write(f"You have {game.human_player.wallet} money left")

hit_button = st.button("Hit")
if hit_button:
    game.hit()
    st.rerun()

stand_button = st.button("Stand")
if stand_button:
    game.dealer_play()
    game.control()
    if game.victory == True:
        rain(
            emoji="💸",
            font_size=54,
            falling_speed=10,
            animation_length=5,
            )
        
    else:
        rain(
            emoji="😭",
            font_size=54,
            falling_speed=10,
            animation_length=5,
            )
     

st.write("Dealer's hand:")
st.image([card.image for card in game.dealer.hand.cards], width=card_width)

next_hand_button = st.button("Next hand")
if next_hand_button:
    place_bet()
    game.next_hand()

#st.write(game.human_player.hand.score())
#st.write(game.dealer.hand.score())
#st.write(game.human_player.wallet)
#st.write(game.money_betted)