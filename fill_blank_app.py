import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")


# 📌 ฟังก์ชันสำหรับเคลียร์ค่าในกล่องข้อความและรีเซ็ตเกมเมื่อกดปุ่ม "เริ่มเล่นเกม"
def reset_game():
    # 🧹 ลบค่าคำตอบเก่าออกจาก session_state
    if "q1" in st.session_state:
        del st.session_state["q1"]
    if "q2" in st.session_state:
        del st.session_state["q2"]

    # ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่ม del st.session_state["q3"] และ q4 ตรงนี้

    # ⏱️ ตั้งค่าเวลาเริ่มใหม่ และปิดป๊อปอัป
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox แสดงผลลัพธ์แบบป๊อปอัป
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
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


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม (ผูกฟังก์ชัน reset_game ผ่าน on_click)
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎", key="q1"
)
ans2 = st.text_input("ข้อ 2: Cats love to eat `f _ s h`. 🐟", key="q2")

# ----------------------------------------------------
# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มโจทย์ข้อ 3 และ ข้อ 4 ตรงนี้
# ----------------------------------------------------


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง MessageBox เมื่อหมดเวลาหรือกดส่งคำตอบ
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2)
