import streamlit as st
from database.db_setup import search_properties, get_cities
from components.property_card import render_property_card


def app(metadata=None):
    st.markdown("## 🔍 Find PG / Flats")
    st.markdown("<p style='color:#6B7280;'>Filter through verified listings in real time.</p>", unsafe_allow_html=True)

    cities = ["All"] + get_cities()

    f1, f2, f3 = st.columns(3)
    with f1:
        city = st.selectbox("City", cities)
    with f2:
        prop_type = st.selectbox("Type", ["All", "PG", "Flat"])
    with f3:
        max_price = st.slider("Max Budget (₹/month)", 5000, 25000, 25000, step=500)

    results = search_properties(city=city, prop_type=prop_type, max_price=max_price)

    st.markdown(f"**{len(results)} properties found**")
    st.markdown("---")

    if not results:
        st.info("No properties match your filters. Try widening your budget or choosing a different city.")
        return

    cols = st.columns(3)
    for i, prop in enumerate(results):
        with cols[i % 3]:
            render_property_card(
                title=prop["title"],
                location=prop["city"],
                price=prop["price"],
                rating=prop["rating"],
                is_verified=prop["is_verified"],
                uni_partner=prop["uni_partner"],
                image_url=prop["image_url"],
                amenities=prop["amenities"],
            )
