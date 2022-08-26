"""binance service"""
import pandas as pd
from binance import Client
from utils.consts import KLINE_INTERVAL

class BinanceService():

    def __int__(self, key,secret):
        self.client = Client(api_key=key,api_secret=secret)

    def get_historical_raw_data(self, symbol, interval: str, start_date: str, end_date:str):
        df = pd.DataFrame(self.client.get_historical_klines(symbol=symbol,interval=interval,
                                                            start_str= start_date, end_str=end_date),
                          columns=['timestamp', 'open', 'high', 'low',
                                   'close', 'volume', 'close_time', 'quote_av',
                                   'trades', 'tb_base_av', 'tb_quote_av', 'ignore'],
                          )
        df.drop(columns=df.columns.difference(['open', 'high', 'low', 'close', 'volume']), inplace=True)

        return df