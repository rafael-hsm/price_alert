from datetime import datetime

import yfinance as yf


def getting_price(ticker):
    time_now = datetime.now()
    ticker_price = yf.Ticker(ticker).history(interval="1m", period="1d")
    print(f'Consult at: {time_now}')
    print(f"Current price = $ {round(ticker_price['Close'][-1], 2)}")
    return time_now, ticker_price
