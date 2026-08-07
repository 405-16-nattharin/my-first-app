import streamlit as st

# 1. หัวข้อเกมจัดกึ่งกลาง
st.markdown("✏️ เกมเติมคำศัพท์ภาษาอังกฤษ (2 ข้อ) 🧩")
st.write("ให้นักเรียนเติมคำศัพท์ภาษาอังกฤษที่ขาดหายไปในประโยคให้ถูกต้อง")

st.divider()

# ==================== ข้อที่ 1 ====================
st.subheader("ข้อที่ 1 🍎")
st.markdown("ประโยค: **An `a _ _ l e` a day keeps the doctor away.**")

# ช่องรับคำตอบข้อที่ 1
ans1 = st.text_input("พิมพ์คำศัพท์ข้อที่ 1:", key="q1")

# ปุ่มตรวจคำตอบข้อที่ 1
if st.button("ตรวจคำตอบข้อ 1 🎯"):
    clean_ans1 = ans1.strip().lower()
    
    if clean_ans1 == "apple":
        st.success("🎉 ถูกต้องแล้วครับ! คำตอบคือ 'apple' (แอปเปิล)")
        st.balloons()
    elif clean_ans1 == "":
        st.warning("⚠️ โปรดพิมพ์คำตอบข้อที่ 1 ก่อนกดส่งนะครับ")
    else:
        st.error(f"❌ ยังไม่ถูกต้องครับ! คุณตอบว่า '{ans1}' ลองใหม่อีกครั้งนะ")

st.divider()

# ==================== ข้อที่ 2 ====================
st.subheader("ข้อที่ 2 🐟")
st.markdown("ประโยค: **Cats love to eat `f _ s h`.**")

# ช่องรับคำตอบข้อที่ 2
ans2 = st.text_input("พิมพ์คำศัพท์ข้อที่ 2:", key="q2")

# ปุ่มตรวจคำตอบข้อที่ 2
if st.button("ตรวจคำตอบข้อ 2 🎯"):
    clean_ans2 = ans2.strip().lower()
    
    if clean_ans2 == "fish":
        st.success("🎉 ถูกต้องแล้วครับ! คำตอบคือ 'fish' (ปลา)")
        st.snow()  # เปลี่ยนเอฟเฟกต์เป็นหิมะตก
    elif clean_ans2 == "":
        st.warning("⚠️ โปรดพิมพ์คำตอบข้อที่ 2 ก่อนกดส่งนะครับ")
    else:
        st.error(f"❌ ยังไม่ถูกต้องครับ! คุณตอบว่า '{ans2}' ลองใหม่อีกครั้งนะ")
