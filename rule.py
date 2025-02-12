import streamlit as st
class rules:
  # **Blackjack Game Rules**

  ### **Objective of the Game**
  Blackjack is a card game played between a number of players and a dealer. The objective of the game is to achieve a total card value that is **as close as possible to 21** without exceeding it. If a player goes over 21, they automatically lose the hand (known as a "bust").

  ### **Card Values**
  - **Number cards** (2-10) are worth their face value.
  - **Face cards** (Jack, Queen, King) are worth 10 points each.
  - **Ace** can be worth either 1 or 11 points, depending on which value is most beneficial for the player.

  ### **Dealing the Cards**
  1. Each player receives two cards face up (visible only to them), and the dealer receives one card face up (visible to everyone) and one card face down (known as the "hole card").
  2. If a player is dealt a **Blackjack** (an Ace and a 10-point card, such as a 10, Jack, Queen, or King) in the first two cards, they win automatically with a payout of 3:2, unless the dealer also has a Blackjack, in which case the hand is a **push**.

  ### **Gameplay**
  - **Player’s Turn**:
    1. The player can choose to **"Hit"** (request another card) to increase their total.
    2. The player can choose to **"Stand"** (keep their current total) and not take any more cards.
    3. The player can choose to **"Double Down"**, which doubles their initial bet and allows them to receive only one more card.
    4. If the player has two cards of the same value, they can **"Split"** them into two separate hands, doubling their bet. Each hand is then played separately, and one card is dealt to each new hand.
    
  - **Dealer’s Turn**:
    1. After all players have completed their turns, the dealer plays their hand.
    2. The dealer must **"Hit"** until they have at least 17 points.
    3. If the dealer goes over 21 points, all players who have not already busted win.
    4. If the dealer has 17 or more points, they must **"Stand"**.

  ### **Scoring**
  - If a player has a total score of 21 or less, the game proceeds to the comparison between the dealer’s and the player’s hands.
  - If a player’s total exceeds 21, they automatically lose (bust).
  - The dealer’s score is compared to the player’s:
    - If the dealer has a higher score, the dealer wins.
    - If the player has a higher score, the player wins.
    - If both the dealer and the player have the same score, it is a tie (push), and the player keeps their bet.

  ### **Payouts**
  - **Regular Win:** In the case of a win, the player receives their original bet back.
  - **Blackjack:** A winning Blackjack is paid at **3:2** (e.g., a bet of £10 wins £15).
  - **Push:** In the event of a tie between the player and dealer, the player receives their original bet back.
  - **Doubling Down:** If a player doubles down, the payout is **1:1** on the original bet.