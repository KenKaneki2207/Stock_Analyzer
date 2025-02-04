import yfinance as yf
import pandas as pd
import time

stock_list = ['ADANIPOWER','UNIONBANK','BHEL','OIL','RVNL','SUZLON',
              'PNB','GAIL','ZOMATO','HINDALCO','ONGC','NTPC','BPCL','BEL','TATAMOTORS']
intervals = ['1m','5m','15m','1h','1d']

def download_data():
    for stock in stock_list:
        for interval in intervals:
            df = yf.Ticker(f"{stock}.NS").history(period='1d', interval=interval)
            df = df.reset_index()
            if interval != '1d':
                df['Datetime'] = df['Datetime'].dt.tz_localize(None)
            else:
                df = df.rename(columns={"Date":"time"})
            df['Datetime'] = df['Datetime'].astype('int64') // 10**9
            df = df.rename(columns={"Datetime": "time", "Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume":"volume"})
            df = df[["open", "high", "low", "close", "time", "volume"]]
            df.to_csv(f'stock_data/{interval}/{stock}.csv')
            print(f"Successfully downloaded the {stock} with interval {interval}")

def convert_the_data():
    for stock in stock_list[1:]:
        for interval in intervals[:4]:
            df = pd.read_csv(f'stock_data/{interval}/{stock}.csv', parse_dates=['Datetime'])
            df['Datetime'] = df['Datetime'].astype('int64') // 10**9
            df = df.rename(columns={"Datetime": "time", "Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume":"volume"})
            df = df[["open", "high", "low", "close", "time", "volume"]]

            df.to_csv(f'stock_data/{interval}/{stock}.csv')
            print(f"Successfully downloaded the {stock} with interval {interval}")

def update_data(ticker):
    for interval in intervals:
        df = yf.Ticker(ticker).history(period="1d", interval=interval)
        df = df.reset_index()
        if interval != "1d":
            df = df.rename(columns={"Datetime": "time", "Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume":"volume"})
            df = df[["open", "high", "low", "close", "time", "volume"]]
        else:
            df = df.rename(columns={"Date": "time", "Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume":"volume"})
            df = df[["open", "high", "low", "close", "time", "volume"]]

        
        df['time'] = df['time'].astype('int64') // 10**9
        print(df)
