#!/usr/bin/python3
"""Stock Market Tracking"""
import os
import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

headers = {
    "accepts": "application/json"
}

NEWS_API_KEY = os.environ["NEWS_API_KEY"]
STOCK_API_KEY = os.environ["STOCK_API_KEY"]

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "5min",
    "apikey": STOCK_API_KEY
}

news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "language": "en",
    "sortBy": "publishedAt"
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Retrieve stock
get_stock = requests.get(STOCK_ENDPOINT, headers=headers, params=stock_params)
stock_data = get_stock.json()["Time Series (Daily)"]

stock_list = [v for k, v in stock_data.items()]
stock = stock_list[0:2]

# Yesterday
yesterday_close = float(stock[0]['4. close'])

# The day before yesterday
day_before_close = float(day_before[1]['4. close'])

# Check for positive difference between yesterday and the day before yesterday stock
positive_diff = round(yesterday_close - day_before_close, 2)

if int(positive_diff) > 5:
    # Get latest news of the stock
    get_news = requests.get(NEWS_ENDPOINT, headers=headers, params=news_params)
    news_data = get_news.json()
    news_list = [(k, v) for k, v in news_data.items()]
    news = news_list[1:3][1][1][:4]

    # Send notification
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    for new in news:
        message = client.messages.create(
                body=f"{STOCK_NAME}: 🔺{positive_diff}%\n{new['title']}\n{new['content']}",
            from_="+18000000000",
            to="+200000000000"
        )
        print(message.sid)
