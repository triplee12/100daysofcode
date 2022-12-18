#!/usr/bin/python3
import random

"""Picking a random words and checking answers"""
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("True")
    else:
        print("False")
