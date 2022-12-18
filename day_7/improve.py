#!/usr/bin/python3
import random

"""Picking a random word, checking answers and replace the blank with the
correct answer at the corresponding index with letter.
And keep track of the player to determine if he/she lose or win.
"""

logo = '''
88
88
88
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8
                                    aa,    ,88
                                     "Y8bbdP"    '''
print(logo)

word_list = ["ardvark", "baboon", "camel", "able", "about", "account",
        "acid", "across", "act", "addition", "adjustment", "advertisement",
        "after", "again", "against", "agreement", "air", "all", "almost",
        "among", "amount", "amusement", "and", "angle", "angry", "animal",
        "answer", "ant", "any", "apparatus", "awake", "baby", "back", "bad",
        "bag", "balance", "ball", "band", "base", "basin", "basket", "bath",
        "be", "beautiful", "because", "bed", "bee", "before", "behaviour",
        "by", "cake", "camera", "canvas", "card", "care", "carriage",
        "cart", "cat", "cause", "danger", "dark", "daughter", "day", "dead",
        "Android"]

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
print(display)

while("-" in display and lives != 0):
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for letter in chosen_word:
            for i in range(0, len(chosen_word)):
                if letter == guess and chosen_word[i] == letter:
                    display[i] = guess
    else:
        lives = lives - 1
        print(hangman[lives])

    print(display)

if display == list(chosen_word):
    print("You win!")
else:
    print("Opps you lose!")
