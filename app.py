import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

# --- Initialize Database (Session State) ---
# Ye code aapka data temporary save rakhega jab tak app chal rahi hai
if 'tailor_db' not in st.session_state:
    st.session_state.tail_db = []

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

# --- Shalwar Details ---
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

# --- Action Buttons ---
col_save, col_print = st.columns(2)

with col_save:
    if st.button("💾 SAVE RECORD", use_container_width=True):
        if name:
            new_record = {
                "Date": datetime.now().strftime("%d/%m/%Y"),
                "Name": name,
                "Phone": phone,
                "Delivery": d_date.strftime("%d/%m/%Y"),
                "Lambai": l, "Shoulder": s, "Chest": c, "Kamar": k,
                "Hip": h, "Chak": chak, "Daman": daman, "Astin": astin,
                "ArmHole": armh, "DanAstin": dana, "GalaF": gf, "GalaB": gb,
                "ShalwarDesign": sd, "ShalwarL": sl, "ShalwarLoos": sw, "Paicha": sp,
                "Total": total, "Advance": adv, "Balance": bal, "Note": note
            }
            st.session_state.tail_db.append(new_record)
            st.success(f"Record for {name} saved successfully!")
        else:
            st.error("Please enter a name first!")

with col_print:
    if st.button("🖨️ PREPARE RECEIPT", use_container_width=True):
        if name:
            # Receipt Display (Same as before)
            st.markdown(f"""
            <div style="background-color: white; color: black; padding: 20px; font-family: 'Courier New', Courier, monospace; border: 1px solid #ccc; width: 300px; margin: auto;">
                <h3 style="text-align: center;">SHE'S STYLE TAILORS</h3>
                <hr>
                <p>NAME: {name.upper()}</p>
                <p>DELIVERY: {d_date.strftime("%d/%m/%Y")}</p>
                <hr>
                <p>TOTAL: Rs. {total} | BAL: Rs. {bal}</p>
                <hr>
                <p style="font-size: 10px; text-align: center;">Record Saved in Database</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Pehle Name likhen!")

st.divider()

# --- Database View & Download ---
st.header("📊 Business Records")
if st.session_state.tail_db:
    df = pd.DataFrame(st.session_state.tail_db)
    st.dataframe(df) # Screen par table dikhayega
    
    # Download Button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 DOWNLOAD EXCEL (CSV) FILE",
        data=csv,
        file_name=f"Tailor_Records_{datetime.now().strftime('%Y%m%d')}.csv",
        mime='text/csv',
        use_container_width=True
    )
else:
    st.info("Abhi tak koi record save nahi hua.")
