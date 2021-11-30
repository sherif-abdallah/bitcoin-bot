import requests
import time

# global variables
api_key = 'XXXXXXXXXX' # You Can Get API Key From https://coinmarketcap.com/api
bot_key = 'XXXXXXXXXX' # You Can Get bot key from This Telegram bot @BotFather https://web.telegram.org/z/#93372553
chat_id = 'XXXXXXXXXX' # You Can Get Your Chat ID from This Telegram bot @GetIDBotbot https://web.telegram.org/z/#1115273825

limit = 59000 # This is The Limit of The Bitcoin To Send The Message
time_interval = 5 * 60 # Sending Message All 5 Minutes

def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest" # For More Details Take a look for the documentation https://coinmarketcap.com/api/documentation/v1#section/Quick-Start-Guide

    parameters = {
        'start': '1',
        'limit': '2',
        'convert': 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price

def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def main():
    while True:
        price = get_price()
        if price < limit:
            send_update(chat_id, f"The BitCoin Price Updated To : {price}")
        time.sleep(time_interval)

main()