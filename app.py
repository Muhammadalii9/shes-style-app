import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime, timedelta

# --- Page Setup ---
st.set_page_config(page_title="She's Style Tailors", layout="wide")

st.title("✂️ She's Style Tailors - Digital Register")

# --- Google Sheets Connection ---
conn = st.connection("gsheets", type=GSheetsConnection)

# --- Form Inputs ---
with st.form("tailor_form", clear_on_submit=True):
    st.header("👤 Customer & Delivery")
    col_inf1, col_inf2, col_inf3 = st.columns(3)
    with col_inf1:
        name = st.text_input("Customer Name")
    with col_inf2:
        phone = st.text_input("Phone Number")
    with col_inf3:
        d_date = st.date_input("Delivery Date", datetime.now() + timedelta(days=7))
    
    st.divider()
    
    # --- Measurements Section ---
    st.header("📏 Measurements (Inches)")
    st.info("💡 Tip: '+' dabane se poora 1 inch barhay ga.")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        # step=1.0 se ab + dabane par poora 1 inch barhay ga
        l = st.number_input("Lambai (Length)", value=38.0, step=1.0)
        s = st.number_input("Shoulder (Tera)", value=14.0, step=1.0)
    with c2:
        c = st.number_input("Chest (Seena)", value=34.0, step=1.0)
        k = st.number_input("Kamar (Waist)", value=32.0, step=1.0)
    with c3:
        h = st.number_input("Hip", value=36.0, step=1.0)
        d = st.number_input("Daman", value=22.0, step=1.0)
    with c4:
        s_l = st.number_input("Shalwar L", value=38.0, step=1.0)
        p = st.number_input("Paicha", value=6.5, step=0.5) # Paicha aksar aadha inch hota hai

    st.divider()
    
    # --- Gala & Design ---
    st.header("🎨 Design Details")
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        gala_front = st.text_input("Gala Front (e.g. V-Shape 6x7)", "Round")
    with g_col2:
        gala_back = st.text_input("Gala Back", "Normal")

    st.divider()
    
    # --- Billing ---
    st.header("💰 Billing")
    p1, p2 = st.columns(2)
    with p1:
        total = st.number_input("Total Bill", value=1500, step=50.0)
    with p2:
        adv = st.number_input("Advance Payment", value=500, step=50.0)
    
    note = st.text_area("Extra Notes (Lace, Piping, Karigar Instructions)")
    
    submit = st.form_submit_button("✅ SAVE TO GOOGLE SHEET & GENERATE RECEIPT")

if submit:
    if name:
        # Naya data tayyar karna
        new_row = {
            "Date": [datetime.now().strftime("%d-%m-%Y")],
            "Name": [name],
            "Phone": [phone],
            "L": [l], "S": [s], "C": [c], "K": [k], "H": [h], "D": [d],
            "Gala_F": [gala_front], "Gala_B": [gala_back], "ShL": [s_l],
            "Total": [total], "Advance": [adv], "Balance": [total-adv],
            "Note": [note]
        }
        df_new = pd.DataFrame(new_row)
        
        try:
            # Google Sheet mein update karna
            sheet_url = "https://docs.google.com/spreadsheets/d/19hHI5vz6-LhnP_egTPGaRjmp89zelGEWPqcCZ0xrk7o/edit?usp=sharing"
            existing_data = conn.read(spreadsheet=sheet_url)
            updated_df = pd.concat([existing_data, df_new], ignore_index=True)
            conn.update(spreadsheet=sheet_url, data=updated_df)
            
            st.success(f"Zabardast Master Alii! {name} ka record save ho gaya.")
            st.balloons()
            
            # Printer Optimized Receipt
            st.markdown("---")
            st.subheader("🧾 Receipt for Bluetooth Printer")
            receipt_text = f"""
            SHE'S STYLE TAILORS
            ------------------
            Cust: {name}
            Date: {datetime.now().strftime("%d-%m-%Y")}
            ------------------
            L: {l} | S: {s} | C: {c}
            K: {k} | H: {h} | D: {d}
            ShL: {s_l} | P: {p}
            ------------------
            GALA F: {gala_front}
            GALA B: {gala_back}
            ------------------
            TOTAL: {total}
            ADV: {adv}
            BAL: {total-adv}
            ------------------
            Note: {note}
            """
            st.code(receipt_text)
            st.info("Iski screenshot len aur iTech printer se print nikal len.")
            
        except Exception as e:
            st.error("Sheet save nahi ho saki. Check karen ke internet on hai?")
    else:
        st.error("Customer ka naam likhna lazmi hai!")
