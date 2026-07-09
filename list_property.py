import streamlit as st
from database.db_setup import add_property


def app():
    st.markdown("## 🏠 List Your Property")
    st.markdown(
        "<p style='color:#6B7280;'>Are you a PG or flat owner? Add your property so students can find and contact you directly.</p>",
        unsafe_allow_html=True,
    )

    with st.form("list_property_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Property Name*", placeholder="e.g. Green Valley PG")
            prop_type = st.selectbox("Type*", ["PG", "Flat"])
            city = st.text_input("City*", placeholder="e.g. Jaipur")
            price = st.number_input("Monthly Rent (₹)*", min_value=1000, step=500)
        with col2:
            owner_name = st.text_input("Your Name*", placeholder="e.g. Ramesh Sharma")
            owner_contact = st.text_input("Contact Number*", placeholder="e.g. +91-9876543210")
            image_url = st.text_input("Property Image URL (optional)", placeholder="https://...")
        amenities = st.text_area("Amenities", placeholder="e.g. WiFi, Food, AC, Laundry")

        submitted = st.form_submit_button("Submit Listing")

        if submitted:
            if not title or not city or not owner_name or not owner_contact:
                st.error("Please fill all required fields marked with *.")
            else:
                add_property(
                    title=title,
                    prop_type=prop_type,
                    city=city,
                    price=int(price),
                    amenities=amenities or "Not specified",
                    owner_name=owner_name,
                    owner_contact=owner_contact,
                    image_url=image_url or None,
                )
                st.success(f"'{title}' has been listed successfully! It's now visible under Find PG/Flats.")
                st.balloons()
