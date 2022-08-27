"""Base class for strategy creation"""
from typing import Optional
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

    def get_trend(self, df: pd.DataFrame, data, log_data: bool = False) -> int:
        """ gives the current trend
         bearish (short position) : -1
         neutral : 0
         bullish (long position) : 1
         """

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


