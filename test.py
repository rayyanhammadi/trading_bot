try:
    import pandas as pd
    from service.binance_service import BinanceService
    from strategies.strategy import Strategy
    from backtests.historical_data import HistoricalData
    from utils.helpers import TechnicalAnalysis
    from utils.consts import INTERVAL, SYMBOLS, TA_INDICATORS
except Exception as e:
    raise e


indicators = {'trend': {'indicator1': {'name': TA_INDICATORS.EMA50, 'params': None}},
              'momentum': {'indicator1': {'name': TA_INDICATORS.RSI, 'params': {"window" : 14}}}}
strategy = Strategy("bu baker","RSI + BB", INTERVAL.ONE_MONTH)
strategy.tradable_coins = [SYMBOLS.BTCUSDT, SYMBOLS.ETHUSDT]
strategy.indicators = indicators
client = BinanceService(key="lbrCzGsrBGwdhba84A9hNBmBLyLdKjrF0f45BXw36i4J3qN2gMZ9UyweigUrhIlF",
                        secret="84759Gd37HRCuQhSbmTpkyYzECdvQ6auGcKZ8HDwQFH3aqSHrpBpsc5jJLgb1Yv0")
historical_data = HistoricalData(client.get_historical_raw_data(SYMBOLS.ETHUSDT, INTERVAL.ONE_WEEK, "1 JANUARY 2020"))
# print(historical_data.df)
print(historical_data.prepare_backtesting_data(strategy=strategy))
