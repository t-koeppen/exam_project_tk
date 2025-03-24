import streamlit as st

def tips_page():
    st.image("images/TipsHeader.jpg")
    st.header("Tips")

    st.markdown("In the following I will present you some tips that can help you with styling outfits.")

    st.subheader("Shapes")

    st.markdown("When recreating an outfit you’ve seen, it’s not just important to match the colours of your outfit to "
                    "your inspo but also the shapes. As @justmacrose explains in her TikTok Video, clothes can have similar "
                    "colors to an inspo outfit, but the overall look will still not be the same, if the shapes don’t match "
                    "the inspiration.")

    st.subheader("Accessories")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("Don’t hold back with accessorizing your outfits! Accessories can evaluate an outfit, make it more "
                    "interesting, and tie everything together. Accessories can include styling your hair, and make-up if you "
                    "like to wear it. Wear jewelry, belts, hair clips, scarves, hats, bags, glasses, maybe some fake tattoos - "
                    "whatever you like. Don’t be afraid to overdo it or to mix medals. You can repurpose accessories and wear "
                    "them in a way they weren’t originally intended to be worn (this goes for clothes as well).")

    with c2:
        st.image("images/Accessories.png")

    st.subheader("Getting the clothes")

    st.markdown("Thrifting is amazing for getting cool, unique clothes for a mostly cheap price (Since thrifting became a "
                "trend, not every place will be cheap. But you still can find great pieces for little money.)You can either "
                "shop at a secondhand store, a fleamarket, or use apps like Vinted or Depop to find stuff. The apps are "
                "great if you don’t have a thrift store nearby or if you are looking for something specific.")
    st.markdown("Another option is to alter clothes you already own (or the ones you find secondhand, but don’t like the "
                "shape / style of). There are great tutorials online. You can also crochet, knit, or sew your own clothes. "
                "Maybe you’ll pick up a new hobby?")

    st.video("https://www.youtube.com/watch?v=ZYbJ0pfxiX4",
             muted=False)
    st.caption("This is an example video for altering your clothes.")