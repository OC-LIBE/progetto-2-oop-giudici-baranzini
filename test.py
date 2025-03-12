import streamlit as st
from streamlit_extras.let_it_rain import rain


if st.button("Fai piovere emoji!"):
    rain(
        emoji="💸",
        font_size=54,
        falling_speed=10,
        animation_length=5,
    )



st.button("", help="")

st.button("Deal", help="Let's go gambling!")

st.button("Hit", help="+1 card")

st.button("Stand", help="No more cards, just check!")

st.button("split", help="split your hand")

st.button("double", help="get only one more card and double the bet")
    