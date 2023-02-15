#!/usr/bin/python3
"""Sunrise sunset api request"""
import requests
import smtplib
import time
from datetime import datetime

parameters = {
        "lat": 203.24,
        "lng": -240.1,
        "formatted": 0
}

headers = {'Accept': 'application/json'}

def is_iss():
    """
    Check for the iss lat and lng 
    Then compare with my current location
    Return: True
    """
    global headers
    res = requests.get(url="http://api.open-notify.org/iss-now.json", headers=headers)
    res.raise_for_status()
    data = res.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])
    my_lat = float(parameters["lat"])
    my_lng = float(parameters["lng"])

    if my_lat -5 <= iss_lat <= my_lat + 5 and my_lng - 5 <= iss_lng <= my_lng + 5:
        return True

def is_night():
    """
    Check if it's night and return True
    """
    global headers, parameters
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, headers=headers)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time = datetime.now().hour

    if sunset >= int(time) or sunrise <= int(time):
        return True

while True:
    i = 0
    time.sleep(60)
    print(i + 1)
    if is_iss() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as send_mail:
            send_mail.starttls()
            send_mail.login("me@gmail.com", "hello")
            message = "Look up"
            send_mail.sendmail(to_addr="me@gmail.com", to_addrs="me@gmail.com", msg=f"subject:Iss Location\n\n{message}")
