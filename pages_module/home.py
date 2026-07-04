import streamlit as st
import sqlite3
import pandas as pd
from components.ui_elements import render_property_card

def app():
    # Hero Section
    st.markdown("""
        <div style="text-align: center; padding: 4rem 2rem; background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); border-radius: 24px; margin-bottom: 3rem;">
            <h1 style="color: white; font-size: 3rem; margin-bottom: 1rem;">Find Your Perfect Campus Home.</h1>
            <p style="color: #94A3B8; font-size: 1.2rem; margin-bottom: 2rem;">Verified Student Housing & Brokerage-Free Rentals</p>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Featured Properties")
    
    # Fetch from DB
    conn = sqlite3.connect('database/staynest.db')
    df = pd.read_sql_query("SELECT * FROM properties LIMIT 3", conn)
    conn.close()

    cols = st.columns(3)
    for index, row in df.iterrows():
        with cols[index % 3]:
            render_property_card(
                title=row['title'],
                location=row['city'],
                price=row['price'],
                rating=row['rating'],
                is_verified=row['is_verified'],
                uni_partner=row['uni_partner'],
                image_url=row['image_url'],
                amenities=row['amenities']
            )
            st.button("View Details", key=f"btn_{row['id']}")
