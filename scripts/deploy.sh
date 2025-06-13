#!/bin/bash
echo "Mendeploy trading bot..."

# Buat systemd service
sudo tee /etc/systemd/system/trading-bot.service > /dev/null <<EOL
[Unit]
Description=AI Trading Bot
After=network.target

[Service]
User=$USER
WorkingDirectory=$(pwd)
ExecStart=$(which python) src/trading_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOL

# Aktifkan service
sudo systemctl daemon-reload
sudo systemctl start trading-bot
sudo systemctl enable trading-bot

# Setup auto-retrain
(crontab -l ; echo "0 3 * * MON $(pwd)/scripts/training.sh") | crontab -