import streamlit as st
from utils import predict_phishing

st.title("Phishing Message Detector")

msg = st.text_area("Enter Message or Email")

if st.button("Check"):
    if msg:
        result = predict_phishing(msg)
        st.success(result)
    else:
        st.warning("Enter text first")