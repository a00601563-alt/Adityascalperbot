import streamlit as st
import MetaTrader5 as mt5
import pandas as pd

st.set_page_config(page_title="ADITYA AI", layout="wide")

# ===== STYLE =====
st.markdown("""
<style>
.stApp{background:white;color:black;}
.stButton button{
background:red;color:white;
border:none;border-radius:10px;
font-weight:bold;
}
.box{
padding:15px;
background:#f5f5f5;
border-radius:10px;
text-align:center;
margin:5px;
}
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====
with st.sidebar:

    st.title("🤖 ADITYA AI")

    login_id = st.text_input("MT5 Login ID")
    password = st.text_input("Password", type="password")
    server = st.text_input("Server")

    pair = st.selectbox(
        "Select Pair",
        [
            "XAUUSD","EURUSD","GBPUSD",
            "USDJPY","AUDUSD","USDCAD"
        ]
    )

    timeframe = st.selectbox(
        "Timeframe",
        ["M1","M5"]
    )

    lot = st.number_input(
        "Lot Size",
        0.01,5.0,0.01
    )

    tp = st.number_input(
        "Take Profit ($)",
        1,10000,50
    )

    sl = st.number_input(
        "Stop Loss ($)",
        1,10000,20
    )

    mode = st.radio(
        "Trading Mode",
        ["SAFE","AGGRESSIVE"]
    )

# ===== TITLE =====
st.title("🤖 ADITYA AI SCALPER")

# ===== CONNECT =====
if st.button("🚀 START BOT"):

    if mt5.initialize():

        login = mt5.login(
            int(login_id),
            password=password,
            server=server
        )

        if login:

            st.success("MT5 CONNECTED ✅")

            # ===== TIMEFRAME =====
            tf = mt5.TIMEFRAME_M1

            if timeframe == "M5":
                tf = mt5.TIMEFRAME_M5

            # ===== MARKET DATA =====
            rates = mt5.copy_rates_from_pos(
                pair, tf, 0, 20
            )

            df = pd.DataFrame(rates)

            last_close = df.close.iloc[-1]
            prev_close = df.close.iloc[-2]

            # ===== AI ANALYSIS =====
            signal = "WAIT"

            if last_close > prev_close:
                signal = "BUY"

            elif last_close < prev_close:
                signal = "SELL"

            # ===== LIVE PRICE =====
            tick = mt5.symbol_info_tick(pair)

            buy_price = tick.ask
            sell_price = tick.bid

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
            LOT<br><b>{lot}</b>
            </div>
            """, unsafe_allow_html=True)

            # ===== AGGRESSIVE =====
            deviation = 20

            if mode == "AGGRESSIVE":
                deviation = 50

            # ===== AUTO TRADE =====
            if signal == "BUY":

                request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": pair,
                    "volume": lot,
                    "type": mt5.ORDER_TYPE_BUY,
                    "price": buy_price,
                    "deviation": deviation,
                    "magic": 100,
                    "comment": "ADITYA AI BUY",
                    "type_time": mt5.ORDER_TIME_GTC,
                    "type_filling": mt5.ORDER_FILLING_IOC,
                }

                mt5.order_send(request)

                st.success("BUY TRADE OPENED ✅")

            elif signal == "SELL":

                request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": pair,
                    "volume": lot,
                    "type": mt5.ORDER_TYPE_SELL,
                    "price": sell_price,
                    "deviation": deviation,
                    "magic": 100,
                    "comment": "ADITYA AI SELL",
                    "type_time": mt5.ORDER_TIME_GTC,
                    "type_filling": mt5.ORDER_FILLING_IOC,
                }

                mt5.order_send(request)

                st.error("SELL TRADE OPENED ✅")

            st.code(f"""
MT5 CONNECTED
PAIR = {pair}
TIMEFRAME = {timeframe}
SIGNAL = {signal}
MODE = {mode}
LIVE MARKET RUNNING
AUTO TRADING ACTIVE
            """)

        else:
            st.error("LOGIN FAILED ❌")

    else:
        st.error("MT5 NOT FOUND ❌")
