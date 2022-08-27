"""binance service"""
try:
    import pandas as pd
    from binance import Client
    from utils.consts import INTERVAL
except Exception as e:
    print(e)


class BinanceService:
    """binance service"""

    def __init__(self, key: str, secret: str):
        """constructor"""
        self.client = Client(api_key=key, api_secret=secret)

    def get_historical_raw_data(self, symbol, interval: str, start_date: str, end_date: str = None):
        df = pd.DataFrame(self.client.get_historical_klines(symbol=symbol, interval=interval,
                                                            start_str=start_date, end_str=end_date),
                          columns=['timestamp', 'open', 'high', 'low',
                                   'close', 'volume', 'close_time', 'quote_av',
                                   'trades', 'tb_base_av', 'tb_quote_av', 'ignore'],
                          )
        df.drop(columns=df.columns.difference(['timestamp','open', 'high', 'low', 'close', 'volume']), inplace=True)

        return df

