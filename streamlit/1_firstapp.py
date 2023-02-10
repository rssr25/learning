import yfinance as yf
import streamlit as sl
import pandas as pd


sl.title("Hello!")
sl.write("""

# Simple stock price app

Shown are the stock **closing price** and **volume** for Apple

""")

tickrSymbol='AAPL'
tickrData = yf.Ticker(tickrSymbol)
tickrDf = tickrData.history(period='1d', start='2010-01-01', end='2022-01-01')

sl.write('''
## Closing price
''')
sl.line_chart(tickrDf.Close)

sl.write('''
## Volume
''')
sl.line_chart(tickrDf.Volume)