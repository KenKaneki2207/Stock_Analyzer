import yfinance as yf
import pandas as pd

stock_list = ['ADANIPOWER','UNIONBANK','BHEL','OIL','RVNL','SUZLON',
              'PNB','GAIL','ZOMATO','HINDALCO','ONGC','NTPC','BPCL','BEL','TATAMOTORS']
intervals = ['1m','5m','15m','1h','1d']

def download_data(stock, interval):
    # Choosing the period for respective intervals
    if interval == "1m":
        period = "2d"
    elif interval == "5m":
        period = "5d"
    elif interval == "15m":
        period = '15d'
    elif interval == "1h":
        period = "60d"
    else:
        period = "200d"

    # Downloading the data from Yahoo Finance
    df = yf.Ticker(f"{stock}.NS").history(period=period, interval=interval)

    # converting datetime(index) into a column
    df = df.reset_index()
    return df

def conversion_candle(df):
    if df.columns[0] == "Date":
        date = "Date"
    else:
        date = "Datetime"

    df[date] = df[date].dt.tz_localize(None)
    df[date] = df[date].astype('int64') // 10**9

    # renaming the columns to be compatible with streamlit-lightweight-charts
    df = df.rename(columns={date: "time", 
                            "Open": "open", 
                            "High": "high", 
                            "Low": "low", 
                            "Close": "close", 
                            "Volume": "volume"})
    
    # reordering the columns and removing the unwanted columns (i.e. stock_splits, dividends)
    df = df[["time", "open", "high", "low", "close", "volume"]]

    # converting to dictionary(json) format
    df = df.to_dict(orient='records')
    return df

def conversion_line(df):
    if df.columns[0] == "Date":
        date = "Date"
    else:
        date = "Datetime"

    df[date] = df[date].dt.tz_localize(None)
    df[date] = df[date].astype('int64') // 10**9

    # renaming the columns to be compatible with streamlit-lightweight-charts
    df = df.rename(columns={date: "time", 
                            "Close": "value", 
                            "Volume": "volume"})
    
    # reordering the columns and removing the unwanted columns (i.e. stock_splits, dividends)
    df = df[["time", "value", "volume"]]

    # converting to dictionary(json) format
    df = df.to_dict(orient='records')
    return df

def chart_data(chart, stock, interval):
    if chart == "Candle":
        data = conversion_candle(download_data(stock, interval))
    else:
        data = conversion_line(download_data(stock, interval))

    return data

