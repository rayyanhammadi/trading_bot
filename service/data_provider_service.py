try:
    from service.binance_service import BinanceService
    import pandas as pd
except Exception as e:
    print(e)


class Data:
    def __init__(self, client: BinanceService,interval: str, symbol: str, start_date: str, end_date: str = None):
        self.df = None
        self.client = client
        self.interval = interval
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

    def get_historical_raw_data(self):
        self.df = pd.DataFrame(self.client.get_historical_klines(symbol=self.symbol, interval=self.interval,
                                                            start_str=self.start_date, end_str=self.end_date),
                          columns=['timestamp', 'open', 'high', 'low',
                                   'close', 'volume', 'close_time', 'quote_av',
                                   'trades', 'tb_base_av', 'tb_quote_av', 'ignore'],
                          )
        self.df.drop(columns=self.df.columns.difference(['timestamp', 'open', 'high', 'low', 'close', 'volume']), inplace=True)

        return self.df

