import streamlit as st

# --- Shop ka Naam ---
shop_name = "She's Style Tailors"

st.set_page_config(page_title=shop_name, layout="wide")
st.title(f"✂️ {shop_name}: Booking & Measurements")

# --- Form Shuru ---
st.header("📋 Customer Information")

col_info1, col_info2 = st.columns(2)
with col_info1:
    name = st.text_input("Customer ka Naam")
with col_info2:
    phone = st.text_input("Phone Number")

st.divider()

# --- Measurements (Kameez) ---
st.subheader("📏 Kameez aur Astin")
m1, m2, m3 = st.columns(3)

with m1:
    lambai = st.number_input("Kameez ki Lambai", value=38.0)
    shoulder = st.number_input("Shoulder (Tera)", value=14.0)
    chest = st.number_input("Chest (Seena)", value=34.0)
    kamar = st.number_input("Kamar (Waist)", value=32.0)

with m2:
    hip = st.number_input("Hip", value=36.0)
    chaak = st.number_input("Chaak (Armhole se niche)", value=11.0)
    daman = st.number_input("Daman / Ghera", value=22.0)
    gala = st.text_input("Gala (Front/Back)", "6x6")

with m3:
    astin_lambai = st.number_input("Astin ki Lambai", value=20.0)
    arm_hole = st.number_input("Armhole (Golaee)", value=8.5)
    astin_sar = st.number_input("Astin ka Sar", value=3.5)

st.divider()

# --- Bottom (Shalwar) ---
st.subheader("👖 Shalwar / Bottom")
s1, s2, s3 = st.columns(3)
with s1:
    shalwar_lambai = st.number_input("Shalwar ki Lambai", value=38.0)
with s2:
    paicha = st.number_input("Paicha", value=6.5)
with s3:
    # Loosing ab yahan Shalwar ke section mein hai
    loosing = st.number_input("Loosing (Shalwar/Gher)", value=2.0)

st.divider()

description = st.text_area("📝 Extra Instructions (Design/Lace/Piping)")

st.divider()

# --- Print & Save Section ---
if st.button("Generate Print Slip"):
    if name:
        st.success(f"Order Saved for {name}!")
        
        # Print Slip Update
        st.markdown(f"""
        ---
        ### 🧾 {shop_name} - Measurement Slip
        **Customer:** {name} | **Phone:** {phone}
        
        **Kameez Details:**
        * Lambai: {lambai} | Tera: {shoulder} | Chest: {chest} | Kamar: {kamar}
        * Hip: {hip} | Chaak: {chaak} | Daman: {daman} | Gala: {gala}
        
        **Astin Details:**
        * Astin: {astin_lambai} | Armhole: {arm_hole} | Astin Sar: {astin_sar}
        
        **Shalwar Details:**
        * Lambai: {shalwar_lambai} | Paicha: {paicha} | Loosing: {loosing}
        
        **Notes:** {description}
        ---
        """)
    else:
        st.error("Pehle Customer ka Naam likhen!")