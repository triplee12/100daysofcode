#!/usr/bin/python3
import random

"""Picking a random word, checking answers and replace the blank with the
correct answer at the corresponding index with letter.

And keep track of the player to determine if he/she lose or win.
"""
word_list = ["ardvark", "baboon", "camel"]
hangman = [
        '''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 jgs_|___''',
 '''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 jgs_|___''',
 '''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 jgs_|___''',
 '''
       _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 jgs_|___''',
 '''
       _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 jgs_|___''',
 '''
       _______
     |/      |
     |      
     |      
     |       
     |      
     |
 jgs_|___'''
        ]
lives = 6

chosen_word = random.choice(word_list)
blank = "-" * len(chosen_word)
display = list(blank)
while("-" in display and lives != 0):
    print(display)
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for letter in chosen_word:
            for i in range(0, len(chosen_word)):
                if letter == guess and chosen_word[i] == letter:
                    display[i] = guess
    else:
        lives = lives - 1
        print(hangman[lives])

if display == list(chosen_word):
    print("You win!")
else:
    print("Opps you lose!")
