import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. ช่องรับคำตอบ (เห็นโจทย์ทันที)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎", key="q1"
)
ans2 = st.text_input("ข้อ 2: Cats love to eat `f _ s h`. 🐟", key="q2")

# ----------------------------------------------------
# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มโจทย์ข้อ 3 และ ข้อ 4 ตรงนี้
# ----------------------------------------------------


# 2. ปุ่มกดเริ่มจับเวลา
if st.button("🚀 เริ่มจับเวลา (30 วินาที)"):
    st.session_state.start = time.time()

# 3. ระบบจับเวลาและการตรวจคำตอบ
if "start" in st.session_state:
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")

        if st.button("📥 ส่งคำตอบ"):
            st.session_state.start = 0  # บังคับหมดเวลาทันที
            st.rerun()

        time.sleep(1)
        st.rerun()

    else:
        st.warning("⏰ หมดเวลาแล้ว! มาตรวจคำตอบกัน")
        score = 0

        u_ans1 = st.session_state.get("q1", "").strip().lower()
        u_ans2 = st.session_state.get("q2", "").strip().lower()

        # ตรวจข้อ 1
        if u_ans1 == "apple":
            st.success("✅ ข้อ 1: ถูกต้อง (apple)")
            score += 1
        else:
            st.error(f"❌ ข้อ 1: ผิด! คุณตอบ '{u_ans1}' (เฉลย: apple)")

        # ตรวจข้อ 2
        if u_ans2 == "fish":
            st.success("✅ ข้อ 2: ถูกต้อง (fish)")
            score += 1
        else:
            st.error(f"❌ ข้อ 2: ผิด! คุณตอบ '{u_ans2}' (เฉลย: fish)")

        # ----------------------------------------------------
        # ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มการตรวจข้อ 3 และ ข้อ 4 ตรงนี้
        # ----------------------------------------------------

        st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")
