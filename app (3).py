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
        options=["Home", "Find PG/Flats", "University Partners", "Dashboard"],
        icons=["house", "search", "building", "person-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#2563EB", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px 0", "--hover-color": "#E5E7EB"},
            "nav-link-selected": {"background-color": "#F8FAFC", "color": "#0F172A", "font-weight": "600"},
        }
    )

    st.markdown("---")
    st.markdown("Logged in as **Student**")

# 5. Routing Engine
if selected == "Home":
    from pages_module import home
    home.app()
elif selected == "Find PG/Flats":
    from pages_module import search
    search.app()
elif selected == "University Partners":
    st.title("🎓 University Partners")
    st.info("University partner module under construction.")
elif selected == "Dashboard":
    st.title("👤 Student Dashboard")
    st.info("Dashboard module under construction.")
