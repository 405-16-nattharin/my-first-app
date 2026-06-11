import streamlit as st

# 1. หัวข้อเว็บ
st.title("ระบบคำนวณดัชนีมวลกาย (BI) 🏋️‍♂️")
st.write("ยินดีต้อนรับเข้าสู่แอปพลิเคชันแรกของพวกเรา ม.4")

# 2. ส่วนรับค่าจากผู้ใช้ (Input)
weight = st.number_input("กรุณากรอกน้ำหนัก (กิโลกรัม):", min_value=1.0, value=50.0)
height_cm = st.number_input("กรุณากรอกส่วนสูง (เซนติเมตร):", min_value=1.0, value=160.0)

# 3. ส่วนคำนวณ (Logic)
height_m = height_cm / 100
bmi = weight / (height_m ** 2)

# 4. ส่วนแสดงผลลัพธ์ (Output)
if st.button("คำนวณค่า BMI"):
    st.write(f"### ค่า BMI ของคุณคือ: {bmi:.2f}")
    
    if bmi < 18.5:
        st.error("น้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
    elif bmi < 23.0:
        st.success("น้ำหนักปกติ (สุขภาพดี)")
    else:
        st.warning("น้ำหนักเกินเกณฑ์")
