import streamlit as st
import pandas as pd
from datetime import datetime

# --- Shop Info ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

# --- Data Store ---
if 'orders' not in st.session_state:
    st.session_state.orders = []

st.title("✂️ She's Style Tailors")

# --- Inputs ---
name = st.text_input("Customer Name")
phone = st.text_input("Phone")

c1, c2 = st.columns(2)
with c1:
    lambai = st.number_input("Lambai", value=38.0)
    chest = st.number_input("Chest", value=34.0)
with c2:
    shoulder = st.number_input("Shoulder", value=14.0)
    paicha = st.number_input("Paicha", value=6.5)

note = st.text_area("Notes")

# --- Save Button ---
if st.button("Add to List"):
    if name:
        new_data = {"Date": datetime.now().strftime("%d-%m"), "Name": name, "Phone": phone, "L": lambai, "C": chest, "S": shoulder, "P": paicha}
        st.session_state.orders.append(new_data)
        st.success("Saved!")
    else:
        st.error("Enter Name")

# --- Display List ---
if st.session_state.orders:
    st.divider()
    df = pd.DataFrame(st.session_state.orders)
    st.table(df) # Table iPad par zyada behtar chalti hai
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download List", data=csv, file_name="orders.csv", mime='text/csv')
