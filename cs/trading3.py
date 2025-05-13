import ccxt
import time
import pandas as pd
import requests
from ta.momentum import RSIIndicator
from ta.trend import SMAIndicator, MACD
from ta.volatility import AverageTrueRange

# Параметры
symbol = 'BTC/USDT'
timeframe = '15m'  # Уменьшили таймфрейм до 15 минут
rsi_period = 14
sma_period = 20
macd_fast = 12
macd_slow = 26
macd_signal = 9
rsi_buy = 30
rsi_sell = 70
atr_period = 14

# Риск-менеджмент
stop_loss_multiplier = 2  # Умножаем ATR для стоп-лосса
take_profit_multiplier = 3  # Умножаем ATR для тейк-профита
position_size = 0.01  # Размер позиции, например, 0.01 BTC

# API
binance_api_key = 'xLBxbAgDNWYTgd4GO1wDyZDhoZOPY6kGcmosi8uU7VQ3K0FINpnX3ssibg87Bkpa'
binance_api_secret = 'YRTJpTgVx9lEHOyKkM0PkU15OILIhdo2TDN0akpyPk8KtMPaMWYKhytGvPyxzfTj'

# Телеграм
TELEGRAM_TOKEN = '7633447499:AAGXYYR_A1KI8inFb6Q5lcyRBadJ48Cr2YI'
CHAT_ID = '282752187'

# Настройка API
exchange = ccxt.binance({
    'apiKey': binance_api_key,
    'secret': binance_api_secret,
    'enableRateLimit': True,
    'options': {'defaultType': 'future'}
})

# Функция для отправки сообщений в Telegram
def send_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)

# Функция для открытия ордера
def open_order(order_type, price):
    order = exchange.futures_create_market_order(symbol=symbol, side=order_type, quantity=position_size)
    send_telegram(f"Открыт ордер {order_type} по цене {price:.2f}")
    return order

# Функция для вычисления стоп-лосса и тейк-профита
def calculate_stop_loss_take_profit(entry_price, atr_value):
    stop_loss = entry_price - atr_value * stop_loss_multiplier
    take_profit = entry_price + atr_value * take_profit_multiplier
    return stop_loss, take_profit

# Основной цикл
while True:
    try:
        # Получаем данные о ценах
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe='15m', limit=50)  # Таймфрейм 15 минут и лимит 50 баров
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

        # Индикаторы
        rsi = RSIIndicator(df['close'], rsi_period).rsi()
        sma = SMAIndicator(df['close'], sma_period).sma_indicator()
        macd = MACD(df['close'], macd_fast, macd_slow, macd_signal)
        atr = AverageTrueRange(df['high'], df['low'], df['close'], atr_period).average_true_range()

        current_price = df['close'].iloc[-1]
        current_rsi = rsi.iloc[-1]
        current_sma = sma.iloc[-1]
        current_macd = macd.macd_diff().iloc[-1]
        atr_value = atr.iloc[-1]

        # Вычисляем стоп-лосс и тейк-профит
        stop_loss, take_profit = calculate_stop_loss_take_profit(current_price, atr_value)

        # Стратегия принятия решения
        buy_signal = current_rsi < rsi_buy and current_price > current_sma and current_macd > 0
        sell_signal = current_rsi > rsi_sell and current_price < current_sma and current_macd < 0

        if buy_signal:
            send_telegram(f"📈 BUY Signal: Цена {current_price:.2f}, RSI={current_rsi:.2f}, MACD={current_macd:.2f}")
            order = open_order('BUY', current_price)
            send_telegram(f"📉 Стоп-лосс: {stop_loss:.2f}, Тейк-профит: {take_profit:.2f}")

        elif sell_signal:
            send_telegram(f"📉 SELL Signal: Цена {current_price:.2f}, RSI={current_rsi:.2f}, MACD={current_macd:.2f}")
            order = open_order('SELL', current_price)
            send_telegram(f"📈 Стоп-лосс: {stop_loss:.2f}, Тейк-профит: {take_profit:.2f}")

        else:
            print("⏳ No signal. Watching...")

    except Exception as e:
        print(f"Ошибка: {e}")

    time.sleep(15 * 60)  # Проверка каждый 15 минут
    markets = exchange.load_markets()
    print('BTC/USDT' in markets)  # должно быть True
