import streamlit as st
import MetaTrader5 as mt5
import pandas as pd

# Page Setup
st.set_page_config(page_title="ADITYA AI SCALPER", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #000000; }
    div.stButton > button:first-child { background-color: #FF0000; color: white; font-weight: bold; }
    .stat-val { color: #FF0000; font-weight: bold; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 ADITYA AI SCALPER - FINAL")

col1, col2 = st.columns([1, 2])

with col1:
    acc_id = st.text_input("MT5 ID")
    password = st.text_input("Password", type="password")
    asset = st.selectbox("Asset", ["XAUUSD", "EURUSD"])
    sl = st.number_input("Stop Loss ($)", value=10.0)
    tp = st.number_input("Take Profit ($)", value=20.0)
    
    if st.button("▶ START TRADING"):
        if acc_id and password:
            st.success("System Connected & Active!")
        else:
            st.error("Please enter Login Details")

with col2:
    st.subheader("LIVE LOGS")
    st.write("Waiting for Start command...")
