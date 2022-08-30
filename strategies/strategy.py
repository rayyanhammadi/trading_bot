"""Base class for strategy creation"""
from typing import Optional
from utils.consts import INDICATORS, F_G_STATUS, POSITIONS
import pandas as pd
import ta


class Strategy:
    """Strategy class"""
    def __init__(self, name: str = None, description: str = "No strategy description", time_frame: str = None):
        self.name: str = name
        self.description = description
        self.trend: Optional[int] = None
        self.time_frame = time_frame
        self.tradable_coins: [str] = None
        self.indicators: {str: {{str: int}}} = {}
            # {'trend': {'name': str, 'params': {str: int}},
           # 'momentum': {'name': str, 'params': {str: int}},
           #  'volatility': {'name': str, 'params': {str: int}}}

    def get_strategy_current_position(self, indicators,index = None, price: int = None,) -> str:
        """ retuns the position that the trader should take according the strategy.
         Here, strategy is :
            when srsi <~0.3, rsi <~0.3 and f&g index == extreme fear: buy i.e. should go long
            when srsi >~0.8, rsi>~0.8 and f&g index == extreme greed: sell i.e. should go short
         """
        if indicators[INDICATORS.STOCH_RSI] < 0.3 and indicators[INDICATORS.RSI] < 0.3 and indicators[INDICATORS.F_G] == F_G_STATUS.EXTREME_FEAR:
            self.trend = POSITIONS.LONG
            return self.trend
        elif indicators[INDICATORS.STOCH_RSI] > 0.8 and indicators[INDICATORS.RSI] > 0.8 and indicators[INDICATORS.F_G] == F_G_STATUS.EXTREME_GREED:
            self.trend = POSITIONS.SHORT
            return self.trend



    def get_histroical_performance(self, data: dict = None) -> dict :
        """ returns data on how this strategy performed
        by the past:
            - #good trades and bad trades
            - max drawdown
        """
        pass

    def log_performance(self):
        """records performance"""

        pass

    def strategy_configuration(self):
        """sets strategy configuration such as:
            -name and description
            -time_frame or interval
            -tradble coins
            - technical indicators allowed"""


