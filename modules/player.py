import streamlit as st
import numpy as np
from modules.deck import Deck
from modules.hand import Hand


class Player:
    def __init__(self):
        self.hand:Hand = Hand()
        

    def deal(self):
        self.hand.deal()