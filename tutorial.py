import streamlit as st
import numpy as np

if "show_video" not in st.session_state:
    st.session_state.show_video = False
with st.sidebar:
    if st.button("Tutorial"):
        st.session_state.show_video = not st.session_state.show_video
if st.session_state.show_video:
    st.title("Video YouTube in Streamlit")
    youtube_url = "https://www.youtube.com/watch?v=eyoh-Ku9TCI"
    st.video(youtube_url, start_time=0)


