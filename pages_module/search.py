import streamlit as st
from database.db_setup import search_properties, get_cities
from components.property_card import render_property_card


def app(metadata=None):
    st.markdown("## 🔍 Find PG / Flats")
    st.markdown("<p style='color:#6B7280;'>Filter through verified listings in real time.</p>", unsafe_allow_html=True)

    all_locations = get_cities()  # e.g. "Govindpuram, Ghaziabad"
    main_cities = sorted(set(loc.split(", ")[-1] for loc in all_locations))

    f1, f2, f3, f4 = st.columns(4)
    with f1:
        main_city = st.selectbox("City", ["All"] + main_cities)
    with f2:
        if main_city == "All":
            area_options = ["All"] + all_locations
        else:
            area_options = ["All"] + [loc for loc in all_locations if loc.endswith(main_city)]
        area = st.selectbox("Area", area_options)
    with f3:
        prop_type = st.selectbox("Type", ["All", "PG", "Flat"])
    with f4:
        max_price = st.slider("Max Budget (₹/month)", 5000, 26000, 26000, step=500)

    # Determine effective city filter for the query
    if area != "All":
        city_filter = area
    elif main_city != "All":
        city_filter = None  # handled below via substring match
    else:
        city_filter = "All"

    if area != "All":
        results = search_properties(city=area, prop_type=prop_type, max_price=max_price)
    else:
        results = search_properties(city="All", prop_type=prop_type, max_price=max_price)
        if main_city != "All":
            results = [r for r in results if r["city"].endswith(main_city)]

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
                owner_name=prop.get("owner_name"),
                owner_contact=prop.get("owner_contact"),
            )
