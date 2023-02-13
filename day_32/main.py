#!/usr/bin/python3
"""Birthday email sender"""
import smtplib

reciever = "reciever@example.com"
sender = "sender@example.com"
password = "yourpassword"

with smtplib.SMTP("smtp.gmail.com") as connect:
    connect.starttls()
    connect.login(user=sender, password=password)
    connect.sendmail(from_addr=sender, to_addrs=reciever, msg="subject: Hello!\n\nBody of message.")
