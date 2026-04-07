import streamlit as st
import pandas as pd
from datetime import datetime

# --- Shop ka Naam ---
shop_name = "She's Style Tailors"
st.set_page_config(page_title=shop_name, layout="wide")

# --- Data Storage (Temporary Session) ---
if 'orders' not in st.session_state:
    st.session_state.orders = []

st.title(f"✂️ {shop_name}: Digital Register")

# --- Customer Information ---
st.header("📋 New Order")
col_info1, col_info2 = st.columns(2)
with col_info1:
    name = st.text_input("Customer ka Naam")
with col_info2:
    phone = st.text_input("Phone Number")

st.divider()

# --- Measurements ---
st.subheader("📏 Measurements")
m1, m2, m3 = st.columns(3)

with m1:
    lambai = st.number_input("Kameez Lambai", value=38.0)
    chest = st.number_input("Chest (Seena)", value=34.0)
    shoulder = st.number_input("Shoulder (Tera)", value=14.0)
    kamar = st.number_input("Kamar", value=32.0)

with m2:
    hip = st.number_input("Hip", value=36.0)
    chaak = st.number_input("Chaak", value=11.0)
    daman = st.number_input("Daman", value=22.0)
    gala = st.text_input("Gala", "6x6")

with m3:
    astin = st.number_input("Astin Lambai", value=20.0)
    armhole = st.number_input("Armhole", value=8.5)
    shalwar = st.number_input("Shalwar Lambai", value=38.0)
    paicha = st.number_input("Paicha", value=6.5)

loosing = st.number_input("Loosing (Shalwar/Gher)", value=2.0)
note = st.text_area("📝 Extra Design Details (Lace, Piping, etc.)")

# --- Buttons: Save & Download ---
c1, c2 = st.columns(2)

with c1:
    if st.button("➕ List Mein Shamil Karen"):
        if name:
            # Data ko ek dictionary mein save karna
            new_order = {
                "Date": datetime.now().strftime("%d-%m-%Y"),
                "Name": name,
                "Phone": phone,
                "Lambai": lambai,
                "Chest": chest,
                "Shoulder": shoulder,
                "Kamar": kamar,
                "Hip": hip,
                "Chaak": chaak,
                "Daman": daman,
                "Gala": gala,
                "Astin": astin,
                "Armhole": armhole,
                "Shalwar": shalwar,
                "Paicha": paicha,
                "Loosing": loosing,
                "Notes": note
            }
            st.session_state.orders.append(new_order)
            st.success(f"✅ {name} ka naap list mein shamil ho gaya!")
            st.balloons()
        else:
            st.error("Meharbani karke Naam likhen!")

# --- Table Display & Download ---
if st.session_state.orders:
    st.divider()
    st.subheader("📑 Aaj ki Order List")
    df = pd.DataFrame(st.session_state.orders)
    st.dataframe(df) # Table dikhane ke liye

    # Excel/CSV Download Button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Poori List Download Karen (Excel/CSV)",
        data=csv,
        file_name=f"Shes_Style_Orders_{datetime.now().strftime('%d_%m')}.csv",
        mime='text/csv',
    )

    if st.button("🗑️ List Khali Karen (Clear All)"):
        st.session_state.orders = []
        st.experimental_rerun()