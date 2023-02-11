import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure()
def date_converter(date_col):
    result = list()
    values = date_col.values

    for value in values:
        result.append(str(value).split("T")[0])
    return result

st.markdown("""
# Data Visualizer
---
""")

file_names = list()
files = st.file_uploader("Upload Multiple Files", type=["xlsx"], accept_multiple_files=True)
if files:
    for file in files:
        file_names.append(file.name)
    
    selected_files = st.multiselect("Select Files", options=file_names)
    
    if selected_files:
        options = ("None", "GPU", "CPU", "KEYBOARD", "MOUSE", "CASING")
        option = st.radio("Select Entity Against Date", options=options)
        if option != "None":
            for file in files:
                #check names of files which user has selected
                if file.name in selected_files:
                    shop_data = pd.read_excel(file, index_col=0)
                    item = list(shop_data[option])
                    dates = date_converter(shop_data["DATE"])

                    index = np.arange(len(dates))
                    plt.xticks(index, dates)
                    plt.gcf().autofmt_xdate()
                    plt.plot(index, item, label=file.name, marker='o')
                    plt.xlabel("Date")
                    plt.ylabel(option)
                    plt.title(option + " chart")
                    plt.grid(True)
                    plt.legend()

            
            st.write(fig)