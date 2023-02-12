import streamlit as st
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie
import json

# com.iframe('https://embed.lottiefiles.com/animation/134351')

with open("animation.json") as source:
    animation = json.load(source)


st_lottie(animation)
