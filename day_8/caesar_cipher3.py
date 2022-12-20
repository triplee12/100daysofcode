#!/usr/bin/python3
import string
"""Caesar cipher encryption"""
alphabet = list(string.ascii_letters.lower())
sysmbols = ["'", '"', ",", " ", ".", "?", "!", "@", "#", "$",
        "%", "^", "&", "*"]
alphabet.extend(sysmbols)

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(text, shift, direction):
    encrypted = ""
    decrypted = ""
    for i in text:
        position = alphabet.index(i)
        if direction == "encode":
            position += shift
            encrypted += alphabet[position]
        elif direction == "decode":
            position -= shift
            decrypted += alphabet[position]
    if direction == "encode":
        print(f"Your encoded text is: {encrypted}")
    elif direction == "decode":
        print(f"Your decoded text is: {decrypted}")

ceasar(text, shift, direction)
