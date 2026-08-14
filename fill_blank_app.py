import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. ปุ่มเริ่มเล่นเกม (ล้างความจำทั้งหมด แล้วสั่งรันบรรทัดแรกใหม่ทันที)
if st.button("🎮 เริ่มเล่นเกม"):
    st.session_state.clear()  # ล้างค่าในความจำทั้งหมด
    st.session_state.start = time.time()  # บันทึกเวลาเริ่มเล่นรอบใหม่
    st.rerun()  # ⚡ สั่งให้กลับไปรันบรรทัดแรกใหม่ทันที!

# 2. แถบแสดงเวลานับถอยหลัง (แสดงเฉพาะเมื่อกดเริ่มเล่นเกมแล้ว)
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (หน้าจอจะถูกล้างใหม่ใสสะอาด)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎", key="q1"
)
ans2 = st.text_input("ข้อ 2: Cats love to eat `f _ s h`. 🐟", key="q2")

# ----------------------------------------------------
# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มโจทย์ข้อ 3 และ ข้อ 4 ตรงนี้
# ----------------------------------------------------


# 4. ปุ่มส่งคำตอบ (แสดงเฉพาะช่วงเวลาที่กำลังเล่นอยู่)
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True  # สั่งจบเกมเพื่อแสดงผลลัพธ์
        st.rerun()

    time.sleep(1)
    st.rerun()

# ----------------------------------------------------
# 5. ส่วนตรวจคำตอบ (จะไม่รันเลย จนกว่าจะกดส่งคำตอบหรือเวลาหมด)
# ----------------------------------------------------
if st.session_state.get("is_ended", False):
    st.warning("⏰ หมดเวลาทำข้อสอบแล้ว!")
    st.balloons()

    score = 0
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()

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
