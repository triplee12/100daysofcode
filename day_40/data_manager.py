#!/usr/bin/python3
"""DataManager module"""
import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = YOUR ENDPOINT HERE


class DataManager:
    """DataManager class"""

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Get data from the sheety api endpoint"""
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        """Update data in google sheet"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
