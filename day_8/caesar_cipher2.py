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

def encrypt(text, shift):
    encrypted = ""
    for i in text:
       position = alphabet.index(i)
       position += shift
       encrypted += alphabet[position]
    print(f"Your encoded text is: {encrypted}")

def decrypt(text, shift):
    decrypted = ""
    for i in text:
        position = alphabet.index(i)
        position -= shift
        decrypted += alphabet[position]
    print(f"Your decoded text is: {decrypted}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print(f"Unknown command {direction}")
