import streamlit as st
import pandas as pd
import time

st.title("Some Text Functions")
st.subheader("Beginning text functions in streamlit")
st.header("First heading")
st.text("A simuation of <p> tag from html")
st.markdown(" **HELLO YA'LL**")
st.latex(r'\begin{pmatrix}1&2\\3&4\end{pmatrix}')
json = {"Rahul":"amazing, beautiful, perfect",
        "Lukas":"bitch, classy, gonna be rich"}

st.json(json)
code = """
def newfunction() -> None:
    print("text functions")
"""
st.code(code, language = 'python')

#swiss army knife for all above text elements
text= """
The swiss knife of text functions is:
```python
streamlit.write()
```
"""
st.write(text)
st.metric(label="My speed", value='12m/s', delta = '-2m/s')

#table
table = pd.DataFrame({"Col 1": [1, 2, 34, 5, 6], "Col2": [3, 4, 5, 6, 8]})
st.table(table)

#dataframe
st.dataframe(table)

#image
st.image("./data/image.jpeg", caption="My breakfast", width=500)

#audio
st.audio("./data/audio.mp3")

#video
st.video("./data/video.mp4")

##### INTERACTIVE ELEMENTS
def callback():
    print(st.session_state.checker)

state = st.checkbox("Male", value=False, 
                    on_change=callback,
                    key='checker')
if state:
    st.write("Hi!")

radio_btn = st.radio(label="What's your country?", 
options = ("India", "Other")) 
print(radio_btn)

def btn_click():
    print('button clicked')
btn = st.button("Click me!", on_click=btn_click)

#select boxes
sb = st.selectbox("What is your favorite car?",
options=("Audi", "Nano", "YEAHHH"))

#multiselect
ms = st.multiselect("Which courses are your favorite?",
options=("Math", 'Computer Science', 'statistics', 'DS'))
st.write(ms)

#fileuploader
st.title("Uploading files")
st.markdown('---')
images = st.file_uploader("Please upload a media",
                 type=['png', 'jpg', 'jpeg', 'mp4'], 
                 accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)

###### more interactive stuff
value = st.slider("Choose age", min_value=10, max_value=90, value=18)
print(value)

val = st.text_input(label="Enter name")
texts = st.text_area(label="Describe your name")
print(texts)

date = st.date_input("Enter your birth date")
times = st.time_input("Set timer")

######## Progress bars
bar = st.progress(0)
progress_status = st.empty()
for i in range(10):
    bar.progress((i+1)*10)
    progress_status.write(str((i+1)*10) + "%")
    time.sleep(1)
