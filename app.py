import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="ADITYA AI SCALPER ULTIMATE", layout="wide", page_icon="📈")

# Custom CSS for High-Tech UI
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stApp { background: radial-gradient(circle, #1c1f26 0%, #0e1117 100%); }
    .stat-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 251, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .stat-val { font-size: 24px; font-weight: bold; color: #00fbff; }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.5em;
        font-weight: bold;
    }
    .stButton>button:first-child { 
        background: linear-gradient(45deg, #00ff88, #00a859);
        color: black; border: none;
    }
    .stButton>button:last-child { 
        background: linear-gradient(45deg, #ff4b4b, #a80000);
        color: white; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2091/2091665.png", width=80)
    st.header("🔑 MASTER ACCESS")
    acc_id = st.text_input("MT5 ID", placeholder="Account Number")
    password = st.text_input("Password", type="password")
    server = st.text_input("Server", placeholder="e.g. VProp-Server")
    st.divider()
    st.info("System: MT5 Connection Ready")
    st.caption("Magic No: 889911 Active")

# Header
st.title("🛡️ ADITYA AI SCALPER - ULTIMATE V3.0")
st.write("---")

# Metrics Row
m1, m2, m3, m4 = st.columns(4)
with m1: st.markdown('<div class="stat-card"><small>Pair</small><div class="stat-val">XAUUSD</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="stat-card"><small>Bot Status</small><div class="stat-val" style="color:#00ff88;">READY</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="stat-card"><small>Spread</small><div class="stat-val">12</div></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="stat-card"><small>Daily P/L</small><div class="stat-val">$0.00</div></div>', unsafe_allow_html=True)

st.write("---")

# Settings Area
left, right = st.columns([1.5, 2])

with left:
    st.subheader("⚙️ STRATEGY SETTINGS")
    with st.container(border=True):
        lot = st.number_input("Lot Size", 0.01, 5.0, 0.01, step=0.01)
        mode = st.radio("Execution Mode", ["Conservative 🛡️", "Aggressive 🔥"], horizontal=True)
        
        st.divider()
        st.markdown("**Profit & Risk Control**")
        control_type = st.segmented_control("Control Mode", ["AI Automatic", "Manual Dollars ($)"])
        
        if control_type == "Manual Dollars ($)":
            c1, c2 = st.columns(2)
            tp = c1.number_input("Take Profit ($)", 1, 1000, 50)
            sl = c2.number_input("Stop Loss ($)", 1, 1000, 20)
        else:
            st.write("🤖 AI is handling TP/SL based on market volatility.")
            tp, sl = "Auto", "Auto"

    st.write("")
    if st.button("▶ START TRADING"):
        st.balloons()
        st.toast(f"Bot Active: {mode}")
    if st.button("🛑 STOP BOT"):
        st.error("System Offline")

with right:
    st.subheader("📜 LIVE INTELLIGENCE LOGS")
    with st.container(border=True):
        st.code(f"""
[SYSTEM] Initializing Aditya AI Scalper...
[CONFIG] Asset: XAUUSD | Lot: {lot}
[MODE] Strategy: {mode} | Control: {control_type}
[TARGETS] TP: ${tp} | SL: ${sl}
[WAIT] Scanning for high-probability setups...
        """, language="bash")
    
    st.divider()
    st.markdown("#### 🔄 MULTI-ACCOUNT MANAGEMENT")
    st.button("+ Add Linked Account")

st.write("---")
st.caption("Aditya AI Labs | Scalping Terminal 2026")
