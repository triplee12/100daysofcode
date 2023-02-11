#!/usr/bin/env python3
"""Error handling: IndexError"""

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    """Make pie"""
    try:
        fruit = fruits[index]
    except IndexError as error_message:
        print(f"Sorry no fruits pie for you.")
    else:
        print(fruit + " pie")

make_pie(4)
