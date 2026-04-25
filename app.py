import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

st.title("✂️ She's Style Tailors - Digital Register")

# --- 1. Customer & Delivery ---
st.header("👤 Customer Details")
col_inf1, col_inf2, col_inf3 = st.columns(3)
with col_inf1:
    name = st.text_input("Customer Name")
with col_inf2:
    phone = st.text_input("Phone Number")
with col_inf3:
    d_date = st.date_input("Delivery Date", datetime.now() + timedelta(days=7))

st.divider()

# --- 2. Kameez Ka Nap (Detailed) ---
st.header("📏 Kameez Ka Nap")
k1, k2, k3, k4 = st.columns(4)

with k1:
    l = st.number_input("Lambai (Length)", value=38.0, step=1.0)
    s = st.number_input("Shoulder (Tera)", value=14.0, step=1.0)
    c = st.number_input("Chest (Seena)", value=34.0, step=1.0)

with k2:
    k = st.number_input("Kamar (Waist)", value=32.0, step=1.0)
    h = st.number_input("Hip", value=36.0, step=1.0)
    chak = st.number_input("Chak", value=20.0, step=1.0) # Naya Add Hua

with k3:
    daman = st.number_input("Daman", value=22.0, step=1.0)
    astin = st.number_input("Astin (Sleeve)", value=20.0, step=1.0) # Naya Add Hua
    armhole = st.number_input("Arm Hole", value=9.0, step=0.5) # Naya Add Hua

with k4:
    dan_astin = st.number_input("Dan Astin", value=5.0, step=0.5) # Naya Add Hua
    gala_f = st.text_input("Gala Front", "6x7")
    gala_b = st.text_input("Gala Back", "Normal")

st.divider()

# --- 3. Shalwar Ka Nap (Alag Section) ---
st.header("👖 Shalwar Ka Nap")
s1, s2, s3 = st.columns(3)
with s1:
    s_l = st.number_input("Shalwar Lambai", value=38.0, step=1.0)
with s2:
    s_w = st.number_input("Shalwar Gher/Chodai", value=22.0, step=1.0) # Naya Add Hua
with s3:
    s_p = st.number_input("Paicha", value=6.5, step=0.5)

st.divider()

# --- 4. Billing ---
st.header("💰 Billing")
p1, p2 = st.columns(2)
with p1:
    total = st.number_input("Total Bill", value=1500, step=50.0)
with p2:
    adv = st.number_input("Advance Payment", value=500, step=50.0)

bal = total - adv
st.metric(label="Baqi (Balance)", value=f"{bal}")

note = st.text_area("Extra Notes (Lace, Piping, Design Details)")

# --- Action Button ---
st.divider()
if st.button("✅ SAVE & GENERATE RECEIPT", use_container_width=True):
    if name:
        st.success(f"Master Alii, {name} ka record ready he!")
        st.balloons()
        
        # Receipt for iTech Printer
        st.markdown("### 🧾 RECEIPT FOR PRINTER")
        receipt_text = f"""
        SHE'S STYLE TAILORS
        ------------------
        Name: {name}
        Date: {datetime.now().strftime("%d-%m-%Y")}
        Delivery: {d_date.strftime("%d-%m-%Y")}
        ------------------
        KAMEEZ:
        L:{l} | S:{s} | C:{c}
        K:{k} | H:{h} | Chak:{chak}
        Dam:{daman} | Ast:{astin}
        ArmH:{armhole} | DanA:{dan_astin}
        Gala: F:{gala_f} / B:{gala_b}
        ------------------
        SHALWAR:
        L:{s_l} | Chodai:{s_w} | P:{s_p}
        ------------------
        TOTAL: {total} | ADV: {adv}
        BAL: {bal}
        ------------------
        Note: {note}
        """
        st.code(receipt_text)
        st.info("Iski screenshot len aur iTech printer se print nikal len.")
    else:
        st.error("Meharbani karke Customer ka naam likhen!")
