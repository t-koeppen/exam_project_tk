import streamlit as st
from helpers import reset

def coastal_page():
    st.image("images/CoastalHeader.jpg")
    st.header("Coastal Granddaughter")

    st.subheader("Trends")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("The coastal granddaughter style is a fresh take on breezy, seaside fashion, blending timeless "
                    "coastal elements infused with a youthful twist. This style evokes a nostalgic, effortless "
                    "elegance, perfect for those who embrace a laid-back, beachy vibe with a modern, playful touch. "
                    "Prominent colours are navy or light blue, sandy beige, off-white, and seafoam green.")

    with c2:
        st.image("images/CoastalTrends.png")

    st.subheader("Tops")

    c3, c4 = st.columns(2)

    with c3:
        st.markdown("For tops, coastal granddaughter's wear babydoll shirts, oversized button-ups paired with a tank "
                    "top or t-shirt, linen blouses, cozy pullovers or cardigans. Midi sundresses are also popular.")

    with c4:
        st.image("images/CoastalTops.png")

    st.subheader("Bottoms")

    c5, c6 = st.columns(2)

    with c5:
        st.markdown("Linen pants and denim shorts are frequently worn by those who dress in the coastal granddaughter "
                    "style. Flowy skirts, and jeans are great options as well.")

    with c6:
        st.image("images/CoastalBottoms.png")

    st.subheader("Accessories & Shoes")

    c7, c8 = st.columns(2)

    with c7:
        st.markdown("For shoes you should wear Birkenstock-style sandals. Sneakers are an amazing choice too. Coastal "
                    "Granddaughters favour delicate jewelry. They wear necklaces, bracelets, and earrings - just don't "
                    "overdo it. Other accessories that can be worn are a nice pair of sunnies or a baseball cap. Tote "
                    "bags are great for storing your belongings.")

    with c8:
        # placing an image using a container
        with st.container():
            st.image("images/CoastalShoes.png")

    reset()