import streamlit as st

# Page Configuration - Mobile Friendly
st.set_page_config(page_title="ADITYA AI SCALPER ULTIMATE", layout="wide", page_icon="🤖")

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

# Sidebar - Login Details
with st.sidebar:
    st.markdown("## 🤖 ADITYA BOT")
    st.image("https://cdn-icons-png.flaticon.com/512/2091/2091665.png", width=80)
    st.header("🔑 MASTER ACCESS")
    acc_id = st.text_input("MT5 ID", placeholder="Account Number")
    password = st.text_input("Password", type="password")
    server = st.text_input("Server", placeholder="Broker Server Name")
    st.divider()
    st.info("System Ready: Connection Optimized")

# Header
st.title("🤖 ADITYA AI SCALPER - ULTIMATE V4.0")
st.write("---")

# Main Content
left, right = st.columns([1.5, 2])

with left:
    st.subheader("⚙️ STRATEGY SETTINGS")
    with st.container(border=True):
        selected_asset = st.selectbox("Select Trading Asset", ["XAUUSD (GOLD)", "EURUSD", "GBPUSD", "US30", "BTCUSD"])
        lot = st.number_input("Lot Size", 0.01, 5.0, 0.01, step=0.01)
        mode = st.radio("Execution Mode", ["Conservative 🛡️", "Aggressive 🔥"], horizontal=True)
        
        st.divider()
        st.markdown("**Profit & Risk Control (In Dollars $)**")
        control_type = st.segmented_control("Control Mode", ["AI Automatic 🤖", "Manual Dollars ($) 💰"])
        
        tp_val, sl_val = "Auto", "Auto"
        if control_type == "Manual Dollars ($) 💰":
            c1, c2 = st.columns(2)
            tp_val = c1.number_input("Take Profit ($)", 1, 5000, 50)
            sl_val = c2.number_input("Stop Loss ($)", 1, 5000, 20)

    if st.button("▶ START TRADING"):
        if not acc_id or not password:
            st.error("Bhai, pehle MT5 ID aur Password dalo!")
        else:
            st.balloons()
            st.success(f"Bot connected to {server}! Trading {selected_asset} started.")
            
    if st.button("🛑 STOP BOT"):
        st.error("System Offline")

with right:
    st.subheader("📊 LIVE METRICS")
    m1, m2 = st.columns(2)
    with m1: st.markdown(f'<div class="stat-card"><small>Selected Pair</small><div class="stat-val">{selected_asset}</div></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="stat-card"><small>Daily P/L</small><div class="stat-val" style="color:#00ff88;">$0.00</div></div>', unsafe_allow_html=True)
    
    st.subheader("📜 LIVE INTELLIGENCE LOGS")
    with st.container(border=True):
        st.code(f"""
[SYSTEM] Aditya AI V4.0 - BOOTED
[AUTH] Login Attempt: {acc_id if acc_id else 'Waiting...'}
[SERVER] Connected to: {server if server else 'Scan Mode'}
[CONFIG] Asset: {selected_asset} | Lot: {lot}
[TARGETS] TP: ${tp_val} | SL: ${sl_val}
[STATUS] Scanning Market for high-volatility candles...
        """, language="bash")

st.write("---")
st.caption("Aditya AI Labs | Scalping Terminal 2026")
