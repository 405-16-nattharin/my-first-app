import streamlit as st

# 1. หัวข้อเกมจัดกึ่งกลาง
st.markdown(
    "<h1 style='text-align: center; color: #1E88E5;'>✏️ เกมเติมคำศัพท์ภาษาอังกฤษ (ตรวจทีเดียว 2 ข้อ) 🧩</h1>",
    unsafe_allow_html=True,
)
st.write("ให้นักเรียนเติมคำศัพท์ภาษาอังกฤษที่ขาดหายไปในประโยคให้ถูกต้องทั้ง 2 ข้อ")

st.divider()

# ==================== แสดงโจทย์และช่องรับคำตอบ ====================
st.subheader("ข้อที่ 1 🍎")
st.markdown("ประโยค: **An `a _ _ l e` a day keeps the doctor away.**")
ans1 = st.text_input("พิมพ์คำศัพท์ข้อที่ 1:", key="q1")

st.write("")  # เว้นบรรทัด

st.subheader("ข้อที่ 2 🐟")
st.markdown("ประโยค: **Cats love to eat `f _ s h`.**")
ans2 = st.text_input("พิมพ์คำศัพท์ข้อที่ 2:", key="q2")

st.divider()

# ==================== ปุ่มตรวจคำตอบรวม (กดทีเดียว) ====================
if st.button("ส่งและตรวจคำตอบทั้งหมด 🎯"):
    # ทำความสะอาดข้อความทั้ง 2 ข้อ
    clean_ans1 = ans1.strip().lower()
    clean_ans2 = ans2.strip().lower()

    # 1. เช็กว่ากรอกข้อมูลครบทุกช่องหรือยัง
    if clean_ans1 == "" or clean_ans2 == "":
        st.warning("⚠️ โปรดกรอกคำตอบให้ครบทั้ง 2 ข้อก่อนกดส่งนะครับ")

    # 2. เช็กว่าถูกทั้งหมด (ถูกข้อ 1 AND ถูกข้อ 2)
    elif clean_ans1 == "apple" and clean_ans2 == "fish":
        st.success("🎉 เก่งมากครับ! คุณตอบถูกต้องทั้งหมดทั้ง 2 ข้อ 🏆")
        st.balloons()

    # 3. เช็กกรณีถูกแค่ข้อแรกข้อเดียว
    elif clean_ans1 == "apple":
        st.info("💡 ข้อ 1 ถูกต้อง (apple) แต่ข้อ 2 ยังไม่ถูก ลองใหม่อีกครั้งนะ!")

    # 4. เช็กกรณีถูกแค่ข้อสองข้อเดียว
    elif clean_ans2 == "fish":
        st.info("💡 ข้อ 2 ถูกต้อง (fish) แต่ข้อ 1 ยังไม่ถูก ลองใหม่อีกครั้งนะ!")

    # 5. กรณีผิดทั้งคู่
    else:
        st.error("❌ ยังไม่ถูกต้องทั้ง 2 ข้อ ลองเช็กตัวอักษรใหม่อีกครั้งนะครับ!")
