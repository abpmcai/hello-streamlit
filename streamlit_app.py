import streamlit as st

number = st.slider("Pick a number", 0, 100)

if number == 25:
  st.write("Good Job!")
