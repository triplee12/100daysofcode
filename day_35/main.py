#!/usr/bin/python3
"""Weather app"""
import requests
import os
from twilio.rest import Client

headers = {"Accepts": "Application/json"}
parameters = {
        "lat": 24.2302,
        "lon": -2.2334,
        "exclude": "current,minutely,daily",
        "appid": ""
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters, headers=headers)
response.raise_for_status()

weather_data = response.json()["hourly"][:12]
will_rain = False

for h_data in weather_data:
    weather_id = h_data["weather"][0]["id"]

    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    msg = "Bring an umbrella"
    account_sid = ""
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    message = client.messages.create(
            body=msg,
            from_="",
            to=""
    )

    print(message.sid)
