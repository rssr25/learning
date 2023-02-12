##### CACHE mechanism crucial for optimized performance
import streamlit as st
import time

@st.cache_data
def printer():
    time.sleep(3)
    return "Message"

st.write(printer())