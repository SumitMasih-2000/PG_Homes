import streamlit as st
from database.db_setup import get_all_properties, get_cities
from components.property_card import render_property_card


def app():
    properties = get_all_properties()
    cities = get_cities()

    st.markdown("## 🏢 Find Your Perfect Stay")
    st.markdown(
        "<p style='color:#6B7280; font-size:1.05rem;'>Verified PGs and flats near your campus — real listings, real prices, zero brokerage.</p>",
        unsafe_allow_html=True,
    )

    total_listings = len(properties)
    verified_count = sum(1 for p in properties if p["is_verified"])
    uni_partner_count = sum(1 for p in properties if p["uni_partner"])
    avg_price = int(sum(p["price"] for p in properties) / total_listings) if total_listings else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Listings", total_listings)
    c2.metric("Verified Properties", verified_count)
    c3.metric("University Partnered", uni_partner_count)
    c4.metric("Avg. Monthly Rent", f"₹{avg_price:,}")

    st.markdown("---")
    st.markdown("### ✨ Featured Properties")

    featured = sorted(properties, key=lambda p: p["rating"], reverse=True)[:6]

    cols = st.columns(3)
    for i, prop in enumerate(featured):
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

    st.markdown("---")
    st.markdown(f"**Available in:** {', '.join(cities)}")
