import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

DB_FILE = "tailor_data.csv"

def load_data():
    if os.path.exists(DB_FILE):
        try:
            return pd.read_csv(DB_FILE)
        except:
            return pd.DataFrame()
    return pd.DataFrame()

def save_to_file(new_record):
    df = load_data()
    updated_df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    updated_df.to_csv(DB_FILE, index=False)

def delete_record(index_to_delete):
    df = load_data()
    if not df.empty:
        df = df.drop(index_to_delete).reset_index(drop=True)
        df.to_csv(DB_FILE, index=False)
        return True
    return False

# --- Receipt UI Function ---
def show_receipt(data):
    st.markdown(f"""
    <div style="background-color: white; color: black; padding: 20px; font-family: 'Courier New', Courier, monospace; border: 2px solid black; width: 320px; margin: auto; line-height: 1.2;">
        <h2 style="text-align: center; margin: 0;">SHE'S STYLE</h2>
        <p style="text-align: center; margin: 0; font-size: 12px;">TAILORS - QUETTA</p>
        <hr style="border-top: 2px solid black;">
        <p><b>NAME:</b> {str(data['Name']).upper()}</p>
        <p><b>DATE:</b> {data['Date']}</p>
        <p style="background-color: #eee; padding: 5px;"><b>DELIVERY: {data['Delivery']}</b></p>
        <hr style="border-top: 1px dashed black;">
        <p><b>KAMEEZ:</b> {data['L']} | {data['S']} | {data['C']} | {data['K']}</p>
        <p>H:{data['H']} | Ch:{data['Chak']} | D:{data['Daman']} | Ast:{data['Astin']}</p>
        <p>Gala: {data['GalaF']} / {data['GalaB']}</p>
        <hr style="border-top: 1px dashed black;">
        <p><b>SHALWAR:</b> {data['ShalwarD']}</p>
        <p>L:{data['ShalwarL']} | Loos:{data['ShalwarLoos']} | P:{data['Paicha']}</p>
        <hr style="border-top: 2px solid black;">
        <p>TOTAL: Rs. {data['Total']}</p>
        <p>ADVANCE: Rs. {data['Adv']}</p>
        <p style="font-size: 18px;"><b>BALANCE: Rs. {data['Bal']}</b></p>
        <hr style="border-top: 1px dashed black;">
        <p style="font-size: 18px; text-align: center;">{data['Note']}</p>
        <p style="text-align: center; font-size: 14px; margin-top: 10px;">THANK YOU!</p>
    </div>
    """, unsafe_allow_html=True)

st.title("✂️ She's Style Tailors - Digital Measurement")

# --- 🔍 SEARCH ---
st.header("🔍 Search Customer")
search_query = st.text_input("Naam ya Phone Number:")
db = load_data()
if search_query and not db.empty:
    res = db[db['Name'].astype(str).str.contains(search_query, case=False, na=False) | 
             db['Phone'].astype(str).str.contains(search_query, na=False)]
    if not res.empty:
        st.dataframe(res)

st.divider()

# --- 📝 FORM ---
st.header("📝 New Measurement")
col1, col2, col3 = st.columns(3)
with col1: name = st.text_input("Customer Name")
with col2: phone = st.text_input("Phone Number")
with col3: d_date = st.date_input("Delivery Date", datetime.now() + timedelta(days=7))

# Measurements
st.subheader("Kameez")
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

st.subheader("Shalwar")
s1, s2, s3, s4 = st.columns(4)
with s1: sd = st.text_input("Shalwar Design")
with s2: sl = st.number_input("Shalwar Lambai", value=36.0, step=0.5)
with s3: sw = st.number_input("Loosing", value=15.0, step=0.5)
with s4: sp = st.number_input("Paicha", value=7.5, step=0.5)

st.divider()
st.subheader("Billing")
b1, b2 = st.columns(2)
with b1: total = st.number_input("Total", value=1000, step=100)
with b2: adv = st.number_input("Advance", value=0, step=100)
bal = total - adv
st.metric("Balance to Pay", f"Rs. {bal}")
note = st.text_area("Note (Optional)")

if st.button("💾 SAVE RECORD", use_container_width=True):
    if name:
        rec = {
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Name": name, "Phone": phone, "Delivery": d_date.strftime("%Y-%m-%d"),
            "L": l, "S": s, "C": c, "K": k, "H": h, "Chak": chak, "Daman": daman,
            "Astin": astin, "AH": armh, "DanA": dana, "GalaF": gf, "GalaB": gb,
            "ShalwarD": sd, "ShalwarL": sl, "ShalwarLoos": sw, "Paicha": sp,
            "Total": total, "Adv": adv, "Bal": bal, "Note": note
        }
        save_to_file(rec)
        st.success("Record Saved Successfully!")
        show_receipt(rec)
    else:
        st.error("Pehle Naam likhen!")

st.divider()

# --- 📊 HISTORY & RE-PRINT ---
st.header("📊 History & Re-Print")
history_db = load_data()
if not history_db.empty:
    st.write("Raseed nikalne ke liye select karen:")
    customer_list = [f"{idx}: {row['Name']} ({row['Date']})" for idx, row in history_db.iterrows()]
    selected_option = st.selectbox("Select Customer", customer_list)
    
    if selected_option:
        selected_idx = int(selected_option.split(":")[0])
        selected_data = history_db.iloc[selected_idx]
        
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            if st.button("📄 View Receipt"):
                show_receipt(selected_data)
        with col_p2:
            if st.button("🗑️ Delete Record"):
                if delete_record(selected_idx):
                    st.warning("Deleted!")
                    st.rerun()
    
    st.dataframe(history_db)
