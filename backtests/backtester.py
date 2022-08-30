"""Backtesting tool"""
try:
    from datetime import datetime
    import time
    from bots.trader import Trader
    import logging
    from typing import Optional
    from strategies.strategy import Strategy
    from backtests.historical_data import HistoricalData
    from utils.consts import INTERVAL, POSITIONS
except Exception as e:
    print(e)


class Backtester(Trader):

    """ Backtester class """

    def __init__(self, starting_balance: float, hist_data: HistoricalData, strategy: Strategy,
                 margin_enabled: bool = False, precision: int = 4, logger: bool = False):

        super().__init__(tradable_coins=strategy.tradable_coins, precision=precision,
                         starting_balance=starting_balance, margin_enabled=margin_enabled)
        
        self.df = hist_data.df
        self.strategy = strategy
        self.interval = hist_data.interval
        self.start_date = hist_data.start_date
        self.end_date = hist_data.end_date
        self.balance: float = 0

    @staticmethod
    def generate_error_message(error: Exception, strategy) -> str:
        """
        Error message generator when running a backtest.
        :param error: Error object.
        :param strategy: Strategy that caused this error.
        :return: String containing error message.
        """
        return f'It looks like your strategy has crashed because of: "{str(error)}". Try using' \
               f' different parameters, rewriting your strategy, or taking a look at ' \
               f'your strategy code again. The strategy that caused this crash is: ' \
               f'{strategy.name}. You can find more details about the crash in the ' \

    
    def start_backtest(self):
        """
        Main function to start a backtest.
        :param : ____
        """

        self.starting_time = time.time()
        
        if len(self.strategies) == 0:
            raise "No implemented strategy"
        else:
            for strategy in self.strategies:
                self.strategy = strategy
                for coin in strategy.tradable_coins:
                    self.strategy_backtest(coin)

                self.get_strategy_performance_against_hodl()

    # def exit_backtest(self, index: int = None):
    #     """
    #     Ends a backtest by exiting out of a position if needed.
    #     """
    #     if index is None:
    #         index = self.end_date
    #
    #     self.current_period = self.df[index]
    #
    #     # if self.current_position == POSITIONS.SHORT:
    #     #     self.buy_short("Exited short position because backtest ended.")
    #     # elif self.current_position == POSITIONS.LONG:
    #     #     self.sell_long("Exited long position because backtest ended.")
    # #
    def strategy_backtest(self, coin):
        """
        Perform a backtest with provided strategies to backtester object.
        :coin ___.
        """

        for index, row in self.df.iterrows():
            if self.strategy.get_strategy_current_position(row) == "LONG":
                buy_price = row['close']
                self.coin[coin] = self.balance / buy_price
                self.commissions_paid += self.coin['coin']*self.transaction_fee_percentage_decimal*buy_price
                self.coin[coin] -= self.coin['coin']*self.transaction_fee_percentage_decimal
                self.balance = 0
                self.trades[index] = {"side": 'buy', "buy price": row['close']}
                self.current_position = POSITIONS.LONG
            elif self.strategy.get_strategy_current_position(row) == "SHORT":
                sell_price = row['close']
                self.balance = self.coin[coin] * sell_price
                self.commissions_paid += self.balance*self.transaction_fee_percentage_decimal
                self.balance -= self.balance*self.transaction_fee_percentage_decimal
                self.coin[coin] = 0
                self.trades[index] = {"side": 'sell', "sell price": row['close']}
                self.current_position = POSITIONS.SHORT

    def get_strategy_performance_against_hodl(self):
        first_close = self.df.iloc[0]['close']
        last_close = self.df.iloc[-1]['close']
        self.balance = final_balance = self.balance + sum([self.coin[coin] for coin in
                                                           self.tradable_coins])*self.df.iloc[-1]['close']
        holding_percentage = (last_close-first_close)/first_close * 100
        strategy_percentage = (final_balance-self.starting_balance)/self.starting_balance * 100
        print(f'from{self.start_date} -------> {self.end_date}\n '
              f'Strategy name: {self.strategy.name}\n'
              f'Starting balance: {self.starting_balance}$\n '
              f'Final balance: {self.balance}$\n'
              f'Coins we own:  {self.coin}\n'
              f'Strategy performance vs $USD: {strategy_percentage}%\n'
              f'Buy and Hold: {holding_percentage}\n'
              f'Total fees paid: {self.commissions_paid}$\n')

    #     todo: finish after finishing data providing and cleaning

