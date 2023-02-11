import streamlit as st
input = st.text_input("Enter your name")
s_btn = st.button("Submit")

## Whenever a checkbox is selected, the entire script runs
if s_btn:
    opt = st.checkbox("Want to display your name?")
    if opt:
        print(input)
