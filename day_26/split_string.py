#!/usr/bin/env python3
"""Split string and convert it to dictionary"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_sen = sentence.split(" ")
result = {word:len(word) for word in list_sen}
print(result)
