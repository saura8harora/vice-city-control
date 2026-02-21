import streamlit as st
import base64

def get_base64(file_path: str) -> str:
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def load_css():
    bg_image = get_base64("background.png")

    st.markdown(f"""
    <style>
    /* =========================
       FONTS (chunky + neon vibe)
       ========================= */
    @import url('https://fonts.googleapis.com/css2?family=Lilita+One&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&display=swap');

    :root {{
        --vc-pink: #ff2bd6;
        --vc-cyan: #00f0ff;
        --vc-yellow: #ffd84d;
        --panel: rgba(0,0,0,0.45);
        --panel2: rgba(10,10,30,0.55);
        --stroke: #05050a;
    }}

    /* FULLSCREEN BACKGROUND IMAGE */
    .stApp {{
        background-image: url("data:image/png;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* DARK OVERLAY FOR READABILITY */
    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: radial-gradient(circle at top, rgba(10,10,30,0.55), rgba(0,0,0,0.88));
        z-index: -1;
    }}

    /* GENERAL TEXT */
    html, body, [class*="css"] {{
        font-family: 'Orbitron', sans-serif;
        color: #eef0ff;
    }}

    /* TITLE (poster / RULES style) */
    .hero-title {{
        font-family: 'Lilita One', cursive;
        font-size: 72px;
        letter-spacing: 3px;
        color: #f6f1e8;
        line-height: 0.95;

        /* thick outline */
        -webkit-text-stroke: 8px var(--stroke);

        /* chunky 3D shadow */
        text-shadow:
            10px 10px 0 var(--stroke),
            0 0 18px var(--vc-pink),
            0 0 38px var(--vc-cyan);

        transform: skewX(-8deg);
        margin: 0 0 14px 0;
    }}

    /* SUBTITLE */
    .hero-sub {{
        font-family: 'Orbitron', sans-serif;
        font-size: 18px;
        color: rgba(235,235,255,0.85);
        margin-bottom: 18px;
    }}

    /* SECTION HEADINGS */
    h2, h3 {{
        font-family: 'Luckiest Guy', cursive;
        letter-spacing: 1px;
        color: var(--vc-cyan);
        text-shadow: 0 0 12px rgba(0,240,255,0.35);
    }}

    /* GLASS PANEL LOOK */
    .block-container {{
        padding-top: 1.2rem;
    }}

    /* Cards for most widgets */
    div[data-testid="stMetric"],
    div[data-testid="stVerticalBlockBorderWrapper"],
    section[data-testid="stSidebar"] {{
        background: var(--panel);
        border: 1px solid rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        box-shadow: 0 0 22px rgba(255,43,214,0.12);
        padding: 10px;
    }}

    /* Improve metric text */
    div[data-testid="stMetric"] * {{
        color: #f6f7ff !important;
    }}

    /* BUTTONS */
    .stButton > button {{
        background: linear-gradient(45deg, var(--vc-pink), var(--vc-cyan)) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 10px 16px !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 900 !important;
        box-shadow: 0 0 18px rgba(255,43,214,0.55) !important;
        transition: transform 0.08s ease-in-out;
    }}

    .stButton > button:hover {{
        transform: translateY(-1px) scale(1.01);
        box-shadow: 0 0 26px rgba(0,240,255,0.55) !important;
    }}

    /* INPUTS / SELECTS */
    input, textarea {{
        background: rgba(0,0,0,0.55) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
    }}

    /* TICKER */
    .ticker {{
        background: rgba(0,0,0,0.72);
        color: var(--vc-pink);
        padding: 12px 16px;
        font-family: 'Orbitron', sans-serif;
        font-weight: 800;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(0,240,255,0.25);
        border: 1px solid rgba(255,255,255,0.10);
    }}

    /* Make charts area look dark */
    .stPyplotChart, .stPlotlyChart {{
        background: rgba(0,0,0,0.55);
        border-radius: 16px;
        padding: 8px;
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow: 0 0 18px rgba(255,43,214,0.18);
    }}

    </style>
    """, unsafe_allow_html=True)

    # ----------------------------
    # Matplotlib dark defaults
    # ----------------------------
    st.markdown("""
    <style>
    /* nothing here; matplotlib styling must be done in python via rcParams */
    </style>
    """, unsafe_allow_html=True)