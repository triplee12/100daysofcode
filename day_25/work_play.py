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
#print(pd_data["temp"])
#data_to_dict = pd_data.to_dict()
#print(data_to_dict)

#total = 0
#data_to_list = pd_data["temp"].to_list()

#for i in data_to_list:
#    total += i

# Get the average temperature
#average = total / len(data_to_list)

average = pd_data["temp"].mean()
print(average)

maximum = pd_data["temp"].max()
print(maximum)

day_with_highest_temp = pd_data[pd_data.temp == pd_data.temp.max()]

print(day_with_highest_temp)

# Get Monday temp and convert it to fahrenheit
monday_data = pd_data[pd_data.day == "Monday"]
monday_temp = monday_data.temp

# Convert the temp
fahrenheit = (monday_temp * 1.8) + 32
print(fahrenheit)
