import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

st.title("✂️ She's Style Tailors - MacBook POS")

# --- Form Inputs ---
st.header("👤 Customer & Order")
c1, c2, c3 = st.columns(3)
with c1:
    name = st.text_input("Customer Name")
with c2:
    phone = st.text_input("Phone Number")
with c3:
    d_date = st.date_input("Delivery Date", datetime.now() + timedelta(days=7))

st.divider()

# --- Measurements ---
st.header("📏 Measurements")
k1, k2, k3, k4 = st.columns(4)
with k1:
    l = st.number_input("Lambai", value=38.0, step=0.5)
    s = st.number_input("Shoulder", value=14.0, step=0.5)
    c = st.number_input("Chest", value=20.0, step=0.5)
with k2:
    k = st.number_input("Kamar", value=18.0, step=0.5)
    h = st.number_input("Hip", value=21.0, step=0.5)
    chak = st.number_input("Chak", value=12.0, step=0.5)
with k3:
    daman = st.number_input("Daman", value=22.0, step=0.5)
    astin = st.number_input("Astin", value=20.0, step=0.5)
    armh = st.number_input("Arm Hole", value=9.0, step=0.5)
with k4:
    dana = st.number_input("Dan Astin", value=6.0, step=0.5)
    gf = st.text_input("Gala Front", "7x5")
    gb = st.text_input("Gala Back", "Normal")

st.divider()

# --- Shalwar ---
st.header("👖 Shalwar Details")
s1, s2, s3, s4 = st.columns(4)
with s1:
    sl = st.number_input("Shalwar Lambai", value=36.0, step=0.5)
with s2:
    sw = st.number_input("Shalwar Loosing", value=16.0, step=0.5)
with s3:
    sp = st.number_input("Paicha", value=7.5, step=0.5)
with s4:
    sp = st.text_input("shalwar")
    
st.divider()

# --- Billing ---
b1, b2 = st.columns(2)
with b1:
    total = st.number_input("Total Bill", value=1000.0, step=100.0)
with b2:
    adv = st.number_input("Advance Payment", value=0.0, step=100.0)
bal = float(total) - float(adv)
st.metric("BAQI (BALANCE)", f"Rs. {bal}")

note = st.text_area("Karigar Note")

# --- Print Action ---
if st.button("✅ PREPARE RECEIPT", use_container_width=True):
    if name:
        order_date = datetime.now().strftime("%d/%m/%Y")
        delivery_str = d_date.strftime("%d/%m/%Y")
        
        # Receipt UI
        st.markdown(f"""
        <div style="background-color: white; color: black; padding: 20px; font-family: monospace; border: 1px solid #ccc; width: 300px; margin: auto;">
            <h3 style="text-align: center;">SHE'S STYLE TAILORS</h3>
            <p style="text-align: center;">Quetta, Pakistan</p>
            <hr>
            <p>NAME: {name.upper()}</p>
            <p>DATE: {order_date}</p>
            <p>DELIVERY: {delivery_str}</p>
            <hr>
            <p>L:{l} S:{s} C:{c} K:{k}</p>
            <p>H:{h} Chak:{chak} D:{daman}</p>
            <p>Ast:{astin} AH:{armh} DA:{dana}</p>
            <p>Gala: {gf} / {gb}</p>
            <hr>
            <p>SHALWAR: L:{sl} Loos:{sw} P:{sp}</p>
            <hr>
            <p>TOTAL: Rs. {total}</p>
            <p>ADV:   Rs. {adv}</p>
            <p><b>BAL:   Rs. {bal}</b></p>
            <hr>
            <p style="text-align: center; font-size: 20px;">{note}</p>
            <p style="text-align: center;">*** THANK YOU ***</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 MacBook par Print ke liye: **Command + P** dabayen.")
    else:
        st.error("Pehle Name likhen!")
