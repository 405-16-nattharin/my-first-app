import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. ปุ่มเริ่มเล่นเกม (ล้างทุกอย่างให้เหมือนเปิดแอปใหม่)
if st.button("🎮 เริ่มเล่นเกม"):
    st.session_state.clear()  # ล้าง session ทั้งหมด
    st.session_state.start = time.time()  # บันทึกเวลาเริ่ม
    st.session_state.is_ended = False  # กำหนดให้ยังไม่จบเกม
    st.session_state["q1"] = ""  # เคลียร์กล่องข้อความ 1
    st.session_state["q2"] = ""  # เคลียร์กล่องข้อความ 2
    st.rerun()

# 2. แถบแสดงเวลานับถอยหลัง (แสดงเฉพาะตอนกำลังเล่นอยู่)
if "start" in st.session_state:
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0 and not st.session_state.get("is_ended", False):
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")

st.divider()

# 3. ช่องรับคำตอบ
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎", key="q1"
)
ans2 = st.text_input("ข้อ 2: Cats love to eat `f _ s h`. 🐟", key="q2")

# ----------------------------------------------------
# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มโจทย์ข้อ 3 และ ข้อ 4 ตรงนี้
# ----------------------------------------------------


# 4. ปุ่มส่งคำตอบ และระบบตรวจคะแนน
if "start" in st.session_state:
    time_left = int(30 - (time.time() - st.session_state.start))

    # --- กรณีที่ 1: กำลังเล่นเกมอยู่ ---
    if time_left > 0 and not st.session_state.get("is_ended", False):
        if st.button("📥 ส่งคำตอบ"):
            # บันทึกคำตอบสุดท้ายไว้ก่อนเคลียร์
            st.session_state.final_q1 = ans1
            st.session_state.final_q2 = ans2
            st.session_state.is_ended = True  # จบเกม
            st.rerun()

        time.sleep(1)
        st.rerun()

    # --- กรณีที่ 2: หมดเวลา หรือ กดส่งคำตอบแล้ว (ตรวจคำตอบและแสดงผล) ---
    elif time_left <= 0 or st.session_state.get("is_ended", False):
        # ถ้าเป็นการหมดเวลาโดยไม่ได้กดปุ่มส่ง ให้ดึงค่าปัจจุบันมาบันทึกไว้
        if "final_q1" not in st.session_state:
            st.session_state.final_q1 = ans1
            st.session_state.final_q2 = ans2

        st.session_state.is_ended = True  # ยืนยันสถานะจบเกม
        st.warning("⏰ หมดเวลาทำข้อสอบแล้ว!")
        st.balloons()

        score = 0
        u_ans1 = st.session_state.final_q1.strip().lower()
        u_ans2 = st.session_state.final_q2.strip().lower()

        # ตรวจข้อ 1
        if u_ans1 == "apple":
            st.success("✅ ข้อ 1: ถูกต้อง")
            score += 1
        else:
            st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

        # ตรวจข้อ 2
        if u_ans2 == "fish":
            st.success("✅ ข้อ 2: ถูกต้อง")
            score += 1
        else:
            st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

        # ----------------------------------------------------
        # ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มการตรวจข้อ 3 และ ข้อ 4 ตรงนี้
        # ----------------------------------------------------

        st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

        if score == 2:
            st.success("🎉 You win!")
        else:
            st.error("💀 You lose!")
