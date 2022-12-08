#!/usr/bin/python3
#!/bin/env/python3
"""Day 2 final project: Tip calculator"""
print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
current_bill = float(bill)
pay_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

percent = pay_percent / 100
total = current_bill * percent
total += current_bill
tip = total / split
print(f"Each person should pay: ${tip:.2f}")
