import streamlit as st

def reset():
    st.session_state.counter = 0
    st.button("Home", on_click=reset)