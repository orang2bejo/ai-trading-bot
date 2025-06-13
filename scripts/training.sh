#!/bin/bash
echo "Memulai training model..."
python -c "
import tensorflow as tf
from src.model import create_model
from src.data_loader import load_and_preprocess_data

# Konfigurasi GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_memory_growth(gpus[0], True)
    except RuntimeError as e:
        print(e)

# Load data
X_train, y_train = load_and_preprocess_data()

# Buat dan train model
model = create_model(input_shape=(60, 20))
model.fit(X_train, y_train, epochs=1000000, batch_size=2048)

# Simpan model
model.save('models/trading_model.keras')
"