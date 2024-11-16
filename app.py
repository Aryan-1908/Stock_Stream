import streamlit as st
import pandas as pd
from data_loader import load_data, add_indicators
from strategy import bollinger_strategy
from backtest_engine import backtest
import matplotlib.pyplot as plt

st.title("Backtest Bollinger Bands & Moving Average Strategy")

# Input Section
ticker = st.text_input("Enter Stock Ticker", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2023-01-01"))
initial_capital = st.number_input("Initial Capital", min_value=1000, value=10000, step=1000)
investment_type = st.selectbox("Investment Type", ["aggressive", "moderate", "passive"])

# Load and Display Data
data = load_data(ticker, start_date, end_date)
data = add_indicators(data)
st.subheader("Stock Data with Indicators")
st.dataframe(data.tail())

# Plotting
fig, ax = plt.subplots()
ax.plot(data.index, data['Close'], label='Close Price')
ax.plot(data.index, data['SMA_20'], label='SMA 20')
ax.plot(data.index, data['Bollinger_Upper'], label='Upper Band', linestyle='--')
ax.plot(data.index, data['Bollinger_Lower'], label='Lower Band', linestyle='--')
ax.legend()
st.pyplot(fig)

# Backtest
buy_signals, sell_signals = bollinger_strategy(data, investment_type)
final_capital, avg_return, hodl_return = backtest(data, buy_signals, sell_signals, initial_capital)

# Display Metrics
st.subheader("Backtest Results")
st.write(f"Final Capital: ${final_capital:.2f}")
st.write(f"Average Return per Trade: {avg_return * 100:.2f}%")
st.write(f"HODL Return: {hodl_return * 100:.2f}%")
