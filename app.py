import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

if 'orders' not in st.session_state:
    st.session_state.orders = []

st.title("✂️ She's Style Tailors - Digital Register")

# --- 1. Customer & Delivery Details ---
st.header("👤 Customer & Delivery")
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1:
    c_name = st.text_input("Customer Name")
with col_c2:
    c_phone = st.text_input("Phone Number")
with col_c3:
    # Default delivery date 1 hafta baad ki
    delivery_date = st.date_input("Delivery Date", datetime.now() + timedelta(days=7))

st.divider()

# --- 2. Suit Measurements (Kameez) ---
st.header("📏 Kameez ka Naap")
k1, k2, k3, k4 = st.columns(4)

with k1:
    lambai = st.number_input("Lambai (Length)", value=38.0)
    shoulder = st.number_input("Shoulder (Tera)", value=14.0)
    chest = st.number_input("Chest (Seena)", value=34.0)

with k2:
    kamar = st.number_input("Kamar (Waist)", value=32.0)
    hip = st.number_input("Hip", value=36.0)
    chak = st.number_input("Chak", value=11.0)

with k3:
    daman = st.number_input("Daman", value=22.0)
    sleeve = st.number_input("Sleeve (Astin)", value=20.0)
    armhole = st.number_input("Arm Hole", value=8.5)

with k4:
    dan_astin = st.number_input("Dan Astin", value=5.0)
    # GALA KA OPTION
    gala_design = st.text_input("Gala Design (e.g. V-Shape, Round)", "Round")
    gala_size = st.text_input("Gala Size (e.g. 6x7)", "6x6")

st.divider()

# --- 3. Shalwar ka Naap ---
st.header("👖 Shalwar ka Naap")
s1, s2, s3 = st.columns(3)
with s1:
    s_lambai = st.number_input("Shalwar Lambai", value=38.0)
with s2:
    loosing = st.number_input("Loosing", value=2.5)
with s3:
    paicha = st.number_input("Paicha", value=6.5)

st.divider()

# --- 4. Paiso ka Hisab (Billing) ---
st.header("💰 Billing & Payment")
p1, p2, p3 = st.columns(3)
with p1:
    total_bill = st.number_input("Total Mazdoori", value=1500)
with p2:
    advance = st.number_input("Advance Payment", value=500)
with p3:
    balance = total_bill - advance
    st.write(f"**Baqi (Balance):** {balance}")
    st.metric(label="Remaining Amount", value=balance)

# --- 5. Description ---
description = st.text_area("📝 Extra Notes (Lace, Piping, Karigar Instructions)")

# --- Buttons ---
st.divider()
if st.button("✅ Save & Generate Receipt"):
    if c_name:
        order_data = {
            "Date": datetime.now().strftime("%d-%m"),
            "Delivery": delivery_date.strftime("%d-%m"),
            "Name": c_name, "Total": total_bill, "Bal": balance,
            "L": lambai, "S": shoulder, "C": chest, "K": kamar, "H": hip, 
            "Gala": f"{gala_design} ({gala_size})", "Note": description
        }
        st.session_state.orders.append(order_data)
        
        # --- Raseed ka Design (Printer ke liye) ---
        st.success("Record Saved!")
        st.subheader("🧾 Printing Receipt")
        receipt_box = f"""
        **SHE'S STYLE TAILORS**
        -------------------------
        **Date:** {datetime.now().strftime("%d-%m-%Y")}
        **Delivery:** {delivery_date.strftime("%d-%m-%Y")}
        **Customer:** {c_name} ({c_phone})
        -------------------------
        **KAMEEZ:**
        L:{lambai} | S:{shoulder} | C:{chest}
        K:{kamar} | H:{hip} | Ch:{chak} | D:{daman}
        Sl:{sleeve} | AH:{armhole} | DA:{dan_astin}
        **GALA:** {gala_design} ({gala_size})
        -------------------------
        **SHALWAR:**
        L:{s_lambai} | Loo:{loosing} | P:{paicha}
        -------------------------
        **BILL:** Total: {total_bill} | Adv: {advance} | **BAL: {balance}**
        **Note:** {description}
        """
        st.info(receipt_text if 'receipt_text' in locals() else receipt_box)
        st.balloons()
    else:
        st.error("Naam likhna zaroori hai!")

# --- Table ---
if st.session_state.orders:
    st.divider()
    st.table(pd.DataFrame(st.session_state.orders))
