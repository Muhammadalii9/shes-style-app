import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

st.title("✂️ She's Style Tailors - Digital Register")

# --- Google Sheets Connection ---
# Aapki sheet ka link yahan connect ho raha hai
conn = st.connection("gsheets", type=GSheetsConnection)
url = "https://docs.google.com/spreadsheets/d/19hHI5vz6-LhnP_egTPGaRjmp89zelGEWPqcCZ0xrk7o/edit?usp=sharing"

# --- 1. Customer Details ---
st.header("👤 Customer Details")
col_inf1, col_inf2, col_inf3 = st.columns(3)
with col_inf1:
    name = st.text_input("Customer Name")
with col_inf2:
    phone = st.text_input("Phone Number")
with col_inf3:
    d_date = st.date_input("Delivery Date", datetime.now() + timedelta(days=7))

st.divider()

# --- 2. Kameez Ka Nap ---
st.header("📏 Kameez Ka Nap")
k1, k2, k3, k4 = st.columns(4)
with k1:
    l = st.number_input("Lambai (Length)", value=38.0, step=1.0)
    s = st.number_input("Shoulder (Tera)", value=14.0, step=1.0)
    c = st.number_input("Chest (Seena)", value=34.0, step=1.0)
with k2:
    k = st.number_input("Kamar (Waist)", value=32.0, step=1.0)
    h = st.number_input("Hip", value=36.0, step=1.0)
    chak = st.number_input("Chak", value=20.0, step=1.0)
with k3:
    daman = st.number_input("Daman", value=22.0, step=1.0)
    astin = st.number_input("Astin (Sleeve)", value=20.0, step=1.0)
    armhole = st.number_input("Arm Hole", value=9.0, step=0.5)
with k4:
    dan_astin = st.number_input("Dan Astin", value=5.0, step=0.5)
    gala_f = st.text_input("Gala Front", "6x7")
    gala_b = st.text_input("Gala Back", "Normal")

st.divider()

# --- 3. Shalwar Ka Nap ---
st.header("👖 Shalwar Ka Nap")
s1, s2, s3 = st.columns(3)
with s1:
    s_l = st.number_input("Shalwar Lambai", value=38.0, step=1.0)
with s2:
    s_w = st.number_input("Shalwar Chodai", value=22.0, step=1.0)
with s3:
    s_p = st.number_input("Paicha", value=6.5, step=0.5)

st.divider()

# --- 4. Billing ---
st.header("💰 Billing")
p1, p2, p3 = st.columns(3)
with p1:
    total_bill = st.number_input("Total Bill", value=1500.0, step=50.0)
with p2:
    advance_pay = st.number_input("Advance Payment", value=500.0, step=50.0)
with p3:
    remaining_bal = float(total_bill) - float(advance_pay)
    st.metric(label="Baqi (Balance)", value=f"{remaining_bal}")

note = st.text_area("Extra Notes (Lace, Piping, Design Details)")

# --- Action Button ---
st.divider()
if st.button("✅ SAVE TO SHEET & GENERATE RECEIPT", use_container_width=True):
    if name:
        try:
            # Data tayyar karna
            new_data = pd.DataFrame([{
                "Date": datetime.now().strftime("%d-%m-%Y"),
                "Name": name, "Phone": phone, "Delivery": d_date.strftime("%d-%m-%Y"),
                "L": l, "S": s, "C": c, "K": k, "H": h, "Chak": chak, "D": daman,
                "Astin": astin, "ArmH": armhole, "DanA": dan_astin,
                "Gala_F": gala_f, "Gala_B": gala_b,
                "Sh_L": s_l, "Sh_W": s_w, "Sh_P": s_p,
                "Total": total_bill, "Advance": advance_pay, "Balance": remaining_bal,
                "Note": note
            }])
            
            # Maujooda data parhna aur naya add karna
            existing_df = conn.read(spreadsheet=url)
            updated_df = pd.concat([existing_df, new_data], ignore_index=True)
            
            # Google Sheet update karna
            conn.update(spreadsheet=url, data=updated_df)
            
            st.success(f"Mubarak ho! {name} ka record Google Sheet mein save ho gaya.")
            st.balloons()
            
            # Receipt for Screenshot
            st.code(f"SHE'S STYLE TAILORS\nName: {name}\nL:{l} S:{s} C:{c}\nBAL: {remaining_bal}")
            
        except Exception as e:
            st.error(f"Sheet mein save nahi hua. Wajah: {e}")
    else:
        st.error("Pehle Customer ka naam likhen!")
