import streamlit as st


def render_property_card(title, location, price, rating, is_verified, uni_partner,
                          image_url, amenities, owner_name=None, owner_contact=None):
    verified_badge = '<span class="badge-verified">✓ Verified</span>' if is_verified else ''
    uni_badge = '<span class="badge-uni">🎓 Uni Partner</span>' if uni_partner else ''

    contact_block = ""
    if owner_name or owner_contact:
        contact_block = (
            '<div class="owner-box">'
            f'👤 <b>{owner_name or "Owner"}</b><br>'
            f'📞 {owner_contact or "Contact via platform"}'
            '</div>'
        )

    card_html = (
        '<div class="property-card">'
        f'<img src="{image_url}" class="property-img" alt="Property">'
        '<div class="card-top-row">'
        f'<div>{verified_badge} {uni_badge}</div>'
        f'<div class="rating-badge">★ {rating}</div>'
        '</div>'
        f'<h3 class="card-title">{title}</h3>'
        f'<p class="card-location">📍 {location}</p>'
        f'<p class="card-amenities">{amenities}</p>'
        '<div class="card-price-row">'
        f'<span class="card-price">₹{price}<span class="card-price-sub">/month</span></span>'
        '</div>'
        f'{contact_block}'
        '</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)
