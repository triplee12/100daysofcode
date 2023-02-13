#!/usr/bin/python3
"""Birthday email automation"""
import smtplib
import datetime
import pandas as pd
import random

REMOVE_WORD = "[NAME]"
REMOVE_ANG = "Angela"

# Update the birthdays.csv
add_to_csv = {
        "name": ["Uncle"],
        "email": ["their@me.com"],
        "year": [2023.0],
        "month": [2.0],
        "day": [13.0]
}
df = pd.DataFrame(add_to_csv)
df.to_csv("birthdays.csv", mode='a', index=False, header=False)
data = pd.read_csv("birthdays.csv")
birth_dct = data.to_dict(orient="records")

# Check if today matches a birthday in the birthdays.csv
date = datetime.datetime.now()
month = date.month
day = date.day

for i in range(len(birth_dct)):
    if month == int(birth_dct[i]["month"]) and day == int(birth_dct[i]["day"]):

        templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        to_use = random.choice(templates)

        with open(f"letter_templates/{to_use}", mode="r") as birth_t:
            content = birth_t.read()
            message = content.replace(REMOVE_WORD, birth_dct[i]["name"])
            message = message.replace(REMOVE_ANG, "Blockdev")

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="me@gmail.com", password="mypass")
                connection.send(from_addr="me@gmail.com", to_addrs="receive@any.com", msg="subject: Happy Birthday Wish\n\n{message}")
