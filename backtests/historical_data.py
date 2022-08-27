""" import dataset, indicators for backtesting """

import pandas as pd
import ta
import logging
from strategies.strategy import Strategy
from utils.helpers import TechnicalAnalysis
from utils.consts import INTERVAL, SYMBOLS , TA_INDICATORS


class HistoricalData:
    """historical data provider"""

    def __init__(self, data_frame):
        self.df = data_frame

    def process_data(self):

        self.df = self.df.set_index(self.df['timestamp'])
        self.df.index = pd.to_datetime(self.df.index, unit='ms')
        self.df['close'] = pd.to_numeric(self.df['close'])
        self.df['high'] = pd.to_numeric(self.df['high'])
        self.df['low'] = pd.to_numeric(self.df['low'])
        self.df['open'] = pd.to_numeric(self.df['open'])
        del self.df['timestamp']

        print('clean market_data loaded')

        return self.df

    def sets_ta_indicators(self, strategy: Strategy = None):
        for indicator_type in strategy.indicators:
            for indicator in strategy.indicators[indicator_type]:
                strat_info = strategy.indicators[indicator_type][indicator]
                self.df[strat_info['name']] = TechnicalAnalysis.get_indicator_data(self.df, strat_info['name'], strat_info['params'])

    def prepare_backtesting_data(self, strategy: Strategy = None):

        self.process_data()
        self.sets_ta_indicators(strategy=strategy)

        return self.df
