import streamlit as st
from helpers import reset

def academia_page():
    st.image("https://i.pinimg.com/736x/7d/64/6f/7d646f2193eb8a5cb6c13a3758484a0d.jpg")
    st.header("Academia")

    st.subheader("Trends")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("The coastal granddaughter style is a fresh take on breezy, seaside fashion, blending timeless "
                    "coastal elements infused with a youthful twist. This style evokes a nostalgic, effortless "
                    "elegance, perfect for those who embrace a laid-back, beachy vibe with a modern, playful touch. "
                    "Prominent colours are navy or light blue, sandy beige, off-white, and seafoam green.")

    with c2:
        st.image("images/BabyTee.png")

    st.subheader("Tops")

    c3, c4 = st.columns(2)

    with c3:
        st.markdown(
            "For tops, coastal granddaughter's wear babydoll shirts, oversized button-ups paired with a tank "
            "top or t-shirt, linen blouses, cozy pullovers or cardigans. Midi sundresses are also popular.")

    with c4:
        st.image("https://i.pinimg.com/736x/89/86/10/898610a00753fe5c3e603d25a4cbea86.jpg")

    st.subheader("Bottoms")

    c5, c6 = st.columns(2)

    with c5:
        st.markdown(
            "Linen pants and denim shorts are frequently worn by those who dress in the coastal granddaughter "
            "style. Flowy skirts, and jeans are great options as well.")

    with c6:
        st.image("https://i.pinimg.com/736x/89/86/10/898610a00753fe5c3e603d25a4cbea86.jpg")

    st.subheader("Accessories & Shoes")

    c7, c8 = st.columns(2)

    with c7:
        st.markdown(
            "For shoes you should wear Birkenstock-style sandals. Sneakers are an amazing choice too. Coastal "
            "Granddaughters favour delicate jewelry. They wear necklaces, bracelets, and earrings - just don't "
            "overdo it. Other accessories that can be worn are a nice pair of sunnies or a baseball cap. Tote "
            "bags are great for storing your belongings.")

    with c8:
        # placing an image using a container
        with st.container():
            st.image("https://i.pinimg.com/736x/89/86/10/898610a00753fe5c3e603d25a4cbea86.jpg")

    reset()