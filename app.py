import streamlit as st
import MetaTrader5 as mt5
import pandas as pd
import time

# Page Configuration
st.set_page_config(page_title="ADITYA AI SCALPER ULTIMATE", layout="wide", page_icon="🤖")

# CSS for White Theme, Red Buttons, and Dashboard look
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #000000; }
    h1, h2, h3, p, label { color: #000000 !important; }
    div.stButton > button:first-child {
        background-color: #FF0000;
        color: white;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    .stat-card { background: #f0f2f6; border: 1px solid #FF0000; 
                 border-radius: 10px; padding: 15px; text-align: center; color: #000000; }
    .stat-val { font-size: 20px; font-weight: bold; color: #FF0000; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - Login & Timing
with st.sidebar:
    st.header("🔑 MASTER ACCESS")
    acc_id = st.text_input("MT5 ID")
    password = st.text_input("Password", type="password")
    server = st.text_input("Server")
    st.divider()
    st.subheader("⏱️ CHART SETTINGS")
    tf = st.selectbox("Select Timeframe", ["1 Minute (M1)", "5 Minutes (M5)"])
    st.info("System Ready for Trading")

# Header
st.title("🤖 ADITYA AI SCALPER - ULTIMATE V4.5")

# Dashboard Layout
col1, col2 = st.columns([1.5, 2])

with col1:
    st.subheader("⚙️ STRATEGY & RISK")
    with st.container(border=True):
        selected_asset = st.selectbox("Select Asset", ["XAUUSD (GOLD)", "EURUSD", "GBPUSD", "USDJPY", "US30"])
        lot = st.number_input("Lot Size", 0.01, 5.0, 0.01, step=0.01)
        sl_val = st.number_input("Stop Loss ($)", min_value=1.0, value=10.0, step=1.0)
        tp_val = st.number_input("Take Profit ($)", min_value=1.0, value=20.0, step=1.0)
        mode = st.radio("Execution Mode", ["Conservative", "Aggressive"], horizontal=True)
    
    start_btn = st.button("▶ START TRADING")
    stop_btn = st.button("🛑 STOP BOT")

    if start_btn:
        if not acc_id or not password:
            st.error("Error: Enter MT5 ID and Password!")
        else:
            st.success(f"Bot active: {selected_asset} | TF: {tf} | SL:${sl_val} | TP:${tp_val}")
    
    if stop_btn:
        st.warning("System Stopped!")

with col2:
    st.subheader("📊 LIVE METRICS")
    m1, m2 = st.columns(2)
    with m1: st.markdown(f'<div class="stat-card"><small>Timeframe</small><div class="stat-val">{tf}</div></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="stat-card"><small>Daily P/L</small><div class="stat-val" style="color:#FF0000;">$0.00</div></div>', unsafe_allow_html=True)
    
    st.subheader("📜 LIVE INTELLIGENCE LOGS")
    with st.container(border=True):
        st.code(f"""
[SYSTEM] Aditya AI V4.5 - READY
[TIMING] Running on {tf}
[ASSET] {selected_asset}
[RISK] SL:${sl_val} / TP:${tp_val}
[LOG] Awaiting market triggers...
        """, language="bash")

st.write("---")
st.caption("Aditya AI Labs | Scalping Terminal 2026")
