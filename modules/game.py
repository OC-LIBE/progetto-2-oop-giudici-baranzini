from modules.deck import Deck
from modules.player import Dealer,Human_player

class Game:
    def __init__(self, number_of_decks):
        self.deck: Deck = Deck(number_of_decks)
        self.dealer: Dealer = Dealer()
        self.human_player: Human_player = Human_player()
        self.state = 1

    def begin_game(self):
        self.human_player.draw_card(self.deck) 
        self.dealer.draw_card(self.deck)
        self.human_player.draw_card(self.deck) 
        self.dealer.draw_card(self.deck)

    def hit(self):
        self.human_player.draw_card(self.deck)

    def dealer_play(self):
        self.dealer.play(self.deck)
    
"""
import streamlit as st
# Inizializza variabili di sessione con un'unica funzione
    

import streamlit as st

def init_session_state():
    """Initialize session state variables with default values."""
    defaults = {
        "show_game": False,
        "show_profile": False,
        "nickname": "",
        "game_started": False,
        "bet_value": 100,
        "show_video": False,
        "selected_color": "Red",
        "show_rules": False  # Added to avoid potential KeyError
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def toggle_state(state_key):
    """Toggle a boolean session state value."""
    st.session_state[state_key] = not st.session_state[state_key]

def create_profile():
    """Display profile creation form."""
    st.subheader("Create Your Profile")
    nickname = st.text_input("Enter your Nickname")
    
    # Ensure color_options is defined before use
    if "color_options" in globals():
        selected_color = st.radio("Choose a color", list(color_options.keys()))
    else:
        selected_color = "Red"
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Confirm") and nickname:
            st.session_state.update({
                "nickname": nickname,
                "selected_color": selected_color,
                "show_profile": False
            })
            st.rerun()
    
    with col2:
        if st.button("Cancel"):
            st.session_state.show_profile = False
            st.rerun()

def play_game():
    """Display game UI once started."""
    st.write("🃏 **Game begun!**")
    
    st.session_state.bet_value = st.slider(
        "💰 Place a bet", min_value=10, max_value=5000, step=10,
        value=st.session_state.bet_value
    )
    st.write(f"Your bet is: **{st.session_state.bet_value}**")

def start_game():
    """Display game interface."""
    st.title("🎲 Welcome to the Table!")
    
    if st.session_state.show_profile:
        create_profile()
    else:
        if not st.session_state.game_started:
            if st.button("Start Game"):
                st.session_state.game_started = True
                st.rerun()
        else:
            play_game()

# Initialize session state
init_session_state()

# Dictionary of color options
color_options = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Yellow": "#FFFF00",
    "Purple": "#800080"
}

# Sidebar controls
with st.sidebar:
    if st.button("Table"):
        st.session_state.update({"show_game": not st.session_state.show_game, "show_profile": True, "game_started": False})
    if st.button("Tutorial"):
        toggle_state("show_video")
    if st.button("Rules"):
        toggle_state("show_rules")

# Display tutorial video if selected
if st.session_state.show_video:
    st.title("Tutorial Video")
    st.video("https://www.youtube.com/watch?v=eyoh-Ku9TCI")

# Display game or profile creation
if st.session_state.show_rules:
    st.title("🃏 Blackjack Game Rules")
    
    # Objective of the Game
    st.header("🎯 Objective of the Game")
    st.write("""
    Blackjack is a card game played between players and a dealer. The objective is to achieve a total card value that is **as close as possible to 21** without exceeding it. 
    If a player exceeds 21, they automatically lose the hand (this is known as a **bust**).
    """)
    
    # Card Values
    st.header("🃎 Card Values")
    st.markdown("""
    - **Number cards** (2-10) are worth their face value.
    - **Face cards** (Jack, Queen, King) are worth **10 points** each.
    - **Ace** can be worth **1** or **11** points, depending on which value benefits the player the most.
    """)
    
    # Dealing the Cards
    st.header("🃏 Dealing the Cards")
    st.markdown("""
    - Each player receives **two cards face up** (visible to them), while the dealer receives **one card face up** and **one card face down** (the "hole card").
    - If a player is dealt a **Blackjack** (an Ace and a 10-point card), they win automatically with a payout of **3:2**, unless the dealer also has a Blackjack, resulting in a **push** (a tie).
    """)
    
    # Gameplay
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
    
    # Payouts
    st.header("💸 Payouts")
    st.markdown("""
    - **Regular Win:** Player receives their original bet back.
    - **Blackjack Win:** Paid at **3:2** (e.g., a £10 bet wins £15).
    - **Push:** Player gets their original bet back.
    - **Double Down:** Payout is **1:1** on the original bet.
    """)
    
    st.markdown("---")
    st.markdown("Enjoy your game of Blackjack! 🎲")

# Display game interface if selected
if st.session_state.show_game:
    start_game()

# Display nickname with selected color if set
if st.session_state.nickname:
    nickname_color = color_options.get(st.session_state.selected_color, "#000000")
    st.markdown(f"<p style='color:{nickname_color}; font-weight:bold; font-size:20px;'>👤 {st.session_state.nickname}</p>", unsafe_allow_html=True)

    st.write(f"👤 **Nickname:** {st.session_state.nickname}")
"""
