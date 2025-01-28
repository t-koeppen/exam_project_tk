import streamlit as st

def creator_page():
    st.header("About the Creator")

    c1, c2 = st.columns(2)

    with c1:
        st.write("Hi, I’m Tami. I’m into reading, movies, and "
                 "fashion. My interest in fashion is what sparked "
                 "the idea to build this app for a uni class.")

    with c2:
        st.image("images/Creator.png")