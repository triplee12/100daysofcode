#!/usr/bin/python3
#!/bin/env/python3
"""String formatting"""
age = input("What is your current age? ")
current_age = int(age)
year_left  = 90 - current_age
months_left = year_left * 12
weeks_left = year_left * 52
days_left = year_left * 365
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months in your life")
