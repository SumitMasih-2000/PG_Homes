import streamlit as st
import sqlite3
import pandas as pd
from components.ui_elements import render_property_card

def app():
    st.markdown("<h2>Search Properties</h2>", unsafe_allow_html=True)
    
    # Filters
    with st.expander("Advanced Filters", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            city = st.selectbox("City", ["All", "Delhi", "Mumbai", "Bangalore"])
        with col2:
            prop_type = st.selectbox("Type", ["All", "PG", "Flat"])
        with col3:
            budget = st.slider("Max Budget (₹)", 5000, 50000, 20000)

    # Query DB based on filters
    conn = sqlite3.connect('database/staynest.db')
    query = f"SELECT * FROM properties WHERE price <= {budget}"
    if city != "All": query += f" AND city='{city}'"
    if prop_type != "All": query += f" AND type='{prop_type}'"
    
    df = pd.read_sql_query(query, conn)
    conn.close()

    st.markdown(f"<p style='color: #6B7280;'>Found {len(df)} properties</p>", unsafe_allow_html=True)

    cols = st.columns(2)
    for index, row in df.iterrows():
        with cols[index % 2]:
            render_property_card(
                title=row['title'], location=row['city'], price=row['price'],
                rating=row['rating'], is_verified=row['is_verified'],
                uni_partner=row['uni_partner'], image_url=row['image_url'], amenities=row['amenities']
            )
