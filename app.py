import streamlit as st
import requests
import pandas as pd

from simulation import create_population, apply_rumor, apply_mission
from metrics import (
    calculate_respect, calculate_trust, calculate_chaos,
    calculate_heat, calculate_civic_points
)
from visuals import city_pulse_meter, influencer_network
from styles import load_css
from constants import RUMOR_IMPACT, MISSION_BOOST
from metrics import misinfo_radar, crisis_playbook


st.set_page_config(layout="wide")
load_css()

# Title (using CSS class)
st.markdown('<div class="hero-title"> VICE CITY CONTROL DASHBOARD</div>', unsafe_allow_html=True)
st.markdown("""
<div style='font-size:18px; color:#cfcfe6; margin-bottom:25px;'>
NPC behavior modulation • influence mapping • civic missions • misinformation heat
</div>
""", unsafe_allow_html=True)

# Disclaimer
if "accepted" not in st.session_state:
    st.session_state.accepted = False

if not st.session_state.accepted:
    st.warning("This is a fictional civic simulation. Educational use only.")
    if st.button("Enter Vice City"):
        st.session_state.accepted = True
        st.rerun()
    st.stop()

# Population Init
if "population" not in st.session_state:
    st.session_state.population = create_population()

df = st.session_state.population

# Safety net: if df ever becomes list, convert back
if isinstance(df, list):
    df = pd.DataFrame(df)
    st.session_state.population = df

# Controls
st.markdown("## 🎮 City Controls")
col1, col2 = st.columns(2)

with col1:
    if st.button("🎙 Spread Rumor"):
        df = apply_rumor(df, RUMOR_IMPACT)

with col2:
    if st.button("🎯 Launch Civic Mission"):
        df = apply_mission(df, MISSION_BOOST)

st.session_state.population = df

# Metrics
respect = calculate_respect(df)
trust = calculate_trust(df)
chaos = calculate_chaos(df)
heat = calculate_heat(chaos)
civic = calculate_civic_points(respect, trust)

pulse = max(min((respect + trust - chaos) / 2, 100), 0)

# Overview layout
st.markdown("## 🌆 City Overview")
colA, colB = st.columns([1, 2])

with colA:
    st.pyplot(city_pulse_meter(pulse))

with colB:
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Chaos", round(chaos, 2))
    c2.metric("Respect", round(respect, 2))
    c3.metric("Trust", round(trust, 2))
    c4.metric("Civic Points", round(civic, 2))
    c5.metric("Heat", round(heat, 2))

st.markdown("---")
# ------------------------------
# ROUND 2 FEATURE: MISINFO RADAR
# ------------------------------
level, radar_score = misinfo_radar(chaos, trust)

st.markdown("## 📡 Misinformation Radar")

if level == "WAVE":
    st.error(f"🚨 CITY-WIDE MISINFORMATION WAVE • Radar Score: {radar_score:.0f}")
elif level == "TENSION":
    st.warning(f"⚠️ RISING TENSION • Radar Score: {radar_score:.0f}")
else:
    st.success(f"✅ STABLE • Radar Score: {radar_score:.0f}")

# Playbook (always shows, changes with level)
st.markdown("### 🧠 Recommended Playbook (No Censorship, Only Belief Redirection)")
steps = crisis_playbook(level)
for i, s in enumerate(steps, 1):
    st.write(f"**{i}.** {s}")

# Network + AI
left, right = st.columns([2, 1])

with left:
    st.markdown("### 🌐 Influence Network")
    st.pyplot(influencer_network(df))

with right:
    st.markdown("### 🤖 Vice AI Advisor")
    user_input = st.text_input("Ask about city strategy:")

    if st.button("Get Advice"):
        if user_input:
            try:
                r = requests.get("https://api.quotable.io/random", timeout=5)
                if r.status_code == 200:
                    st.success(r.json().get("content", "No advice returned."))
                else:
                    st.error("AI service returned error.")
            except Exception:
                st.error("AI service unavailable.")

# Vice Radio ticker
st.markdown("""
<div class="ticker">
VICE RADIO LIVE: Rumor spreading | Mission active | Heat rising | Civic morale fluctuating...
</div>
""", unsafe_allow_html=True)
