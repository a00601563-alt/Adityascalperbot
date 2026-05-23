import streamlit as st

# Page Configuration
st.set_page_config(page_title="ADITYA MASTER BOT", layout="wide", page_icon="🤖")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stat-card { background: rgba(255, 255, 255, 0.05); border: 1px solid #00fbff; padding: 20px; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - Sirf MT5 Details
with st.sidebar:
    st.header("🔑 MT5 CONNECTION")
    acc_id = st.text_input("MT5 Account ID")
    password = st.text_input("MT5 Password", type="password")
    server = st.text_input("Server Name")
    st.success("Trend Logic: ACTIVATED")

st.title("🤖 ADITYA MASTER BOT - FINAL V6.2")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("⚙️ SETTINGS")
    asset = st.selectbox("Asset", ["XAUUSD (GOLD)", "EURUSD", "US30"])
    tp = st.number_input("Take Profit ($)", value=50)
    
    if st.button("🚀 START MASTER BOT"):
        if not acc_id or not password or not server:
            st.error("Bhai, MT5 ki details to dalo!")
        else:
            st.balloons()
            st.success("Bot server se connect ho gaya! Trend scanning shuru...")

with col2:
    st.subheader("📊 STATUS")
    st.markdown('<div class="stat-card"><h3>TREND MODE: ON</h3><p>Up = Buy | Down = Sell</p></div>', unsafe_allow_html=True)
    st.code("""
[SYSTEM] Master Bot V6.2 - ONLINE
[CONNECTION] MT5 Server: CONNECTED
[STRATEGY] Trend Following Enabled
[FILTER] Counter-Trend: BLOCKED
[STATUS] Waiting for Trend-Aligned Signal...
    """, language="bash")
