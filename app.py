import streamlit as st
import pandas as pd
from datetime import datetime

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

# Database ko temporarily save rakhne ke liye
if 'orders' not in st.session_state:
    st.session_state.orders = []

st.title("✂️ She's Style Tailors - Digital Register")

# --- 1. Customer Ki Bunyadi Maloomat ---
st.header("👤 Customer Details")
c_name = st.text_input("Customer ka Naam")
c_phone = st.text_input("Phone Number")

st.divider()

# --- 2. Suit Ka Naap (Kameez) ---
st.header("📏 Kameez ka Naap")
k1, k2, k3 = st.columns(3)

with k1:
    lambai = st.number_input("Lambai (Length)", value=38.0)
    shoulder = st.number_input("Shoulder (Tera)", value=14.0)
    chest = st.number_input("Chest (Seena)", value=34.0)
    kamar = st.number_input("Kamar (Waist)", value=32.0)

with k2:
    hip = st.number_input("Hip", value=36.0)
    chak = st.number_input("Chak", value=11.0)
    daman = st.number_input("Daman", value=22.0)

with k3:
    sleeve = st.number_input("Sleeve (Astin)", value=20.0)
    armhole = st.number_input("Arm Hole", value=8.5)
    dan_astin = st.number_input("Dan Astin", value=5.0)

st.divider()

# --- 3. Shalwar Ka Naap ---
st.header("👖 Shalwar ka Naap")
s1, s2, s3 = st.columns(3)

with s1:
    s_lambai = st.number_input("Shalwar Lambai", value=38.0)
with s2:
    loosing = st.number_input("Loosing", value=2.5)
with s3:
    paicha = st.number_input("Paicha", value=6.5)

st.divider()

# --- 4. Description ---
description = st.text_area("📝 Mazeed Tafseel (Design, Lace, Piping etc.)")

# --- 5. Save aur Receipt Buttons ---
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("✅ Save & Add to List"):
        if c_name:
            # Data List mein shamil karna
            order_data = {
                "Time": datetime.now().strftime("%I:%M %p"),
                "Name": c_name, "Phone": c_phone, "L": lambai, "S": shoulder,
                "C": chest, "K": kamar, "H": hip, "Ch": chak, "D": daman,
                "Sl": sleeve, "AH": armhole, "DA": dan_astin,
                "ShL": s_lambai, "Loo": loosing, "P": paicha, "Note": description
            }
            st.session_state.orders.append(order_data)
            st.success(f"{c_name} ka naap save ho gaya!")
            st.balloons()
        else:
            st.error("Pehle Naam likhein!")

with col_btn2:
    if st.button("🧾 Generate Receipt"):
        if c_name:
            st.subheader("🧾 Business Receipt - She's Style")
            receipt_text = f"""
            **Customer:** {c_name} | **Phone:** {c_phone}
            ---
            **Kameez:** L:{lambai} | S:{shoulder} | C:{chest} | K:{kamar} | H:{hip} | Ch:{chak} | D:{daman} | Sl:{sleeve} | AH:{armhole} | DA:{dan_astin}
            **Shalwar:** L:{s_lambai} | Loosing:{loosing} | P:{paicha}
            ---
            **Notes:** {description}
            """
            st.info(receipt_text)
            st.write("💡 Iska screenshot le kar customer ko bhej den.")

# --- Aaj ki List (Download Option) ---
if st.session_state.orders:
    st.divider()
    st.subheader("📋 Aaj ki List")
    df = pd.DataFrame(st.session_state.orders)
    st.table(df)
    
    # Download Button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Excel File", data=csv, file_name="Today_Orders.csv", mime='text/csv')
