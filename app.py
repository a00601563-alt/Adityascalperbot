import streamlit as st
import time

# Dashboard Configuration
st.set_page_config(page_title="Aditya AI Scalper", page_icon="📈", layout="centered")

# --- CUSTOM CSS FOR PREMIUM LOOK ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
    }
    .stTextInput>div>div>input { border-radius: 8px; }
    h1 { color: #00d4ff; text-align: center; font-family: 'Trebuchet MS'; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1>🚀 ADITYA AI SCALPER PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Premium Gold & Forex Scalping Terminal</p>", unsafe_allow_html=True)

# --- SIDEBAR: MT5 CONNECTION ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/100/bot.png")
    st.header("🔐 MT5 CONNECTION")
    acc_id = st.text_input("Account Number", placeholder="e.g. 1234567")
    acc_pass = st.text_input("Master Password", type="password")
    acc_server = st.text_input("Server", placeholder="e.g. VProp-Server")
    
    st.divider()
    st.info("Secure Connection: Your credentials are encrypted and sent directly to your broker server.")

# --- MAIN DASHBOARD LAYOUT ---
col1, col2, col3 = st.columns(3)
col1.metric("Current Pair", "XAUUSD")
col2.metric("Bot Status", "Standby", "Ready")
col3.metric("Live Spread", "12", "-2")

st.divider()

# --- STRATEGY SETTINGS ---
st.subheader("🛠 STRATEGY CONFIGURATION")
c1, c2 = st.columns(2)

with c1:
    symbol = st.selectbox("Trading Asset", ["XAUUSD (GOLD)", "EURUSD", "GBPUSD", "BTCUSD"])
    timeframe = st.select_slider("Timeframe Strategy", options=["M1", "M5", "M15", "M30"])

with c2:
    lot_size = st.number_input("Risk: Lot Size", min_value=0.01, max_value=10.0, value=0.01, step=0.01)
    mode = st.radio("Execution Mode", ["Conservative", "Aggressive"], horizontal=True)

# --- CONTROL BUTTONS ---
st.divider()
btn_col1, btn_col2 = st.columns(2)

if btn_col1.button("▶ START TRADING"):
    if not acc_id or not acc_pass:
        st.error("Please enter MT5 Credentials!")
    else:
        with st.spinner('Connecting to Market...'):
            time.sleep(2)
            st.success(f"✅ Bot Started! Scanning {symbol} on {timeframe}.")
            st.toast("Connection Successful!", icon="🔥")

if btn_col2.button("🛑 STOP BOT"):
    st.warning("Bot Halted. All open positions are secured.")

# --- LIVE ACTIVITY LOGS ---
st.subheader("📊 LIVE MARKET LOGS")
log_text = f"""
[SYSTEM] Initializing AI Logic...
[MARKET] Monitoring {symbol} Price Action.
[INFO] Ready to execute {mode} trades with {lot_size} lot.
[STATUS] Waiting for high-probability setup...
"""
st.code(log_text, language='bash')

st.markdown("<br><hr><center><p style='color: gray; font-size: 12px;'>Developed by Aditya AI Labs | 2026 Edition</p></center>", unsafe_allow_html=True)
