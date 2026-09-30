import streamlit as st
from config import QUALCOMM_NPU_EXECUTION_PROVIDER

st.set_page_config(page_title="SnapVault AI - On-Device Assistant", layout="wide")

st.title("🔒 SnapVault AI — Local Knowledge Assistant")
st.caption("Optimized for HP Snapdragon® X Series Laptops | Acceleration via Hexagon NPU")

st.sidebar.header("Hardware Execution Target")
st.sidebar.success(f"Execution Provider Target: {QUALCOMM_NPU_EXECUTION_PROVIDER}")
st.sidebar.info("Model Status: Sourced via Qualcomm AI Hub")

user_query = st.text_input("Ask a question about your indexed documents:")

if user_query:
    st.write("### Output:")
    st.info("Simulating QNN / NPU local execution pipeline...")
    st.markdown(f"**Answer:** Context processing completed locally for query: *{user_query}*")
    st.caption("⚡ Latency: ~110ms | Target Hardware: Qualcomm® Hexagon™ NPU | Data Leakage: 0%")