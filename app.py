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

# --- Naya Delete Function ---
def delete_record(index_to_delete):
    df = load_data()
    if not df.empty:
        # Index ke mutabiq row urana
        df = df.drop(index_to_delete)
        df.to_csv(DB_FILE, index=False)
        return True
    return False

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

# --- FORM SECTION (Measurements & Billing) ---
# (Yahan aapka puraana form wese hi rahega...)
# [Baki form code short kiya hai taake delete par tawajjo rahe]
st.header("👤 Customer & Order")
c1, c2, c3 = st.columns(3)
with c1: name = st.text_input("Customer Name")
with c2: phone = st.text_input("Phone Number")
with c3: d_date = st.date_input("Delivery Date", datetime.now() + timedelta(days=7))

# Measurements... (Aap apna mukammal code use karen)
# ...

if st.button("💾 SAVE & GENERATE RECEIPT", use_container_width=True):
    if name:
        record = {
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Name": name, "Phone": phone, "Delivery": d_date.strftime("%Y-%m-%d"),
            "Total": 1000, "Adv": 0, "Bal": 1000 # Ye sirf misal hai
        }
        save_to_file(record)
        st.success("Record Saved!")
    else:
        st.error("Name likhen!")

st.divider()

# --- 📊 HISTORY & DELETE SECTION ---
st.header("📊 History & Record Management")
current_db = load_data()

if not current_db.empty:
    st.write("Niche di gayi table mein se **Index Number** dekh kar delete karen:")
    st.dataframe(current_db)
    
    # Delete Box
    col_del1, col_del2 = st.columns([1, 3])
    with col_del1:
        row_index = st.number_input("Delete karne ke liye Index No likhen:", min_value=0, max_value=len(current_db)-1, step=1)
    with col_del2:
        st.write(" ") # Space
        st.write(" ") # Space
        if st.button(f"🗑️ Delete Record #{row_index}", type="secondary"):
            if delete_record(row_index):
                st.warning(f"Record #{row_index} delete ho gaya!")
                st.rerun() # Screen ko refresh karne ke liye
else:
    st.info("Abhi koi record nahi hai.")
