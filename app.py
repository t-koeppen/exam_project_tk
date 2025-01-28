import streamlit as st
from introduction_page import introduction_page
from overview_styles import overview_styles
from chatbot import chatbot
from creator_page import creator_page

st.set_page_config(page_icon="🎀",
                   page_title="Style Guide")

# create a side bar with different pages
options = ['Introduction', 'Styles', 'Chat', 'Community', 'About The Creator']
page_selection = st.sidebar.selectbox("Menu", options)

# when the user selects a page, we want to show something
if page_selection == "Introduction":
    introduction_page()
elif page_selection == "Styles":
    overview_styles()
elif page_selection == "About The Creator":
    creator_page()
elif page_selection == "Chat":
    chatbot()
else:
        st.write("WORK IN PROGRESS")