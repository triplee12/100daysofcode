#!/usr/bin/python3
#!/bin/env/python3
"""Mathematical operators in python"""
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
new_height = float(height)
new_weight = int(weight)
result = new_weight / (new_height**2)
print(int(result))
