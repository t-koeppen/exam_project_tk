import streamlit as st
from y2k_page import y2k_page
from goth_page import goth_page
from coastal_page import coastal_page
from academia_page import academia_page

def overview_styles():
    # launch the home page
    # initialize session state value
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    def homepage():
        # create a container with an introduction to the overview about the styles page
        placeholder0 = st.empty()
        container0 = placeholder0.container()

        container0.image("images/styles_header.png")

        container0.markdown("Here you will find a selection of "
                            "different styles. Simply click on the "
                            "style button below the image and you will"
                            " be taken to a page with information on"
                            " the respective style.")

        # create a first page - define number of columns
        c1, c2, c3, c4 = st.columns(4)

        with c1:
            # create a placeholder and container
            placeholder1 = st.empty()
            container1 = placeholder1.container()

            container1.image("https://i.pinimg.com/736x/c9/0e/b8/c90eb8428f7c0e9571aa3ae71dd5cd69.jpg")
            c1_button = container1.button("2000s")

            if c1_button:
                st.session_state.counter = 1

        with c2:
            # create a placeholder and container
            placeholder2 = st.empty()
            container2 = placeholder2.container()

            container2.image("https://i.pinimg.com/736x/1a/f4/a6/1af4a6aab0c4cf43fa59714657b169c5.jpg")
            c2_button = container2.button("Goth")

            if c2_button:
                st.session_state.counter = 2

        with c3:
            # create a placeholder and container
            placeholder3 = st.empty()
            container3 = placeholder3.container()

            container3.image("https://i.pinimg.com/474x/b6/a8/d8/b6a8d8960dddd298f5f4555aa4c5302f.jpg")
            c3_button = container3.button("Coastal Granddaughter")

            if c3_button:
                st.session_state.counter = 3

        with c4:
            # create a placeholder and container
            placeholder4 = st.empty()
            container4 = placeholder4.container()

            container4.image("https://i.pinimg.com/736x/75/29/61/752961add70a01bafad1683ab7cc06d8.jpg")
            c4_button = container4.button("Academia")

            if c4_button:
                st.session_state.counter = 4

        if st.session_state.counter == 1:
            placeholder0.empty()
            placeholder1.empty()
            placeholder2.empty()
            placeholder3.empty()
            placeholder4.empty()

            # place y2k page
            y2k_page()

        if st.session_state.counter == 2:
            placeholder0.empty()
            placeholder1.empty()
            placeholder2.empty()
            placeholder3.empty()
            placeholder4.empty()
            # activate next page
            goth_page()

        if st.session_state.counter == 3:
            placeholder0.empty()
            placeholder1.empty()
            placeholder2.empty()
            placeholder3.empty()
            placeholder4.empty()

            # activate next page
            coastal_page()

        if st.session_state.counter == 4:
            placeholder0.empty()
            placeholder1.empty()
            placeholder2.empty()
            placeholder3.empty()
            placeholder4.empty()

            # activate next page
            academia_page()


    if st.session_state.counter == 0:
        homepage()