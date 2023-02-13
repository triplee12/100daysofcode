#!/usr/bin/python3
"""Birthday email automation"""
import smtplib
import datetime
import pandas as pd
import random

REMOVE_WORD = "[NAME]"
REMOVE_ANG = "Angela"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
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

# 2. Check if today matches a birthday in the birthdays.csv
date = datetime.datetime.now()
year = date.year
month = date.month
day = date.day

for i in range(len(birth_dct)):
    if year == int(birth_dct[i]["year"]) and month == int(birth_dct[i]["month"]) and day == int(birth_dct[i]["day"]):

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        to_use = random.choice(templates)

        with open(f"letter_templates/{to_use}", mode="r") as birth_t:
            content = birth_t.read()
            message = content.replace(REMOVE_WORD, birth_dct[i]["name"])
            message = message.replace(REMOVE_ANG, "Blockdev")

            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user="me@gmail.com", password="mypass")
                connection.send(from_addr="me@gmail.com", to_addrs="recieve@any.com", mgs="subject: Happy Birthday Wish\n\n{message}")
