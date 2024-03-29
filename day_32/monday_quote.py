#!/usr/bin/python3
"""Monday quote email sender"""
import smtplib
import datetime
import random

with open("quotes.txt", mode="r", encoding="utf-8") as data:
    data_list = data.readlines()

date_time = datetime.datetime.now()
weekday = date_time.weekday()

receiver = "receiver@example.com"
sender = "sender@example.com"
password = "yourpassword"

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=sender, password=password)
        quote = random.choice(data_list).replace('\"', "")
        connect.sendmail(from_addr=sender, to_addrs=receiver, msg=f"subject: Morning Quote\n\n{quote}.")
