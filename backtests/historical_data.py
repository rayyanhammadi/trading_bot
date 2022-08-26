""" import dataset, indicators for backtesting """

import pandas as pd
import ta
import logging
from strategies.strategy import Strategy
from utils.helpers import TechnicalAnalysis


class HISTROICAL_DATA():
    """historical data provider"""
    def __int__(self, data_frame):
        self.df = data_frame

    def process_data(self):

        self.df = self.df.set_index(self.df['timestamp'])
        self.df.index = pd.to_datetime(self.df.index, unit='ms')
        del self.df['timestamp']

        print('clean market_data loaded')

        return self.df

    def sets_ta_indicators(self, strategy: Strategy = None):
        for indicator_type in strategy.indicators:
            for indicator in indicator_type:
                self.df[indicator] = TechnicalAnalysis.get_indicator_data(self.df,indicator, indicator['params'])


