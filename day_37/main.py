#!/usr/bin/python3
"""Habit Tracking"""
import requests
from datetime import datetime

USERNAME = "blockdev"
TOKEN = "blockdev147"

# User
pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "accepts": "application/json"
}

params = {
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "great project"
}

user_reg = requests.post(url=pixela_endpoint, headers=headers, json=params)
user_res = user_reg.json()

# Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graph"
graph_params = {
    "id": "test-graph", "name": "graph-name",
    "unit": "commit", "type": "int",
    "color": "shibafu", "timezone": "WAT",
    "isSecret": True, "publishOptionalData": True
}
graph_headers = {"X-USER-TOKEN": TOKEN}
graph_reg = requests.post(url=graph_endpoint, headers=graph_headers, json=graph_params)
graph_res = graph_reg.json()

# Pixel
today = datetime.now()
pixel_endpoint = f"{graph_endpoint}/{graph_params.id}"
pixel_params = {"date": today.strftime("%Y%m%d"), "quantity":"5"}
post_pixel = requests.post(url=pixel_endpoint, headers=graph_headers, json=pixel_params)
pixel_res = post_pixel.json()

# Update pixel
put_pixel = f"{pixel_endpoint}/20230427"
pixel = requests.put(url=put_pixel, headers=graph_headers, json={"quantity":"5"})
put_res = pixel.json()

# Delete pixel
del_pixel = f"{pixel_endpoint}/20230427"
to_del = reqquests.delete(url=del_pixel, headers=graph_headers)
print(to_del.json())
