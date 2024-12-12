python
import streamlit as st

st.title("🌌 Universe Generator")

world_name = st.text_input("Name your world:", "Mysteria")
technology_level = st.slider("Technology Level", 0, 10, 5)
magic_level = st.slider("Magic Level", 0, 10, 5)

if st.button("Generate"):
    st.success(f"Welcome to {world_name}!")
    st.write(f"Technology Level: {'⚙️' * (technology_level // 2)}")
    st.write(f"Magic Level: {'✨' * (magic_level // 2)}")
