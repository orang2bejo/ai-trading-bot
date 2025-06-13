import MetaTrader5 as mt5
import pandas as pd
import talib as ta
import numpy as np
from config.settings import SYMBOL, TIMEFRAME, LOOKBACK

def get_historical_data():
    rates = mt5.copy_rates_range(SYMBOL, TIMEFRAME, pd.Timestamp('2000-01-01'), pd.Timestamp.now())
    return pd.DataFrame(rates)

def get_realtime_data():
    rates = mt5.copy_rates_from_pos(SYMBOL, TIMEFRAME, 0, LOOKBACK)
    return pd.DataFrame(rates)

def preprocess_data(df):
    # Tambahkan indikator teknikal
    df['SMA50'] = ta.SMA(df['close'], 50)
    df['SMA200'] = ta.SMA(df['close'], 200)
    df['RSI'] = ta.RSI(df['close'], 14)
    df['MACD'], _, _ = ta.MACD(df['close'], 12, 26, 9)
    df['ATR'] = ta.ATR(df['high'], df['low'], df['close'], 14)
    df.fillna(method='bfill', inplace=True)
    
    # Pilih fitur
    features = ['close', 'SMA50', 'SMA200', 'RSI', 'MACD', 'ATR']
    return df[features].tail(LOOKBACK).values