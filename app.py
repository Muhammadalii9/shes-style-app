import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

st.title("✂️ She's Style Tailors - Digital Register")

# Data ko temporary yaad rakhne ke liye
if 'temp_data' not in st.session_state:
    st.session_state.temp_data = []

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
    c = st.number_input("Chest", value=20.0, step=1.0)
with k2:
    k = st.number_input("Kamar", value=18.0, step=1.0)
    h = st.number_input("Hip", value=21.0, step=1.0)
    chak = st.number_input("Chak", value=12.0, step=1.0)
with k3:
    daman = st.number_input("Daman", value=22.0, step=1.0)
    astin = st.number_input("Astin", value=20.0, step=1.0)
    armh = st.number_input("Arm Hole", value=9.0, step=0.5)
with k4:
    dana = st.number_input("Dan Astin", value=6.0, step=0.5)
    gf = st.text_input("Gala Front", "7x5")
    gb = st.text_input("Gala Back", "Normal")

st.divider()

# --- 3. Shalwar Ka Nap ---
st.header("👖 Shalwar Ka Nap")
s1, s2, s3 = st.columns(3)
with s1:
    sl = st.number_input("Shalwar Lambai", value=36.0, step=1.0)
with s2:
    sw = st.number_input("Shalwar Chodai", value=16.0, step=1.0)
with s3:
    sp = st.number_input("Paicha", value=7.5, step=0.5)

st.divider()

# --- 4. Billing ---
st.header("💰 Billing")
b1, b2 = st.columns(2)
with b1:
    total = st.number_input("Total Bill", value=1000.0, step=50.0)
with b2:
    adv = st.number_input("Advance Payment", value=500.0, step=50.0)

bal = float(total) - float(adv)
st.metric("Baqi (Balance)", f"{bal}")

note = st.text_area("Extra Notes")

st.divider()

# --- Actions ---
if st.button("✅ GENERATE RECEIPT", use_container_width=True):
    if name:
        # Data ko list mein add karna
        new_entry = {
            "Date": datetime.now().strftime("%d-%m-%Y"),
            "Name": name, "Phone": phone, "L": l, "S": s, "C": c, "K": k, 
            "H": h, "Chak": chak, "D": daman, "Ast": astin, "AH": armh, 
            "DA": dana, "G_F": gf, "G_B": gb, "SL": sl, "SW": sw, "SP": sp,
            "Total": total, "Adv": adv, "Bal": bal, "Note": note
        }
        st.session_state.temp_data.append(new_entry)
        
        st.success(f"{name} ka record ready hai!")
        
        # Receipt for Printer
        st.markdown("### 🧾 RECEIPT FOR iTech PRINTER")
        receipt = f"""
        SHE'S STYLE TAILORS
        ------------------
        Name: {name} | Date: {datetime.now().strftime("%d-%m")}
        ------------------
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
        st.info("Iski screenshot len aur iTech printer se print nikal len.")
        st.balloons()
    else:
        st.error("Pehle Name likhen!")

# --- Permanent Save Section ---
if st.session_state.temp_data:
    st.divider()
    st.subheader("📁 Save to Mobile Memory")
    df = pd.DataFrame(st.session_state.temp_data)
    csv = df.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 DOWNLOAD RECORD FILE (CSV)",
        data=csv,
        file_name=f"Tailor_Records_{datetime.now().strftime('%d_%b')}.csv",
        mime='text/csv',
        use_container_width=True
    )
    st.write("Ye file aap ke mobile ke 'Downloads' folder mein save hogi.")
