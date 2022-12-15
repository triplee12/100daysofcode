#!/usr/bin/python3
#!/bin/env/python3

"""Nested if-else (elif) condition"""
weight = input("Enter your weight in km: ")
current_weight = float(weight)
height = input("Enter your height in m: ")
current_height = float(height)

bmi = current_weight / (current_height ** 2)

if bmi < 18.5:
    print("Your BMI is {:.2f}, you're underweight.".format(bmi))
elif bmi < 25.0:
    print("Your BMI is {:.2f}, normal weight.".format(bmi))
elif bmi < 30.0:
    print("Your BMI is {:.2f}, you're slightly overweight.".format(bmi))
elif bmi < 35.0:
    print("Your BMI is {:.2f}, you're obese.".format(bmi))
else:
    print("Your BMI is {:.2f}, you're clinically obese.".format(bmi))
