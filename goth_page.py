import streamlit as st
from helpers import reset

def goth_page():
    st.image("images/GothHeader.jpg")
    st.header("Goth")

    st.subheader("Trends")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("You might not think so, but goth style is very versatile. From trad goth to cyber goth, as well as "
                    "Victorian and romantic goth there are quite a few sub-groups within the style. All of them wear "
                    "black (maybe another dark colour) as the basis of their outfit. The dark clothes can be accompanied "
                    "by some light or colourful highlights. Eyeliner is a must to get the goth makeup, other than that, "
                    "the make-up is quite versatile as well. You can go all out with a white foundation, sharp contour, "
                    "thin eyebrows, heavy eye makeup, and dark lips or you can keep everything a bit more low-key.")

    with c2:
        st.image("images/GothTrends.png")

    st.subheader("Tops")

    c3, c4 = st.columns(2)

    with c3:
        st.markdown("Ruffle shirts, corsets and fishnet tops as well as blouses with a high collar are tops frequently "
                    "worn by goths. For jackets, you can opt for a leather jacket or blazer, accessorized with pins "
                    "of your favourite bands or artists (maybe Bauhaus, The Cure or Siouxsie Sioux).")

    with c4:
        st.image("images/GothTops.png")

    st.subheader("Bottoms")

    c5, c6 = st.columns(2)

    with c5:
        st.markdown("Harem or bondage trousers can be worn for your goth outfit. Every other dark pair of pants will "
                    "do the trick as well. If you like skirts, a mini skirt paired with ripped tights (or tights with "
                    "a dark print) is an option, as well as mid-length ruffled skirts, dark lolita skirts or Victorian "
                    "skirts - whatever style you prefer.")

    with c6:
        st.image("images/GothBottoms.png")

    st.subheader("Accessories & Shoes")

    c7, c8 = st.columns(2)

    with c7:
        st.markdown("Goths wear Doc Martens, combat or platform boots, and pointy shoes - flats or boots, whatever you "
                    "prefer. Maybe they have some studs or charms. For accessories wear chunky statement necklaces, "
                    "velvet or spiked chokers or beaded cathedral necklaces. Wear mismatched earrings and a chain belt  "
                    "or a studded belt. Just make sure to layer a lot and use silver jewelry!")

    with c8:
        # placing an image using a container
        with st.container():
            st.image("images/GothShoes.png")

    reset()