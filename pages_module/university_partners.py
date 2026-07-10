import streamlit as st
from database.db_setup import get_all_properties


UNIVERSITIES = [
    {"name": "Delhi University (North Campus)", "city": "Delhi", "students": "132,000+", "since": "2022"},
    {"name": "Amity University", "city": "Noida", "students": "45,000+", "since": "2023"},
    {"name": "IMS Ghaziabad", "city": "Ghaziabad", "students": "8,500+", "since": "2023"},
    {"name": "Jamia Millia Islamia", "city": "Delhi", "students": "20,000+", "since": "2024"},
    {"name": "Sharda University", "city": "Greater Noida", "students": "20,000+", "since": "2024"},
]


def app():
    st.markdown("## 🎓 University Partners")
    st.markdown(
        "<p style='color:#6B7280; font-size:1.05rem;'>We partner directly with universities to offer verified, "
        "student-friendly housing near campus with special rates and priority booking.</p>",
        unsafe_allow_html=True,
    )

    properties = get_all_properties()
    uni_props = [p for p in properties if p["uni_partner"]]

    c1, c2, c3 = st.columns(3)
    c1.metric("Partner Universities", len(UNIVERSITIES))
    c2.metric("Uni-Partnered Listings", len(uni_props))
    c3.metric("Cities Covered", len(set(u["city"] for u in UNIVERSITIES)))

    st.markdown("---")
    st.markdown("### 🏫 Our Partner Institutions")

    cols = st.columns(len(UNIVERSITIES))
    for i, uni in enumerate(UNIVERSITIES):
        with cols[i % len(UNIVERSITIES)] if len(UNIVERSITIES) <= 5 else st.container():
            st.markdown(
                f"""
                <div class="uni-card">
                    <h4>{uni['name']}</h4>
                    <p>📍 {uni['city']}</p>
                    <p>👥 {uni['students']} students</p>
                    <span class="badge-uni">Partner since {uni['since']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.markdown("### 🏠 Uni-Partnered Properties")

    if not uni_props:
        st.info("No university-partnered listings available right now.")
    else:
        from components.property_card import render_property_card
        cols = st.columns(3)
        for i, prop in enumerate(uni_props[:9]):
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

    st.markdown("---")
    with st.expander("📩 Want your university to partner with StayNest?"):
        st.write("Reach out to our partnerships team and we'll set up verified housing options for your students.")
        uni_contact_name = st.text_input("University / Institution Name")
        contact_email = st.text_input("Contact Email")
        if st.button("Submit Partnership Request"):
            if uni_contact_name and contact_email:
                st.success("Thanks! Our team will reach out within 2 business days.")
            else:
                st.error("Please fill both fields.")
