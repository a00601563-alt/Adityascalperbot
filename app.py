import streamlit as st

# Page Configuration
st.set_page_config(page_title="ADITYA AI SCALPER ULTIMATE", layout="wide", page_icon="🤖")

# Custom CSS
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
    .stat-val { font-size: 20px; font-weight: bold; color: #00fbff; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🤖 ADITYA BOT")
    st.header("🔑 MASTER ACCESS")
    acc_id = st.text_input("MT5 ID")
    password = st.text_input("Password", type="password")
    server = st.text_input("Server")
    st.divider()
    tf = st.selectbox("Select Timeframe", ["1 Minute (M1)", "5 Minutes (M5)"])
    st.info("System Ready: Connection Optimized")

# Header
st.title("🤖 ADITYA AI SCALPER - ULTIMATE V4.2")

left, right = st.columns([1.5, 2])

with left:
    st.subheader("⚙️ STRATEGY SETTINGS")
    with st.container(border=True):
        selected_asset = st.selectbox("Select Trading Asset", ["XAUUSD (GOLD)", "EURUSD", "GBPUSD", "USDJPY", "AUDUSD", "US30", "BTCUSD", "ETHUSD"])
        lot = st.number_input("Lot Size", 0.01, 5.0, 0.01, step=0.01)
        mode = st.radio("Execution Mode", ["Conservative", "Aggressive"], horizontal=True)
        
        st.divider()
        st.markdown("**Profit & Risk Control ($)**")
        control_type = st.segmented_control("Control Mode", ["AI Automatic", "Manual Dollars ($)"])
        
        tp_val, sl_val = "Auto", "Auto"
        if control_type == "Manual Dollars ($)":
            c1, c2 = st.columns(2)
            tp_val = c1.number_input("Take Profit ($)", 1, 5000, 50)
            sl_val = c2.number_input("Stop Loss ($)", 1, 5000, 20)

    if st.button("▶ START TRADING"):
        if not acc_id or not password:
            st.error("Error: Please enter MT5 ID and Password!")
        else:
            st.balloons()
            st.success(f"Bot active on {tf} for {selected_asset}!")

with right:
    st.subheader("📊 LIVE METRICS")
    m1, m2 = st.columns(2)
    with m1: st.markdown(f'<div class="stat-card"><small>Timeframe</small><div class="stat-val">{tf}</div></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="stat-card"><small>Daily P/L</small><div class="stat-val" style="color:#00ff88;">$0.00</div></div>', unsafe_allow_html=True)
    
    st.subheader("📜 LIVE INTELLIGENCE LOGS")
    with st.container(border=True):
        st.code(f"""
[SYSTEM] Aditya AI V4.2 - FULLY LOADED
[TIMEFRAME] {tf} Analysis Enabled
[ASSET] Tracking: {selected_asset}
[MODE] {mode}
[LOG] Scanning Trend -> UP=BUY, DOWN=SELL
[STATUS] Waiting for high-probability entry...
        """, language="bash")

st.write("---")
st.caption("Aditya AI Labs | Scalping Terminal 2026")
