import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. ปุ่มเริ่มเล่นเกม (เคลียร์ค่าทั้งหมดและรีเซ็ตสถานะเกม)
if st.button("🎮 เริ่มเล่นเกม"):
    st.session_state.clear()  # ล้างค่าในความจำทั้งหมด
    st.session_state.start = time.time()  # เริ่มนับเวลา
    st.session_state.is_ended = False  # สั่งปิดหน้าสรุปผลลัพธ์
    st.rerun()

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state:
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0 and not st.session_state.get("is_ended", False):
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.warning("⏰ หมดเวลาทำข้อสอบแล้ว!")

st.divider()

# 3. ช่องรับคำตอบ (เห็นโจทย์ทันที)
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

    # ถ้ายังมีเวลา และยังไม่ได้จบเกม -> แสดงปุ่มส่งคำตอบ
    if time_left > 0 and not st.session_state.get("is_ended", False):
        if st.button("📥 ส่งคำตอบ"):
            st.session_state.is_ended = True  # จบเกมทันที
            st.rerun()

        time.sleep(1)
        st.rerun()

    # เมื่อหมดเวลา หรือ กดส่งคำตอบแล้ว (is_ended == True)
    elif time_left <= 0 or st.session_state.get("is_ended", False):
        # บันทึกสถานะว่าเกมจบแล้ว
        st.session_state.is_ended = True

        # 🎈 ปล่อยลูกโป่ง
        st.balloons()

        score = 0
        u_ans1 = st.session_state.get("q1", "").strip().lower()
        u_ans2 = st.session_state.get("q2", "").strip().lower()

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

        # 🎯 เช็กว่าได้คะแนนเต็มหรือไม่ (หากเพิ่มเป็น 4 ข้ออย่าลืมแก้เลข 2 เป็น 4)
        if score == 2:
            st.success("🎉 You win!")
        else:
            st.error("💀 You lose!")
