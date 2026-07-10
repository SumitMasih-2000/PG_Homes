/* Import Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@500;600;700;800&display=swap');

:root {
    --primary: #7C3AED;
    --primary-dark: #5B21B6;
    --accent: #2563EB;
    --accent2: #EC4899;
    --success: #22C55E;
    --warning: #F59E0B;
    --bg: #F5F3FF;
    --card-bg: #FFFFFF;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #F5F3FF 0%, #EFF6FF 50%, #FDF2F8 100%);
    color: #111827;
}
h1, h2, h3, h4, h5 {
    font-family: 'Poppins', sans-serif;
    color: #1E1B4B;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Sidebar - glass + gradient edge */
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-right: 2px solid transparent;
    border-image: linear-gradient(180deg, #7C3AED, #EC4899) 1;
    box-shadow: 4px 0 20px rgba(124, 58, 237, 0.08);
}

/* Metrics - 3D card feel */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #ffffff, #f3f0ff);
    border-radius: 14px;
    padding: 14px 18px;
    box-shadow: 6px 6px 16px rgba(124, 58, 237, 0.12), -4px -4px 12px rgba(255,255,255,0.7);
    border: 1px solid #EDE9FE;
}

/* 3D Property Cards */
.property-card {
    background: linear-gradient(160deg, #FFFFFF 0%, #FAF9FF 100%);
    border-radius: 20px;
    padding: 18px;
    box-shadow:
        0 1px 2px rgba(0,0,0,0.04),
        0 8px 16px rgba(124, 58, 237, 0.10),
        0 16px 32px rgba(37, 99, 235, 0.06);
    transition: all 0.35s cubic-bezier(.2,.8,.2,1);
    border: 1px solid #EDE9FE;
    margin-bottom: 22px;
    transform: perspective(800px) rotateX(0deg);
}
.property-card:hover {
    transform: perspective(800px) translateY(-8px) rotateX(2deg) scale(1.015);
    box-shadow:
        0 4px 8px rgba(0,0,0,0.06),
        0 16px 28px rgba(124, 58, 237, 0.22),
        0 28px 48px rgba(236, 72, 153, 0.14);
    border-color: #C4B5FD;
}
.property-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 14px;
    box-shadow: inset 0 -30px 30px -20px rgba(0,0,0,0.15);
}
.card-top-row {
    margin-top: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.card-title {
    margin: 10px 0 4px 0;
    font-size: 1.2rem;
    background: linear-gradient(90deg, #1E1B4B, #4C1D95);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.card-location { color: #6B7280; font-size: 0.9rem; margin: 0 0 8px 0; }
.card-amenities { color: #6B7280; font-size: 0.85rem; margin: 0 0 10px 0; }
.card-price-row { display: flex; justify-content: space-between; align-items: center; }
.card-price {
    font-size: 1.25rem;
    font-weight: 800;
    background: linear-gradient(90deg, #7C3AED, #2563EB);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.card-price-sub { font-size: 0.8rem; color: #6B7280; -webkit-text-fill-color: #6B7280; }
.rating-badge {
    font-weight: 700;
    color: #F59E0B;
    background: rgba(245, 158, 11, 0.1);
    padding: 3px 10px;
    border-radius: 20px;
}

.owner-box {
    margin-top: 12px;
    padding: 10px 12px;
    border-radius: 12px;
    background: linear-gradient(135deg, #EDE9FE, #DBEAFE);
    font-size: 0.85rem;
    color: #1E1B4B;
    box-shadow: inset 0 1px 2px rgba(255,255,255,0.6);
}

/* Badges */
.badge-verified {
    background: linear-gradient(135deg, rgba(34,197,94,0.15), rgba(34,197,94,0.05));
    color: #16A34A;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    box-shadow: 0 2px 6px rgba(34,197,94,0.15);
}
.badge-uni {
    background: linear-gradient(135deg, rgba(124,58,237,0.18), rgba(37,99,235,0.08));
    color: #6D28D9;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    box-shadow: 0 2px 6px rgba(124,58,237,0.15);
}

/* Gradient 3D Buttons */
.stButton > button {
    background: linear-gradient(135deg, #7C3AED 0%, #2563EB 60%, #EC4899 100%);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.6rem 1.5rem;
    font-weight: 700;
    box-shadow: 0 6px 16px rgba(124, 58, 237, 0.35), inset 0 1px 0 rgba(255,255,255,0.25);
    transition: all 0.25s ease;
    width: 100%;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 22px rgba(124, 58, 237, 0.45);
    color: white;
}
.stButton > button:active {
    transform: translateY(0px);
}

/* University partner cards */
.uni-card {
    background: linear-gradient(160deg, #ffffff, #F5F3FF);
    border-radius: 16px;
    padding: 16px;
    box-shadow: 0 8px 20px rgba(124,58,237,0.12);
    border: 1px solid #EDE9FE;
    text-align: center;
    margin-bottom: 16px;
    transition: transform 0.25s ease;
}
.uni-card:hover { transform: translateY(-4px); }
.uni-card h4 { margin-bottom: 6px; color: #4C1D95; }
.uni-card p { color: #6B7280; font-size: 0.85rem; margin: 2px 0; }

/* Dashboard profile card */
.dashboard-profile {
    background: linear-gradient(160deg, #ffffff, #F5F3FF);
    border-radius: 20px;
    padding: 28px;
    text-align: center;
    box-shadow: 0 10px 24px rgba(124,58,237,0.15);
    border: 1px solid #EDE9FE;
}
.dashboard-profile .avatar {
    font-size: 3rem;
    width: 80px; height: 80px;
    line-height: 80px;
    margin: 0 auto 12px auto;
    border-radius: 50%;
    background: linear-gradient(135deg, #7C3AED, #2563EB);
    box-shadow: 0 6px 16px rgba(124,58,237,0.4);
}
.dashboard-profile h3 { margin: 6px 0 2px 0; }
.dashboard-profile p { color: #6B7280; margin-bottom: 10px; }

/* Slider + inputs accent */
.stSlider [role="slider"] {
    background-color: #7C3AED !important;
}
