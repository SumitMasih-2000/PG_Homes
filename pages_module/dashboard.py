import streamlit as st
from database.db_setup import get_all_properties


def app():
    st.markdown("## 👤 Student Dashboard")
    st.markdown(
        "<p style='color:#6B7280; font-size:1.05rem;'>Track your saved properties, recent searches, and account details.</p>",
        unsafe_allow_html=True,
    )

    if "saved_properties" not in st.session_state:
        st.session_state.saved_properties = []

    properties = get_all_properties()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(
            """
            <div class="dashboard-profile">
                <div class="avatar">🧑‍🎓</div>
                <h3>Student User</h3>
                <p>student@example.com</p>
                <span class="badge-verified">✓ Verified Account</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        c1, c2, c3 = st.columns(3)
        c1.metric("Saved Properties", len(st.session_state.saved_properties))
        c2.metric("Properties Viewed", len(properties))
        c3.metric("Active Since", "Jul 2026")

    st.markdown("---")
    st.markdown("### ⭐ Save a Property to Your Dashboard")

    titles = [p["title"] for p in properties]
    pick = st.selectbox("Choose a property to save", ["Select..."] + titles)
    if st.button("💾 Save to Dashboard"):
        if pick != "Select..." and pick not in st.session_state.saved_properties:
            st.session_state.saved_properties.append(pick)
            st.success(f"Saved '{pick}' to your dashboard!")
        elif pick in st.session_state.saved_properties:
            st.warning("Already saved.")
        else:
            st.error("Please select a property first.")

    st.markdown("---")
    st.markdown("### 📌 Your Saved Properties")

    if not st.session_state.saved_properties:
        st.info("You haven't saved any properties yet. Browse 'Find PG/Flats' and save your favorites here.")
    else:
        saved = [p for p in properties if p["title"] in st.session_state.saved_properties]
        from components.property_card import render_property_card
        cols = st.columns(3)
        for i, prop in enumerate(saved):
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
                    owner_name=prop.get("owner_name"),
                    owner_contact=prop.get("owner_contact"),
                )
        if st.button("🗑️ Clear All Saved"):
            st.session_state.saved_properties = []
            st.rerun()
