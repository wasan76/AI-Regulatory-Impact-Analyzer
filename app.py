
import streamlit as st

st.set_page_config(page_title="AI Regulatory Impact Analyzer")

st.title("AI Regulatory Impact Analyzer")

uploaded_file = st.file_uploader(
    "Upload Regulatory Circular",
    type=["docx"]
)

if uploaded_file:
    st.success("File uploaded successfully.")
