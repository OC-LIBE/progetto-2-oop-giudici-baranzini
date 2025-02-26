import streamlit as st
from rule import rl

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
    rl.show_rules()

# Display game interface if selected
if st.session_state.show_game:
    start_game()

# Display nickname with selected color if set
if st.session_state.nickname:
    nickname_color = color_options.get(st.session_state.selected_color, "#000000")
    st.markdown(f"<p style='color:{nickname_color}; font-weight:bold; font-size:20px;'>👤 {st.session_state.nickname}</p>", unsafe_allow_html=True)

