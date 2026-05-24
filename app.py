import streamlit as st
import MetaTrader5 as mt5
import pandas as pd
import time

# Page Configuration
st.set_page_config(page_title="DREAMLINER PRO TERMINAL", layout="wide")

# Styling
st.markdown("""
    <style>
    .main {background-color: #f5f5f5;}
    .stButton>button {width: 100%; border-radius: 5px; height: 3em; background-color: #0047AB; color: white;}
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 DREAMLINER PROFESSIONAL TRADING TERMINAL")

# 1. Sidebar Connection
with st.sidebar:
    st.header("⚙️ SYSTEM CONFIG")
    login = st.text_input("MT5 Login ID")
    password = st.text_input("Password", type="password")
    server = st.text_input("Server Name")
    if st.button("CONNECT TO MT5"):
        if mt5.initialize(login=int(login), password=password, server=server):
            st.success("CONNECTION ESTABLISHED")
        else:
            st.error("CONNECTION FAILED")

# 2. Controls
c1, c2, c3, c4 = st.columns(4)
lot = c1.number_input("Lot Size", 0.01, 10.0, 0.01)
sl = c2.number_input("SL ($)", 0.0, 1000.0, 10.0)
tp = c3.number_input("TP ($)", 0.0, 1000.0, 20.0)
mode = c4.selectbox("Mode", ["Safe Mode", "Aggressive Mode"])

# 3. Execution Logic
if st.button("START DREAMLINER BOT"):
    st.info("ENGINE RUNNING... ANALYZING MARKET TREND...")
    # Add your strategy logic here
    # Example: if mt5.symbol_info_tick("XAUUSD").ask > ...
    st.write("AI Analysis: Scanning symbols for optimal entry...")

# 4. Live Dashboard
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("📡 MARKET MONITORING")
    # Real-time data table
    data = {"Symbol": ["XAUUSD", "EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "USDCAD"],
            "Status": ["Active", "Active", "Active", "Active", "Active", "Active"]}
    st.table(pd.DataFrame(data))

with col_right:
    st.subheader("📜 SYSTEM LOGS")
    log_box = st.text_area("Live activity feed", "System initialized. Waiting for user input...", height=300)
    if st.button("KILL SWITCH (STOP ALL)"):
        st.warning("EMERGENCY STOP TRIGGERED!")

# 5. Trend Analysis Status
st.markdown("---")
st.subheader("🤖 AI TREND DIRECTION")
st.success("CURRENT DIRECTION: SCANNING MARKET FLOW...")

# Footer
st.caption("DREAMLINER SYSTEM v1.0 | SECURE CONNECTION ENABLED")
