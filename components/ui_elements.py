import streamlit as st

def render_property_card(title, location, price, rating, is_verified, uni_partner, image_url, amenities):
    verified_badge = '<span class="badge-verified">✓ Verified</span>' if is_verified else ''
    uni_badge = '<span class="badge-uni">🎓 Uni Partner</span>' if uni_partner else ''
    
    html = f"""
    <div class="property-card">
        <img src="{image_url}" class="property-img" alt="Property">
        <div style="margin-top: 12px; display: flex; justify-content: space-between; align-items: center;">
            <div>{verified_badge} {uni_badge}</div>
            <div style="font-weight: 600; color: #F59E0B;">★ {rating}</div>
        </div>
        <h3 style="margin: 10px 0 5px 0; font-size: 1.2rem;">{title}</h3>
        <p style="color: #6B7280; font-size: 0.9rem; margin: 0 0 10px 0;">📍 {location}</p>
        <p style="color: #6B7280; font-size: 0.85rem; margin: 0 0 15px 0;">{amenities}</p>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 1.2rem; font-weight: 700; color: #2563EB;">₹{price}<span style="font-size: 0.8rem; color: #6B7280;">/month</span></span>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
