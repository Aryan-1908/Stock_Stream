import pandas as pd
import yfinance as yf

def load_data(ticker, start_date, end_date):
    """
    Load stock data using yfinance for a given ticker and date range.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    data['Ticker'] = ticker
    return data

def add_indicators(data):
    """
    Adds Bollinger Bands and Moving Averages to the data.
    """
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['Bollinger_Upper'] = data['SMA_20'] + (data['Close'].rolling(window=20).std() * 2)
    data['Bollinger_Lower'] = data['SMA_20'] - (data['Close'].rolling(window=20).std() * 2)
    return data
