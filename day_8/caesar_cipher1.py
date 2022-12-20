#!/usr/bin/python3
import string
"""Caesar cipher encryption"""
alphabet = list(string.ascii_letters.lower())

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted = ""
    for i in text:
       encrypted += alphabet[shift]
       shift += 1
    print(encrypted)

encrypt(text, shift)

