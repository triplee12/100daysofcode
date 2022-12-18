#!/usr/bin/python3
import random

"""Picking a random word, checking answers and replace the blank with the
correct answer at the corresponding index with letter.
"""
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
blank = "-" * len(chosen_word)
display = list(blank)
print(display)
while("-" in display):
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        for i in range(0, len(chosen_word)):
            if letter == guess and chosen_word[i] == letter:
                display[i] = guess
    print(display)
if display == list(chosen_word):
    print("You win!")
else:
    print("Opps you lose!")
