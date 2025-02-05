import streamlit as st

# Inizializza variabili di sessione
if "show_game" not in st.session_state:
    st.session_state.show_game = False
if "show_profile" not in st.session_state:
    st.session_state.show_profile = False
if "nickname" not in st.session_state:
    st.session_state.nickname = ""
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "bet_value" not in st.session_state:
    st.session_state.bet_value = 100  # Valore predefinito della scommessa
if "show_video" not in st.session_state:
    st.session_state.show_video = False
if "selected_number" not in st.session_state:
    st.session_state.selected_number = 1  # Numero predefinito

# Dizionario che associa numeri a immagini
number_images = {
    1: "https://via.placeholder.com/150/FF0000/FFFFFF?text=1",  # Immagine rossa con "1"
    2: "https://via.placeholder.com/150/00FF00/FFFFFF?text=2",  # Immagine verde con "2"
    3: "https://via.placeholder.com/150/0000FF/FFFFFF?text=3",  # Immagine blu con "3"
    4: "https://via.placeholder.com/150/FFFF00/000000?text=4",  # Immagine gialla con "4"
    5: "https://via.placeholder.com/150/FF00FF/FFFFFF?text=5"   # Immagine viola con "5"
}

# Sidebar - Pulsanti per accedere al tavolo e al tutorial
with st.sidebar:
    if st.button("Table"):
        st.session_state.show_game = not st.session_state.show_game
        st.session_state.show_profile = True
        st.session_state.game_started = False  # Resetta lo stato del gioco

    if st.button("Tutorial"):
        st.session_state.show_video = not st.session_state.show_video

# Mostra il video tutorial se selezionato
if st.session_state.show_video:
    st.title("YouTube Video in Streamlit")
    youtube_url = "https://www.youtube.com/watch?v=eyoh-Ku9TCI"
    st.video(youtube_url, start_time=0)

# Gestione del gioco
if st.session_state.show_game:
    st.title("Welcome to the Table!!")

    if st.session_state.show_profile:
        with st.container():
            st.subheader("Create Your Profile")

            nickname = st.text_input("Enter your Nickname")
            st.session_state.selected_number = st.selectbox("Choose a number", list(number_images.keys()))

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Confirm"):
                    if nickname:
                        st.session_state.nickname = nickname
                        st.session_state.show_profile = False
                        st.rerun()

            with col2:
                if st.button("Cancel"):
                    st.session_state.show_profile = False
                    st.rerun()

    if not st.session_state.game_started:
        if st.button("Start Game"):
            st.session_state.game_started = True
            st.rerun()

    if st.session_state.game_started:
        st.write("Game begun")

        # Valori per la scommessa
        values = list(range(10, 500, 10)) + \
                 list(range(500, 1000, 25)) + \
                 list(range(1000, 2500, 50)) + \
                 list(range(2500, 5001, 100))

        # Usa slider invece di select_slider per evitare aggiornamenti continui
        st.session_state.bet_value = st.slider(
            "Place a bet", min_value=min(values), max_value=max(values),
            step=10, value=st.session_state.bet_value
        )

        st.write("Your bet is:", st.session_state.bet_value)

        # Mostra l'immagine selezionata in basso a sinistra
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(number_images[st.session_state.selected_number], caption="Your Number", use_column_width=True)

# Mostra il nickname salvato
if st.session_state.nickname:
    st.write(f"👤 **Nickname:** {st.session_state.nickname}")
