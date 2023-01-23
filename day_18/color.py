#!/usr/bin/python3
"""Create random colors using (r, g, b) : red, green, blue"""
import random


def random_color():
    """Creates random color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
