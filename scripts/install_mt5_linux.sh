#!/bin/bash
echo "Menginstal MetaTrader 5..."
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install -y wine64 wine32

wget https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe -O mt5setup.exe
WINEPREFIX=~/.mt5 wine mt5setup.exe /S

# Set environment variable
echo 'export MT5_PATH="$HOME/.mt5/drive_c/Program Files/MetaTrader 5/terminal64.exe"' >> ~/.bashrc
source ~/.bashrc