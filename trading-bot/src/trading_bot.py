import MetaTrader5 as mt5
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from config.settings import SYMBOL, TIMEFRAME, RISK_PERCENT
from src.data_loader import get_realtime_data, preprocess_data
from src.utils import execute_trade
import time
import os

def init_mt5():
    if not mt5.initialize():
        raise ConnectionError("Gagal menginisialisasi MT5")
    print("Terhubung ke MT5")

def main():
    # Load model
    model = load_model('models/trading_model.keras')
    
    # Init MT5
    init_mt5()
    
    while True:
        try:
            # Ambil data real-time
            raw_data = get_realtime_data()
            processed_data = preprocess_data(raw_data)
            
            # Prediksi
            prediction = model.predict(np.array([processed_data]))[0][0]
            current_price = raw_data['close'].iloc[-1]
            
            # Eksekusi trading
            if prediction > current_price + 0.0005:
                execute_trade("BUY", RISK_PERCENT)
            elif prediction < current_price - 0.0005:
                execute_trade("SELL", RISK_PERCENT)
                
            time.sleep(60)
            
        except Exception as e:
            print(f"Error: {str(e)}")
            time.sleep(30)

if __name__ == "__main__":
    main()