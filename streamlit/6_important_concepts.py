import streamlit as st

def printer(name):
    print(name)
input = st.text_input("Enter your name")
s_btn = st.button("Submit")

## Whenever a checkbox is selected, the entire script runs
if s_btn:
    opt = st.checkbox("Want to display your name?", on_change=printer, args=(input,))

#### session states
#way of sharing variables between reruns for users

text = "😍"
btn = st.button(text, key='btn1')
if btn:
    text="😙"
#nothing happens when you click, because streamlit reruns.
#session states allows reserve the values of the variables

text = "😍"
if "click" not in st.session_state:
    st.session_state.click = False
else:
    if st.session_state.click == False:
        text="😙"
        st.session_state.click = True
    else:
        text = "😍"
        st.session_state.click = False

btn = st.button(text)

