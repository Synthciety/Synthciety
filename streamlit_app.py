python
import streamlit as st

st.title("Universe Generator")

name = st.text_input("Enter name:", "Test")
st.write(f"Hello, {name}!")
