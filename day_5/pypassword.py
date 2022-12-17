#!/usr/bin/python3
#!/bin/env/python3
import random
"""PyPassword Generator"""
print("Welcome to the PyPasswrd Generator!")
letter = int(input("How many letters would you like in your password?\n"))
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

number = int(input("How many numbers would you like in your password?\n"))

symbols = ['"', '/', '>', '.', '<', '[', '{', ']', '}', '?', ';', ':' "'",
        '|', ')', '(', '_', '-', '*', '&', '^', '%', '$', '#', '@', '!', '~'
        ]
symbol = int(input("How many symbols would you like in your password?\n"))
password = []

for l in range(letter):
    ch = random.choice(letters)
    password.append(ch)

for n in range(number):
    pn = random.choice(numbers)
    password.append(pn)

for s in range(symbol):
    sym = random.choice(symbols)
    password.append(sym)

random.shuffle(password)
print(''.join(password))
