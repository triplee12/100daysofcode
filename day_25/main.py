#!/usr/bin/env python3
"""Read csv file using pandas library"""
#import csv
import pandas as pd

#with open("weather-data.csv", mode="r") as file:
#    data = csv.reader(file)
#    temperature = []
#    for datu in data:
#        if datu[1] == "temp":
#            continue
#        else:
#            temperature.append(int(datu[1]))
#    print(temperature)

pd_data = pd.read_csv("weather-data.csv")
print(pd_data["temp"])
