import streamlit as st
#from modules.rule import rules

if "show_game" not in st.session_state:
    st.session_state.show_game = False
if "show_profile" not in st.session_state:
    st.session_state.show_profile = False
if "nickname" not in st.session_state:
    st.session_state.nickname = ""
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "bet_value" not in st.session_state:
    st.session_state.bet_value = 100 
if "show_video" not in st.session_state:
    st.session_state.show_video = False
if "selected_number" not in st.session_state:
    st.session_state.selected_number = 1
if "show_rules" not in st.session_state:
    st.session_state.show_rules = False 


number_images = {
    1: "chi.png", 
    2: "text=2",  
    3: "http3",  
    4: "httpst=4",  
    5: "httpxt=5" 
}

with st.sidebar:
    if st.button("Table"):
        st.session_state.show_game = not st.session_state.show_game
        st.session_state.show_profile = True
        st.session_state.game_started = False  # Resetta lo stato del gioco

    if st.button("Tutorial"):
        st.session_state.show_video = not st.session_state.show_video
        
    if st.button("Rules"):
        st.session_state.show_rules = not st.session_state.show_rules

if st.session_state.show_video:
    st.title("YouTube Video in Streamlit")
    youtube_url = "https://www.youtube.com/watch?v=eyoh-Ku9TCI"
    st.video(youtube_url, start_time=0)

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

    # Scoring
    st.header("🧮 Scoring")
    st.markdown("""
    - If a player's total exceeds **21**, they **bust** and lose automatically.
    - After all players have finished, the dealer's hand is compared to the players':
      - If the dealer has a higher score, the **dealer wins**.
      - If the player has a higher score, the **player wins**.
      - If both have the same score, it's a **push** (tie), and the player keeps their bet.
    """)

    # Payouts
    st.header("💸 Payouts")
    st.markdown("""
    - **Regular Win:** Player receives their original bet back.
    - **Blackjack Win:** Paid at **3:2** (e.g., a £10 bet wins £15).
    - **Push:** Player gets their original bet back.
    - **Double Down:** Payout is **1:1** on the original bet.
    """)

    # Footer
    st.markdown("---")
    st.markdown("Enjoy your game of Blackjack! 🎲")

 

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

        values = list(range(10, 500, 10)) + \
                 list(range(500, 1000, 25)) + \
                 list(range(1000, 2500, 50)) + \
                 list(range(2500, 5001, 100))

        st.session_state.bet_value = st.slider(
            "Place a bet", min_value=min(values), max_value=max(values),
            step=10, value=st.session_state.bet_value
        )

        st.write("Your bet is:", st.session_state.bet_value)

        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(number_images[st.session_state.selected_number], caption="Your Number", use_column_width=True)

if st.session_state.nickname:
    st.write(f"👤 **Nickname:** {st.session_state.nickname}")
