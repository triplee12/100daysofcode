#!/usr/bin/python3
#!/bin/env/python3
"""Treasure Island"""
print("Welcome to Treasure Island. Your mission is to find the treasure.")
move = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
if move.lower() == "left":
    lake = input("There is lake in your front. swim or wait ")
    if lake.lower() == "wait":
        color = input("Which color? red, blue or yellow ")
        if color.lower() == "yellow":
            print("You win!")
        elif color.lower() == "red":
            print("You're consume by fire. Game over!")
        elif color.lower() == "blue":
            print("Fake treasure. Game over!")
    elif lake.lower() == "swim":
        print("You're drown. Game over!")
elif move.lower() == "right":
    print("You fell into a hole. Game over!")
