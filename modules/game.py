from modules.deck import Deck
from modules.player import Dealer,Human_player

class Game:
    def __init__(self, number_of_decks):
        self.deck: Deck = Deck(number_of_decks)
        self.dealer: Dealer = Dealer()
        self.human_player: Human_player = Human_player()
        self.state = 1
    
import streamlit as st

# Inizializza variabili di sessione con un'unica funzione
def init_session_state():
    defaults = {
        "show_game": False,
        "show_profile": False,
        "nickname": "",
        "game_started": False,
        "bet_value": 100,
        "show_video": False,
        "selected_number": 1
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

init_session_state()

# Dizionario immagini associate ai numeri
number_images = {
    i: f"https://via.placeholder.com/150/{color}/FFFFFF?text={i}" 
    for i, color in zip(range(1, 6), ["FF0000", "00FF00", "0000FF", "FFFF00", "FF00FF"])
}

# Sidebar - Navigazione
with st.sidebar:
    if st.button("Table"):
        st.session_state.show_game = not st.session_state.show_game
        st.session_state.show_profile = True
        st.session_state.game_started = False  # Resetta lo stato del gioco

    if st.button("Tutorial"):
        st.session_state.show_video = not st.session_state.show_video

# Mostra il video tutorial
if st.session_state.show_video:
    st.title("🎥 Tutorial Video")
    st.video("https://www.youtube.com/watch?v=eyoh-Ku9TCI")

# Funzione per la creazione del profilo
def create_profile():
    st.subheader("👤 Create Your Profile")
    nickname = st.text_input("Enter your Nickname")
    selected_number = st.selectbox("Choose a number", list(number_images.keys()))

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Confirm") and nickname:
            st.session_state.nickname = nickname
            st.session_state.selected_number = selected_number
            st.session_state.show_profile = False
            st.rerun()

    with col2:
        if st.button("Cancel"):
            st.session_state.show_profile = False
            st.rerun()

# Funzione per la gestione del gioco
def start_game():
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

# Funzione per il gioco attivo
def play_game():
    st.write("🃏 **Game begun!**")
    
    # Slider per la scommessa
    st.session_state.bet_value = st.slider(
        "💰 Place a bet",
        min_value=10, max_value=5000, step=10,
        value=st.session_state.bet_value
    )
    st.write(f"Your bet is: **{st.session_state.bet_value}**")

    # Mostra l'immagine del numero scelto
    st.image(number_images[st.session_state.selected_number], caption="Your Number", width=150)

# Avvio della schermata del gioco
if st.session_state.show_game:
    start_game()

# Mostra il nickname se disponibile
if st.session_state.nickname:
    st.write(f"👤 **Nickname:** {st.session_state.nickname}")
