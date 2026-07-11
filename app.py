import streamlit as st
from streamlit_option_menu import option_menu
import os

# 1. Page Config MUST be the first Streamlit command
st.set_page_config(page_title="StayNest | Premium Housing", page_icon="🏢", layout="wide")

# 2. Initialize the real database once (fast — just creates table + inserts if empty)
from database.db_setup import init_database

@st.cache_resource
def setup():
    init_database()
    return True

setup()

# 3. Load Custom CSS
def load_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("assets/css/style.css")

# 4. Sidebar Navigation
with st.sidebar:
    st.markdown("## 🏢 StayNest")
    st.markdown("---")

    selected = option_menu(
        menu_title=None,
        options=["Home", "Find PG/Flats", "List Your Property", "University Partners", "Dashboard"],
        icons=["house", "search", "plus-circle", "building", "person-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#7C3AED", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px 0", "--hover-color": "#EDE9FE"},
            "nav-link-selected": {"background": "linear-gradient(135deg, #7C3AED 0%, #2563EB 100%)", "color": "#FFFFFF", "font-weight": "600"},
        }
    )

    st.markdown("---")
    

# 5. Routing Engine
if selected == "Home":
    from pages_module import home
    home.app()
elif selected == "Find PG/Flats":
    from pages_module import search
    search.app()
elif selected == "List Your Property":
    from pages_module import list_property
    list_property.app()
elif selected == "University Partners":
    from pages_module import university_partners
    university_partners.app()
elif selected == "Dashboard":
    from pages_module import dashboard
    dashboard.app()
