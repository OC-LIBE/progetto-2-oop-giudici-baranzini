import streamlit as st
# Title of the app
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
