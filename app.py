import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

# --- Permanent Database Logic ---
DB_FILE = "tailor_data.csv"

def load_data():
    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    return pd.DataFrame()

def save_to_file(new_record):
    df = load_data()
    updated_df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    updated_df.to_csv(DB_FILE, index=False)

st.title("✂️ She's Style Tailors - POS System")

# --- 🔍 SEARCH SECTION ---
st.header("🔍 Search Customer")
search_query = st.text_input("Naam ya Phone Number likhen:")
db = load_data()

if search_query and not db.empty:
    results = db[db['Name'].astype(str).str.contains(search_query, case=False, na=False) | 
                db['Phone'].astype(str).str.contains(search_query, na=False)]
    if not results.empty:
        st.success(f"✅ {len(results)} Record mil gaya!")
        st.dataframe(results)
st.divider()

# --- FORM SECTION ---
st.header("👤 Customer & Order")
c1, c2, c3 = st.columns(3)
with c1:
    name = st.text_input("Customer Name")
with c2:
    phone = st.text_input("Phone Number")
with c3:
    d_date = st.date_input("Delivery Date", datetime.now() + timedelta(days=7))

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

st.header("👖 Shalwar Details")
s1, s2, s3, s4 = st.columns(4)
with s1:
    sd = st.text_input("Shalwar Design")
with s2:
    sl = st.number_input("Shalwar Lambai", value=36.0, step=0.5)
with s3:
    sw = st.number_input("Shalwar Loosing", value=16.0, step=0.5)
with s4:
    sp = st.number_input("Paicha", value=7.5, step=0.5)

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

# --- ACTION BUTTON ---
if st.button("💾 SAVE & GENERATE RECEIPT", use_container_width=True):
    if name:
        # 1. Computer mein save karna
        record = {
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Name": name, "Phone": phone, "Delivery": d_date.strftime("%Y-%m-%d"),
            "L": l, "S": s, "C": c, "K": k, "H": h, "Chak": chak, 
            "Daman": daman, "Astin": astin, "AH": armh, "DanA": dana, 
            "GalaF": gf, "GalaB": gb, "ShalwarD": sd, "ShalwarL": sl, 
            "ShalwarLoos": sw, "Paicha": sp, "Total": total, "Adv": adv, 
            "Bal": bal, "Note": note
        }
        save_to_file(record)
        st.success(f"✅ {name} ka record Computer mein save ho gaya!")
        
        # 2. Raseed (Receipt) Screen par dikhana
        st.markdown(f"""
        <div style="background-color: white; color: black; padding: 20px; font-family: 'Courier New', Courier, monospace; border: 2px solid black; width: 320px; margin: auto; line-height: 1.2;">
            <h2 style="text-align: center; margin: 0;">SHE'S STYLE</h2>
            <p style="text-align: center; margin: 0; font-size: 12px;">TAILORS - QUETTA</p>
            <hr style="border-top: 2px solid black;">
            <p><b>NAME:</b> {name.upper()}</p>
            <p><b>DATE:</b> {datetime.now().strftime("%d/%m/%Y")}</p>
            <p style="background-color: #eee; padding: 5px;"><b>DELIVERY: {d_date.strftime("%d/%m/%Y")}</b></p>
            <hr style="border-top: 1px dashed black;">
            <p><b>KAMEEZ:</b> {l} | {s} | {c} | {k}</p>
            <p>H:{h} | Ch:{chak} | D:{daman} | Ast:{astin}</p>
            <p>Gala: {gf} / {gb}</p>
            <hr style="border-top: 1px dashed black;">
            <p><b>SHALWAR:</b> {sd}</p>
            <p>L:{sl} | Loos:{sw} | P:{sp}</p>
            <hr style="border-top: 2px solid black;">
            <p>TOTAL: Rs. {total}</p>
            <p>ADVANCE: Rs. {adv}</p>
            <p style="font-size: 18px;"><b>BALANCE: Rs. {bal}</b></p>
            <hr style="border-top: 1px dashed black;">
            <p style="font-size: 12px; text-align: center;">{note}</p>
            <p style="text-align: center; font-size: 14px; margin-top: 10px;">THANK YOU!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 MacBook par Print ke liye: **Command + P** dabayen.")
        st.balloons()
    else:
        st.error("Pehle Name likhen!")

st.divider()
# Purana sara data nichay table mein nazar ayega
st.header("📊 History")
st.dataframe(load_data())
