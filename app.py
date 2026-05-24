import streamlit as st
import pandas as pd
import random

# ===== PAGE =====
st.set_page_config(
    page_title="ADITYA AI",
    layout="wide"
)

# ===== STYLE =====
st.markdown("""
<style>
.stApp{
background:white;
color:black;
}
.stButton button{
background:red;
color:white;
border:none;
border-radius:10px;
font-weight:bold;
}
.box{
padding:15px;
background:#f5f5f5;
border-radius:12px;
text-align:center;
margin:5px;
}
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====
with st.sidebar:

    st.title("🤖 ADITYA AI")

    login = st.text_input("MT5 Login ID")
    password = st.text_input(
        "Password",
        type="password"
    )

    server = st.text_input("Server")

    pair = st.selectbox(
        "Select Pair",
        [
            "XAUUSD",
            "EURUSD",
            "GBPUSD",
            "USDJPY",
            "AUDUSD"
        ]
    )

    timeframe = st.selectbox(
        "Timeframe",
        ["M1","M5"]
    )

    lot = st.number_input(
        "Lot Size",
        0.01,
        5.0,
        0.01
    )

    tp = st.number_input(
        "Take Profit ($)",
        1,
        10000,
        50
    )

    sl = st.number_input(
        "Stop Loss ($)",
        1,
        10000,
        20
    )

    mode = st.radio(
        "Mode",
        ["SAFE","AGGRESSIVE"]
    )

# ===== TITLE =====
st.title("🤖 ADITYA AI SCALPER")

# ===== START =====
if st.button("🚀 START BOT"):

    st.success("MT5 CONNECTED ✅")

    # ===== FAKE LIVE DATA =====
    buy = round(
        random.uniform(2300,2400),
        2
    )

    sell = round(
        buy - random.uniform(0.2,1),
        2
    )

    signal = random.choice(
        ["BUY","SELL","WAIT"]
    )

    confidence = random.randint(
        70,99
    )

    profit = round(
        random.uniform(-20,120),
        2
    )

    # ===== DASHBOARD =====
    c1,c2,c3,c4 = st.columns(4)

    c1.markdown(f"""
    <div class="box">
    PAIR<br><b>{pair}</b>
    </div>
    """, unsafe_allow_html=True)

    c2.markdown(f"""
    <div class="box">
    TF<br><b>{timeframe}</b>
    </div>
    """, unsafe_allow_html=True)

    c3.markdown(f"""
    <div class="box">
    SIGNAL<br><b>{signal}</b>
    </div>
    """, unsafe_allow_html=True)

    c4.markdown(f"""
    <div class="box">
    AI %<br><b>{confidence}%</b>
    </div>
    """, unsafe_allow_html=True)

    # ===== PRICE =====
    d1,d2,d3 = st.columns(3)

    d1.markdown(f"""
    <div class="box">
    BUY PRICE<br><b>{buy}</b>
    </div>
    """, unsafe_allow_html=True)

    d2.markdown(f"""
    <div class="box">
    SELL PRICE<br><b>{sell}</b>
    </div>
    """, unsafe_allow_html=True)

    d3.markdown(f"""
    <div class="box">
    PROFIT<br><b>${profit}</b>
    </div>
    """, unsafe_allow_html=True)

    # ===== LOGS =====
    st.code(f"""
ADITYA AI ACTIVE
PAIR = {pair}
TIMEFRAME = {timeframe}
MODE = {mode}
SIGNAL = {signal}
AI CONFIDENCE = {confidence}%
AUTO ANALYSIS RUNNING
    """)
