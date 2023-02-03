#!/usr/bin/env python3
"""Analyze squirrel population"""
import pandas as pd

data = pd.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# Get gray squirrels data and calculate the sum
gray = data[data["Primary Fur Color"] == "Gray"]
gray_sum = len(gray)

# Get black squirrels data and calculate the sum
black = data[data["Primary Fur Color"] == "Black"]
black_sum = len(black)

# Get cinnamon data and calculate the sum
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
cinn_sum = len(cinnamon)

# Convert to dictionary
primary_color = {
        "Fur Color": ["Gray", "Black", "Cinnamon"],
        "Total": [gray_sum, black_sum, cinn_sum]
}

# Convert to pandas dataframe
pri_color_csv = pd.DataFrame(primary_color)
# Save to csv
pri_color_csv.to_csv("squirrel_population.csv")
