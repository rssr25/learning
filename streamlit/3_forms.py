import streamlit as st

st.write("""
# User registration form
---
""")

#way 1 to create form. Create object and use . operator

form = st.form("Form 1")
form.text_input("What is your reason!")
form.form_submit_button("Submit")

#way 2 is with help of with keyword
with st.form("Form 2"):

    st.text_input("What's your second reason?")
    st.form_submit_button("Submit")