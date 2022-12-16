#!/usr/bin/python3
#!/bin/env/python3
import random
"""Banker roulette - Who will pay the bill."""
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(names[random.randint(0, len(names) - 1)])
