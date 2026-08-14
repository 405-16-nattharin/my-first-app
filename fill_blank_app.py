import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. ปุ่มเริ่มเล่นเกม (เปลี่ยน game_id เพื่อเคลียร์กล่องข้อความทันที)
if st.button("🎮 เริ่มเล่นเกม"):
    st.session_state.update(
        {"g_id": time.time(), "start": time.time(), "end": False}
    )
    st.rerun()

# 2. นับถอยหลัง และรับคำตอบ (ใช้ g_id ใน key เพื่อให้กล่องว่างเมื่อเริ่มใหม่)
g_id = st.session_state.get("g_id", 0)
if "start" in st.session_state and not st.session_state.get("end", False):
    left = int(30 - (time.time() - st.session_state.start))
    if left > 0:
        st.error(f"⏳ เหลือเวลา: {left} วินาที")
    else:
        st.session_state.end = True

st.divider()

# โจทย์และคำตอบถูกต้อง
questions = [
    ("ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎", "apple"),
    ("ข้อ 2: Cats love to eat `f _ s h`. 🐟", "fish"),
    # ✏️ เพิ่มข้อ 3, 4 ต่อตรงนี้ได้เลย เช่น: ("ข้อ 3: ...", "answer")
]

answers = [
    st.text_input(q, key=f"q_{i}_{g_id}") for i, (q, _) in enumerate(questions)
]

# 3. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("end", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.end = True
        st.rerun()
    time.sleep(1)
    st.rerun()


# 4. MessageBox ป๊อปอัปสรุปผล
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result():
    st.balloons()
    score = sum(
        1
        for a, (_, ans) in zip(answers, questions)
        if a.strip().lower() == ans
    )

    for i, (a, (_, ans)) in enumerate(zip(answers, questions), 1):
        if a.strip().lower() == ans:
            st.success(f"✅ ข้อ {i}: ถูกต้อง")
        else:
            st.error(f"❌ ข้อ {i}: ยังไม่ถูกต้อง (คุณตอบ '{a}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")
    st.success("🎉 You win!") if score == len(
        questions
    ) else st.error("💀 You lose!")


if st.session_state.get("end", False):
    show_result()
