import ta.trend
import ta.volatility
import ta.momentum
import pandas as pd
from utils.consts import TA_INDICATORS



class TechnicalAnalysis:

    @staticmethod
    def get_indicator_data(data: pd.DataFrame, indicator_name: str, params: dict):
        if indicator_name == TA_INDICATORS.RSI:
            return ta.momentum.rsi(data['close'], params['window'])
        elif indicator_name == TA_INDICATORS.STOCH_RSI:
            return ta.momentum.stochrsi(data['close'], params['window'])
        elif indicator_name == TA_INDICATORS.EMA20:
            return ta.trend.ema_indicator(data['close'], 20)
        elif indicator_name == TA_INDICATORS.EMA50:
            return ta.trend.ema_indicator(data['close'], 50)
        elif indicator_name == TA_INDICATORS.EMA100:
            return ta.trend.ema_indicator(data['close'], 100)
        elif indicator_name == TA_INDICATORS.EMA200:
            return ta.trend.ema_indicator(data['close'], 200)
        elif indicator_name == TA_INDICATORS.HIGH_BOL_BAND:
            return ta.volatility.bollinger_hband(data['close'], params['window'])
        elif indicator_name == TA_INDICATORS.LOW_BOL_BAND:
            return ta.volatility.bollinger_lband(data['close'], params['window'])
        elif indicator_name == TA_INDICATORS.MAVG_BOL_BAND:
            return ta.volatility.bollinger_mavg(data['close'], params['window'])
