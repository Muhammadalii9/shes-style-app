import streamlit as st
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

st.title("✂️ She's Style Tailors - Digital Register")

# --- 1. Customer Details ---
st.header("👤 Customer Details")
c1, c2, c3 = st.columns(3)
with c1:
    name = st.text_input("Customer Name")
with c2:
    phone = st.text_input("Phone Number")
with c3:
    d_date = st.date_input("Delivery Date", datetime.now() + timedelta(days=7))

st.divider()

# --- 2. Kameez Ka Nap ---
st.header("📏 Kameez Ka Nap")
k1, k2, k3, k4 = st.columns(4)
with k1:
    l = st.number_input("Lambai", value=38.0, step=1.0)
    s = st.number_input("Shoulder", value=14.0, step=1.0)
    c = st.number_input("Chest", value=34.0, step=1.0)
with k2:
    k = st.number_input("Kamar", value=32.0, step=1.0)
    h = st.number_input("Hip", value=36.0, step=1.0)
    chak = st.number_input("Chak", value=20.0, step=1.0)
with k3:
    daman = st.number_input("Daman", value=22.0, step=1.0)
    astin = st.number_input("Astin", value=20.0, step=1.0)
    armh = st.number_input("Arm Hole", value=9.0, step=0.5)
with k4:
    dana = st.number_input("Dan Astin", value=5.0, step=0.5)
    gf = st.text_input("Gala Front", "6x7")
    gb = st.text_input("Gala Back", "Normal")

st.divider()

# --- 3. Shalwar Ka Nap ---
st.header("👖 Shalwar Ka Nap")
s1, s2, s3 = st.columns(3)
with s1:
    sl = st.number_input("Shalwar Lambai", value=38.0, step=1.0)
with s2:
    sw = st.number_input("Shalwar Chodai", value=22.0, step=1.0)
with s3:
    sp = st.number_input("Paicha", value=6.5, step=0.5)

st.divider()

# --- 4. Billing ---
st.header("💰 Billing")
b1, b2 = st.columns(2)
with b1:
    total = st.number_input("Total Bill", value=1500, step=50.0)
with b2:
    adv = st.number_input("Advance", value=500, step=50.0)
bal = total - adv
st.metric("Baqi (Balance)", f"{bal}")

note = st.text_area("Extra Notes")

st.divider()

# --- Action Button ---
if st.button("✅ GENERATE RECEIPT & SAVE", use_container_width=True):
    if name:
        st.success(f"{name} ka record ready hai!")
        
        # Receipt UI
        st.markdown("### 🧾 RECEIPT FOR iTech PRINTER")
        receipt = f"""
        SHE'S STYLE TAILORS
        ------------------
        Name: {name} | Date: {datetime.now().strftime("%d-%m")}
        Delivery: {d_date.strftime("%d-%m")}
        ------------------
        KAMEEZ:
        L:{l} | S:{s} | C:{c} | K:{k}
        H:{h} | Chak:{chak} | D:{daman}
        Ast:{astin} | AH:{armh} | DA:{dana}
        Gala: F:{gf} / B:{gb}
        ------------------
        SHALWAR:
        L:{sl} | Chodai:{sw} | P:{sp}
        ------------------
        BILL: {total} | ADV: {adv} | BAL: {bal}
        ------------------
        Note: {note}
        """
        st.code(receipt)
        st.balloons()
        
        st.warning("⚠️ Record sheet mein bhejne ke liye niche wala button dabayen:")
        # Yahan apna Google Form ka link dal sakte hain
        st.link_button("📂 Open Google Sheet Form", "https://docs.google.com/spreadsheets/d/19hHI5vz6-LhnP_egTPGaRjmp89zelGEWPqcCZ0xrk7o/edit")
    else:
        st.error("Pehle Naam likhen!")
