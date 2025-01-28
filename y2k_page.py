import streamlit as st
from helpers import reset

def y2k_page():
    st.get_option("theme.backgroundColor")

    st.image("images/y2k_header.png")
    st.header("2000s")

    st.subheader("Trends")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("The early 2000s fashion was a bold blend of eclectic styles, from low-rise jeans and crop "
                    "tops to velour tracksuits and metallics. Influenced by pop icons and Y2K culture, this era "
                    "embraced vibrant, daring looks that broke fashion norms, leaving a lasting impact on contemporary "
                    "style.")

    with c2:
        st.image("images/y2k_trends.png")

    st.subheader("Tops")

    c3, c4 = st.columns(2)

    with c3:
        st.markdown("For tops: you can wear baby tees with a print or messages, tank tops or off the shoulder "
                    "pullovers. Layered shirts and zip-up hoodies were frequently worn during that time as well. "
                    "Especially men wore loose-fitting or oversized hoodies, pullovers, t-shirts and sports jerseys.")

    with c4:
        st.image("https://i.pinimg.com/736x/89/86/10/898610a00753fe5c3e603d25a4cbea86.jpg")

    st.subheader("Bottoms")

    c5, c6 = st.columns(2)

    with c5:
        st.markdown("Low or mid waistlines are very popular for the 2000s style. Capri pants, baggy jeans or "
                    "tracksuit pants were frequently worn by stars of that time. If you feel comfortable, a mini "
                    "skirt is always a good staple for your outfit. As Paris Hilton said: Skirts should be the "
                    "size of a belt.")

    with c6:
        st.image("images/y2k_bottomss.png")

    st.subheader("Accessories & Shoes")

    c7, c8 = st.columns(2)

    with c7:
        st.markdown("Trucker or bucket hats, baseball caps and baker boy hats will complement your look. Use baguette "
                    "bags to store your belongings. Thin scarves, belly chains and hoops are perfect accessories. "
                    "Add shield sunglasses on sunny days. And for shoes: you can wear (platform) flip flops in the "
                    "summer while over-the-knee boots are better suited for the colder days. Sneakers or a kitten heel "
                    "work all year round.")

    with c8:
        # placing an image using a container
        with st.container():
            st.image("images/y2k_shoes.png")

    reset()