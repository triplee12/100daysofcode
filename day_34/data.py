#!/usr/bin/python3
"""Quiz data"""
import requests

parameters = {
        "amount": 10,
        "type":   "boolean"
}

headers = {'Accept': 'application/json'}

response = requests.get(url="https://opentdb.com/api.php", params=parameters, headers=headers)
response.raise_for_status()
question_data = response.json()["results"]

print(question_data)
