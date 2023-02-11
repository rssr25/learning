import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
bar_x = np.array([1, 2, 3, 4, 5])

opt = st.sidebar.radio('SELECT A GRAPH', options=("Line", "Bar", "Scatter"))
if opt == "Line":

    st.markdown("## Line chart")
    fig = plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle')
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), '--')

    st.write(fig)

elif opt == "Bar":
    st.markdown("## Bar chart")
    fig = plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle')
    plt.bar(x, x*2)
    st.write(fig)

else:
    st.markdown("## Scatter chart")
    fig = plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-light.mplstyle')
    plt.scatter(x, x*2, s=0.5)
    st.write(fig)