import streamlit as st

# 1. หัวข้อหน้าเว็บ
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")

# 2. สร้างกล่องรับราคาสินค้า (กำหนดค่าตั้งต้นไว้ที่ 100 บาท)
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0, value=0.0)

# 3. คำนวณภาษี VAT 7% และราคารวมสุทธิ
vat = price * 0.07
total_price = price + vat

# 4. แสดงผลลัพธ์สรุปรายการ
st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"💰 ราคาสุทธิที่ต้องจ่าย: {total_price:.2f} บาท")
