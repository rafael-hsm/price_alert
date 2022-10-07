from utils.common_tools import *
from utils.alert import message_alert

from datetime import datetime

import yfinance as yf

logging.basicConfig(level=logging.INFO, filename='../price_alert/log/main.log',
                    format='%(asctime)s :: %(levelname)s :: %(lineno)d :: '
                           '%(funcName)s :: %(message)s :: %(filename)s',
                    datefmt='%d-%b%y %H:%M:%S')


class PriceAlert:
    def __init__(self, asset: str, waiting_time: float):
        self.waiting_time = waiting_time
        self.asset = asset

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"

    def getting_price(self):
        time_now = datetime.now()
        ticker_price = yf.Ticker(self.asset).history(interval="1m", period="1d")
        print(f'\nConsult at: {time_now}')
        print(f"Ticker {self.asset} - Current price = $ {round(ticker_price['Close'][-1], 2)}")

        return time_now, ticker_price['Close'][-1]

    def check_price(self):
        try:
            current_price = self.getting_price()[1]
            price_above = float(input(f"Type a price bigger than {round(current_price, 2)}: "))
            price_bellow = float(input(f"Type a price less than {round(current_price, 2)}: "))
            if round(current_price, 2) <= price_bellow:
                message_alert(self.asset, price=round(current_price['Close'][-1], 2))
                quit()
            if round(current_price, 2) >= price_above:
                message_alert(self.asset, price=round(current_price['Close'][-1], 2))
                quit()

        except TypeError as e:
            print(e)
            print('Please enter a float number: 10.0')
            quit()



    def price_alert_request(self):
        header(msg='Price Alert')
        print('Example: ticker= MSFT ')
        print('Type a time in seconds to monitoring [5]: ')
        print(self.getting_price()[1])
        schedule_function(function=self.check_price, time_seconds=self.waiting_time)


if __name__ == '__main__':
    price = PriceAlert(asset='TSLA', waiting_time=2)
    price.price_alert_request()
