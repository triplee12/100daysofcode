#!/usr/bin/python3
#!/bin/env/python3
import random
"""Randomisation -  Tossing of coin"""
toss = input("Heads or Tails? ")
choice = random.randint(0, 1)
if choice == 0 and toss.capitalize() == "Heads":
    print(toss.capitalize())
elif choice == 1 and toss.capitalize() == "Tails":
    print(toss.capitalize())
else:
    print(f"Opps! It's {toss}")
