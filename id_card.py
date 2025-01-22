import streamlit as st
import pandas as pd

# Inizializza la lista per memorizzare i dati
if "data" not in st.session_state:
    st.session_state.data = []

# Bottone per mostrare la tabella
if st.button("Aggiungi Nickname e Numero"):
    # Crea i campi di input
    nickname = st.text_input("Inserisci il Nickname")
    numero = st.selectbox("Scegli un numero da 1 a 5", [1, 2, 3, 4, 5])

    # Aggiungi i dati alla lista se il nickname non è vuoto
    if nickname:
        st.session_state.data.append({"Nickname": nickname, "Numero": numero})

# Se ci sono dati, mostra la tabella
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.write("Tabellina dei Nickname e Numeri:")
    st.dataframe(df)
