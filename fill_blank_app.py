import streamlit as st

# 1. หัวข้อเกมจัดกึ่งกลาง
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>✏️ เกมเติมคำศัพท์ภาษาอังกฤษ 🧩</h1>", unsafe_allow_html=True)
st.write("ให้นักเรียนเติมตัวอักษรหรือคำศัพท์ที่ขาดหายไปในประโยคให้ถูกต้อง")

st.divider()

# 2. แสดงโจทย์ประโยคภาษาอังกฤษ
st.subheader("โจทย์ข้อที่ 1:")
st.markdown("### An **`a _ _ l e`** a day keeps the doctor away. 🍎")

# 3. ช่องรับคำตอบข้อความจากผู้ใช้
user_answer = st.text_input("พิมพ์คำศัพท์ภาษาอังกฤษแบบเต็มคำที่ถูกต้อง:")

# 4. ปุ่มตรวจคำตอบและการเช็กเงื่อนไข If-Elif-Else
if st.button("ส่งคำตอบ 🎯"):
    # แปลงข้อความที่พิมพ์เป็นตัวพิมพ์เล็ก และตัดสเปซหัว-ท้ายออก
    clean_answer = user_answer.strip().lower()
    
    if clean_answer == "apple":
        st.success("🎉 ถูกต้องแล้วครับ! คำตอบคือ 'apple' (แอปเปิล)")
        st.balloons()
    elif clean_answer == "":
        st.warning("⚠️ โปรดพิมพ์คำตอบในช่องก่อนกดส่งนะครับ")
    else:
        st.error(f"❌ ยังไม่ถูกต้องครับ! คุณตอบว่า '{user_answer}' ลองใหม่อีกครั้งนะ")
