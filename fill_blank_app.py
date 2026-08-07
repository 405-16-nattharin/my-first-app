import time
import streamlit as st

# 1. บันทึกเวลาเริ่มเล่นเกมไว้ใน session_state
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# 2. หัวข้อเกมจัดกึ่งกลาง
st.markdown(
    "<h1 style='text-align: center; color: #1E88E5;'>✏️ เกมเติมคำศัพท์ภาษาอังกฤษ 🧩</h1>",
    unsafe_allow_html=True,
)
st.write("ให้นักเรียนสลับ Tab ด้านล่างเพื่อทำทีละข้อ")

st.divider()

# 3. สร้าง Tabs แยกข้อ 1 และ ข้อ 2 ออกจากกัน
tab1, tab2 = st.tabs(["📌 ข้อที่ 1 (🍎)", "📌 ข้อที่ 2 (🐟)"])

# ==================== TAB 1: ข้อที่ 1 ====================
with tab1:
    st.subheader("ข้อที่ 1 🍎")
    st.markdown("ประโยค: **An `a _ _ l e` a day keeps the doctor away.**")

    ans1 = st.text_input("พิมพ์คำศัพท์ข้อที่ 1:", key="q1")

    if st.button("ตรวจคำตอบข้อ 1 🎯"):
        elapsed = round(time.time() - st.session_state.start_time, 2)
        clean_ans1 = ans1.strip().lower()

        if clean_ans1 == "apple":
            st.success(
                f"🎉 ถูกต้องแล้วครับ! คำตอบคือ 'apple' (แอปเปิล) — ⏱️ ใช้เวลา {elapsed} วินาที"
            )
            st.balloons()
        elif clean_ans1 == "":
            st.warning("⚠️ โปรดพิมพ์คำตอบข้อที่ 1 ก่อนกดส่งนะครับ")
        else:
            st.error(
                f"❌ ยังไม่ถูกต้องครับ! คุณตอบว่า '{ans1}' ลองใหม่อีกครั้งนะ — ⏱️ ใช้เวลา {elapsed} วินาที"
            )

# ==================== TAB 2: ข้อที่ 2 ====================
with tab2:
    st.subheader("ข้อที่ 2 🐟")
    st.markdown("ประโยค: **Cats love to eat `f _ s h`.**")

    ans2 = st.text_input("พิมพ์คำศัพท์ข้อที่ 2:", key="q2")

    if st.button("ตรวจคำตอบข้อ 2 🎯"):
        elapsed = round(time.time() - st.session_state.start_time, 2)
        clean_ans2 = ans2.strip().lower()

        if clean_ans2 == "fish":
            st.success(
                f"🎉 ถูกต้องแล้วครับ! คำตอบคือ 'fish' (ปลา) — ⏱️ ใช้เวลา {elapsed} วินาที"
            )
            st.snow()
        elif clean_ans2 == "":
            st.warning("⚠️ โปรดพิมพ์คำตอบข้อที่ 2 ก่อนกดส่งนะครับ")
        else:
            st.error(
                f"❌ ยังไม่ถูกต้องครับ! คุณตอบว่า '{ans2}' ลองใหม่อีกครั้งนะ — ⏱️ ใช้เวลา {elapsed} วินาที"
            )

# ==================== ปุ่มรีเซ็ตเวลา ====================
st.divider()
if st.button("🔄 เริ่มจับเวลาใหม่"):
    st.session_state.start_time = time.time()
    st.rerun()
