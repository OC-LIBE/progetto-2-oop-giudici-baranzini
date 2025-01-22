import streamlit as st
    tutorial_clicked = st.button("Tutorial")
if tutorial_clicked:
    st.title("Video YouTube in Streamlit")
    youtube_url = "https://www.youtube.com/watch?v=eyoh-Ku9TCI"
    st.video(youtube_url, start_time=0)