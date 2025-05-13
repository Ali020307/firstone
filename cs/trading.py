import ccxt
import numpy as np
import time
import requests
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator

# Параметры стратегии
symbol = 'BTC/USDT'
timeframe = '1h'
rsi_period = 14
sma_period = 20
rsi_buy = 30
rsi_sell = 70

# Telegram
TELEGRAM_TOKEN = '7633447499:AAGXYYR_A1KI8inFb6Q5lcyRBadJ48Cr2YI'
CHAT_ID = 282752187

def send_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)

# Binance API через CCXT
exchange = ccxt.binance()

while True:
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=100)
        close_prices = np.array([x[4] for x in ohlcv])

        rsi = RSIIndicator(close_prices, rsi_period).rsi()
        sma = SMAIndicator(close_prices, sma_period).sma_indicator()

        current_price = close_prices[-1]
        current_rsi = rsi[-1]
        current_sma = sma[-1]

        if current_rsi < rsi_buy and current_price > current_sma:
            send_telegram(f"📈 BUY Signal: Цена {current_price:.2f}, RSI={current_rsi:.2f}")
        elif current_rsi > rsi_sell and current_price < current_sma:
            send_telegram(f"📉 SELL Signal: Цена {current_price:.2f}, RSI={current_rsi:.2f}")
        else:
            print("⏳ No signal. Watching...")

    except Exception as e:
        print(f"Ошибка: {e}")

    time.sleep(60 * 60)  # Ждём 1 час

