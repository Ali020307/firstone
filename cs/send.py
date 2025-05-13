import requests

def send_telegram(text):
    token = '7633447499:AAGXYYR_A1KI8inFb6Q5lcyRBadJ48Cr2YI'
    chat_id = 282752187
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)

send_telegram("✅ Telegram бот работает!")
