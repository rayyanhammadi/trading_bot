"""binance service"""
try:
    from binance import Client
    from utils.consts import INTERVAL
except Exception as e:
    print(e)


class BinanceService:
    """binance service"""

    def __init__(self, key: str, secret: str):
        """constructor"""
        self.client = Client(api_key=key, api_secret=secret)

    def get_historical_klines(self,symbol, interval, start_str, end_str):
        return self.client.get_historical_klines(symbol=symbol, interval=interval, start_str=start_str, end_str=end_str)

