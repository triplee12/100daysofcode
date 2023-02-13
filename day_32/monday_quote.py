#!/usr/bin/python3
"""Monday quote email sender"""
import smtplib
import datetime
import random

with open("quotes.txt", mode="r", encoding="utf-8") as data:
    data_list = data.readlines()

date_time = datetime.datetime.now()
year = date_time.year
month = date_time.month
weekday = date_time.weekday()

reciever = "reciever@example.com"
sender = "sender@example.com"
password = "yourpassword"

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=sender, password=password)
        quote = random.choice(data_list).replace('\"', "")
        connect.sendmail(from_addr=sender, to_addrs=reciever, msg=f"subject: Morning Quote\n\n{quote}.")
