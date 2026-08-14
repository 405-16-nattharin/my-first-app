import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. ปุ่มเริ่มเล่นเกม
if st.button("🎮 เริ่มเล่นเกม"):
    st.session_state.game_id = time.time()  # สุ่ม key ใหม่เพื่อเคลียร์กล่องข้อความ
    st.session_state.start = time.time()  # เริ่มนับเวลา
    st.session_state.is_ended = False  # ซ่อนส่วนตรวจคำตอบ
    st.rerun()

# ตั้งค่าเริ่มต้นเมื่อเปิดแอปครั้งแรกสุด
if "game_id" not in st.session_state:
    st.session_state.game_id = 0

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        # ถ้าเวลาหมด ให้เปลี่ยนสถานะเป็นจบเกม
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ ( dynamic key เคลียร์กล่องสะอาดแน่นอน)
q1_key = f"q1_{st.session_state.game_id}"
q2_key = f"q2_{st.session_state.game_id}"

ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎", key=q1_key
)
ans2 = st.text_input("ข้อ 2: Cats love to eat `f _ s h`. 🐟", key=q2_key)

# ----------------------------------------------------
# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มโจทย์ข้อ 3 และ ข้อ 4 ตรงนี้
# ----------------------------------------------------


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True  # สั่งให้จบเกมและแสดงผลลัพธ์
        st.rerun()

    time.sleep(1)
    st.rerun()

# ----------------------------------------------------
# 5. ส่วนตรวจคำตอบ (จะทำงานเมื่อ st.session_state.is_ended == True เท่านั้น)
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
