import streamlit as st
from helpers import reset

def academia_page():
    st.image("images/AcademiaHeader.jpg")
    st.header("Academia")

    st.subheader("Trends")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("The academia style blends vintage elegance with intellectual allure. Dark Academia channels moody "
                    "sophistication with rich tones and Gothic influences, while Light Academia offers a softer, sunlit "
                    "take, featuring neutral hues and romantic silhouettes. Both embody a timeless passion for knowledge "
                    "and appreciation of classic style.")

    with c2:
        st.image("images/AcademiaTrends.png")

    st.subheader("Tops")

    c3, c4 = st.columns(2)

    with c3:
        st.markdown("Blouses or button-up shirts are essential staples for the academia style. You can pair them with a "
                    "sweater vest or blazer. Turtle necks and argyle pullovers are more casual tops. On colder days, "
                    "a coat can be worn. ")

    with c4:
        st.image("images/AcademiaTops.png")

    st.subheader("Bottoms")

    c5, c6 = st.columns(2)

    with c5:
        st.markdown("To achieve the academia style, you should wear corduroy trousers or suit pants. A skirt with black "
                    "tights is a good option as well.")

    with c6:
        st.image("images/AcademiaBottoms.png")

    st.subheader("Accessories & Shoes")

    c7, c8 = st.columns(2)

    with c7:
        st.markdown("For shoes you should wear Oxford shoes, shoes in the Mary Jane style or some boots. A tie, a "
                    "wristwatch or pocket watch, and some hair accessories, like a beret or hairband, will complete "
                    "your academia style. Glasses are good as well.")

    with c8:
        # placing an image using a container
        with st.container():
            st.image("images/AcademiaShoes.png")

    reset()