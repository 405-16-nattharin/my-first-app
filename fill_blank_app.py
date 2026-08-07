import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา (30 วินาที)")

# 1. กดปุ่มเริ่มเกม
if st.button("🚀 เริ่มเล่นเกม!"):
    st.session_state.start = time.time()

# 2. เมื่อเกมเริ่มแล้ว ให้แสดงโจทย์
if "start" in st.session_state:
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")

        # โจทย์ 2 ข้อ (ใช้ st.session_state ดึงค่าที่พิมพ์)
        ans1 = st.text_input(
            "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
            key="q1",
        )
        ans2 = st.text_input("ข้อ 2: Cats love to eat `f _ s h`. 🐟", key="q2")

        if st.button("📥 ส่งคำตอบ"):
            st.session_state.start = 0  # บังคับหมดเวลาทันที
            st.rerun()

        # ⚡ เพิ่ม 2 บรรทัดนี้เพื่อสั่งให้หน้ารีเฟรชเวลานับถอยหลังทุก 1 วินาที
        time.sleep(1)
        st.rerun()

    else:
        # 3. เวลาหมด -> คิดคะแนนและบอกข้อที่ผิด
        st.warning("⏰ หมดเวลาแล้ว! มาตรวจคำตอบกัน")
        score = 0

        # ดึงค่าคำตอบจาก key ใน session_state
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

        st.info(f"🏆 ได้คะแนนรวม: {score} / 2 คะแนน")
