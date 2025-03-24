import streamlit as st

def creator_page():
    st.header("About the Creator")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("I admire a lot of different fashion styles. My personal favourites are 2000s styles, Sabrina "
                    "Carpenter’s “Emails I Can’t Send” era outfits, and basically everything Aria Montgomery is wearing"
                    " in season 1 and 2 of Pretty Little Liars.")
        st.markdown("I get my inspo from browsing pinterest, scrolling through TikTok, and from looking at the clothes"
                    "I was wearing as a child as well as looking what outfits I like of characters on TV. I'm by no "
                    "means a fashion expert, but I enjoy learning about new styles. That was part of the reason why I "
                    "decided on doing this style guide as my uni project.")
        st.markdown("xx, Tami💋")

    with c2:
        st.image("images/Creator.jpg")
        st.caption("That's me wearing one of my favourite pairs of jeans and a cute yellow pullover.")