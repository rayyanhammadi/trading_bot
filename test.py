try:
    import pandas as pd
    from service.binance_service import BinanceService
    from strategies.strategy import Strategy
    from backtests.backtester import Backtester
    from backtests.historical_data import HistoricalData
    from service.data_provider_service import Data
    from utils.helpers import TechnicalAnalysis
    from utils.consts import INTERVAL, SYMBOLS, INDICATORS
    from datetime import datetime
except Exception as e:
    raise e


indicators = {'trend': {'indicator1': {'name': INDICATORS.EMA50, 'params': None}},
              'momentum': {'indicator1': {'name': INDICATORS.RSI, 'params': {"window" : 14}}}}
strategy = Strategy("bu baker","RSI + BB", INTERVAL.ONE_MONTH)
strategy.tradable_coins = [SYMBOLS.BTCUSDT, SYMBOLS.ETHUSDT]
strategy.indicators = indicators
client = BinanceService(key="lbrCzGsrBGwdhba84A9hNBmBLyLdKjrF0f45BXw36i4J3qN2gMZ9UyweigUrhIlF",
                        secret="84759Gd37HRCuQhSbmTpkyYzECdvQ6auGcKZ8HDwQFH3aqSHrpBpsc5jJLgb1Yv0")
data = Data(client=client, symbol=SYMBOLS.ETHUSDT, interval=INTERVAL.ONE_WEEK, start_date="1 JANUARY 2020")
historical_data = HistoricalData(data)
backtester = Backtester(1000, strategy=strategy, hist_data=historical_data)

backtester.start_backtest()
#todo : test backtest (thx for playing)
