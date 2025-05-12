import streamlit as st

st.title("Chào mừng đến với Streamlit Web App!")
name = st.text_input("Nhập tên của bạn:")
if name:
    st.write(f"Xin chào, {name}!")
