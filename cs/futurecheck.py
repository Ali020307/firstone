import ccxt
import pandas as pd

# Настройка подключения к Binance Futures
exchange = ccxt.binance({
    'enableRateLimit': True,
    'options': {'defaultType': 'future'},  # ВАЖНО: для фьючерсов
})

# Загружаем рынки и проверяем наличие символа
markets = exchange.load_markets()
symbol = 'BTC/USDT'

if symbol not in markets:
    print(f"Символ {symbol} не найден на фьючерсах Binance.")
    exit()

# Параметры
timeframe = '15m'
limit = 50

# Получаем данные
try:
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    print(df.tail())
except Exception as e:
    print(f"Ошибка при получении свечей: {str(e)}")
