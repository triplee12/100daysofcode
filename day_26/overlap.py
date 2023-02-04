#!/usr/bin/env python3
"""Filter common number from two list"""

with open("number1.txt", mode="r") as number1:
    num1 = number1.readlines()

with open("number2.txt", mode="r") as number2:
    num2 = number2.readlines()

result = [int(common.strip()) for common in num1 if common in num2]
print(result)
