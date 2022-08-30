"""Trader class"""
from typing import Dict
from utils.consts import SIDE, SYMBOLS
from strategies.strategy import Strategy
from datetime import datetime
class Trader:
    def __init__(self,tradable_coins, precision, starting_balance, margin_enabled: bool = False):

        self.starting_balance = starting_balance  # Balance we started bot with.
        self.balance = starting_balance  # USDT Balance.
        self.previous_net = starting_balance  # Our previous net will just be the starting balance in the beginning.
        self.coin: dict = {str: float}  # amount of coins we own
        self.transaction_fee_percentage_decimal: float = 0.007  # Binance transaction fee percentage.
        self.tradable_coins: [str] = tradable_coins
        self.commissions_paid = 0  # Total commissions paid by this smart(?) trader
        self.trades: Dict[str, Dict] = {}  # All trades performed #todo add trades performance.
        self.strategies: [Strategy] = []

        self.starting_time = datetime.utcnow()  # Starting time in UTC.
        self.ending_time = None  # Ending time for previous bot run.
        self.current_period = None  # Current time period the bot is in used for backtesting.
        self.current_position = None  # Current position value.
        self.min_period = 0  # Minimum amount of periods required for trend retrieval.
        self.previous_position = None  # Previous position to validate for a new trend.
        self.trend = None  # Current trend information.
        self.margin_enabled = margin_enabled  # Boolean for whether margin trading is enabled or not.

        self.take_profit_point = None  # Price at which bot will exit trade to secure profits.
        self.trailing_take_profit_activated = False  # Boolean that'll turn true if a stop order is activated.
        self.take_profit_type = None  # Type of take profit: trailing or stop.
        self.take_profit_percentage_decimal = None  # Percentage of profit to exit trade at.

        self.stop_loss = None  # Price at which bot will exit trade due to stop loss limits.
        self.stop_loss_exit = False  # Boolean that'll determine whether last position was exited from a stop loss.
        self.loss_percentage_decimal = None  # Loss percentage in decimal for stop loss.

    def add_trade(self, side, amount, pair, msg):
        """adds a trade to list of trades"""

        self.trades[str(self.current_period)] = {"side": side,
                                                 "pair": pair,
                                                 "amount": amount,
                                                 "why?" : msg}

    def reset_trades(self):
        """
        Clears trades list.
        """
        self.trades = {}

    def get_position(self) -> int:
        """
        Returns current position.
        :return: Current position integer bot is in.
        """
        return self.current_position

    @staticmethod
    def get_profit_or_loss_string(profit: float) -> str:
        """
        Helper function that returns where profit specified is profit or loss. Profit is positive; loss if negative.
        :param profit: Amount to be checked for negativity or positivity.
        :return: String value of whether profit ir positive or negative.
        """
        return "Profit" if profit >= 0 else "Loss"

    @staticmethod
    def get_profit_or_loss_string(profit: float) -> str:
        """
        Helper function that returns where profit specified is profit or loss. Profit is positive; loss if negative.
        :param profit: Amount to be checked for negativity or positivity.
        :return: String value of whether profit ir positive or negative.
        """
        return "Profit" if profit >= 0 else "Loss"

    def get_strategy_inputs(self, strategy_name: str):
        """
        Returns provided strategy's inputs if it exists.
        """
        if strategy_name not in self.strategies:
            return 'Strategy not found.'
        else:
            return self.strategies[strategy_name].values

    def get_strategies_info_string(self, left: str = '\t', right: str = '\n'):
        """
        Returns a formatted string with strategies information.
        :param left: Character to add before each new line in strategies information.
        :param right: Character to add after each new line in strategies information.
        """
        # string = f'Strategies:{right}'
        # for strategy_name in self.strategies:
        #     string += f'{left}{get_label_string(strategy_name)}: {self.get_strategy_inputs(strategy_name)}{right}'
        #
        # return string.rstrip()  # Remove new line in the very end.

    def get_net(self) -> float:
        """
        Returns net balance with current price of coin being traded. It factors in the current balance, the amount
        shorted, and the amount owned.
        :return: Net balance.
        """
        #todo finish net computation

        # return self.coin * self.current_price - self.coin_owed * self.current_price + self.balance