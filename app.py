import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="ADITYA AI SCALPER ULTIMATE",
    layout="wide",
    page_icon="🤖"
)

# WHITE THEME CSS
st.markdown("""
<style>

/* FORCE FULL WHITE SCREEN */
html, body, [class*="css"] {
    background-color: white !important;
    color: black !important;
}

/* MAIN APP */
.stApp {
    background: white !important;
}

/* MAIN AREA */
.main {
    background-color: white !important;
    color: black !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #f5f5f5 !important;
}

/* CARDS */
.stat-card {
    background: white;
    border: 1px solid #dcdcdc;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

/* CARD VALUES */
.stat-val {
    font-size: 20px;
    font-weight: bold;
    color: #0077ff;
}

/* INPUT BOXES */
div[data-baseweb="input"] input {
    background-color: white !important;
    color: black !important;
    border: 1px solid #cccccc !important;
    border-radius: 10px;
}

/* SELECT BOX */
div[data-baseweb="select"] > div {
    background-color: white !important;
    color: black !important;
    border: 1px solid #cccccc !important;
    border-radius: 10px;
}

/* BUTTON */
.stButton button {
    background: black !important;
    color: white !important;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    padding: 10px 20px;
}

/* CODE BOX */
.stCodeBlock {
    background-color: #f8f8f8 !important;
    color: black !important;
}

/* TEXT */
label, p, h1, h2, h3, h4, h5, h6, small {
    color: black !important;
}

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

    tf = st.selectbox(
        "Select Timeframe",
        ["1 Minute (M1)", "5 Minutes (M5)"]
    )

    st.info("System Ready: Connection Optimized")

# Header
st.title("🤖 ADITYA AI SCALPER - ULTIMATE V4.2")

left, right = st.columns([1.5, 2])

# LEFT SIDE
with left:

    st.subheader("⚙️ STRATEGY SETTINGS")

    with st.container(border=True):

        selected_asset = st.selectbox(
            "Select Trading Asset",
            [
                "XAUUSD (GOLD)",
                "EURUSD",
                "GBPUSD",
                "USDJPY",
                "AUDUSD",
                "US30",
                "BTCUSD",
                "ETHUSD"
            ]
        )

        lot = st.number_input(
            "Lot Size",
            0.01,
            5.0,
            0.01,
            step=0.01
        )

        mode = st.radio(
            "Execution Mode",
            ["Conservative", "Aggressive"],
            horizontal=True
        )

        st.divider()

        st.markdown("**Profit & Risk Control ($)**")

        control_type = st.segmented_control(
            "Control Mode",
            ["AI Automatic", "Manual Dollars ($)"]
        )

        tp_val, sl_val = "Auto", "Auto"

        if control_type == "Manual Dollars ($)":

            c1, c2 = st.columns(2)

            tp_val = c1.number_input(
                "Take Profit ($)",
                1,
                5000,
                50
            )

            sl_val = c2.number_input(
                "Stop Loss ($)",
                1,
                5000,
                20
            )

    # BUTTON
    if st.button("▶ START TRADING"):

        if not acc_id or not password:

            st.error(
                "Error: Please enter MT5 ID and Password!"
            )

        else:

            st.balloons()

            st.success(
                f"Bot active on {tf} for {selected_asset}!"
            )

# RIGHT SIDE
with right:

    st.subheader("📊 LIVE METRICS")

    m1, m2 = st.columns(2)

    with m1:
        st.markdown(
            f'''
            <div class="stat-card">
                <small>Timeframe</small>
                <div class="stat-val">{tf}</div>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with m2:
        st.markdown(
            '''
            <div class="stat-card">
                <small>Daily P/L</small>
                <div class="stat-val" style="color:#00aa55;">
                    $0.00
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )

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
