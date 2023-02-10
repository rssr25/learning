import streamlit as st

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