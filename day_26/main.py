#!/usr/bin/env python3
"""NATO alphabet"""
import pandas as pd

# Convert to pandas dataframe
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
# convert to dictionary
nato_data_dict = {row.letter:row.code for index, row in nato_data.iterrows()}

user_input = input("Enter a word: ").upper()
while KeyError:
    try:
        # Split user input into list of letters
        user_list = [alphabet for alphabet in user_input]
        # Use the letter to access values from nato_data_dict
        nato_code = [nato_data_dict[letter] for letter in user_list]
    except KeyError:
        print("Only alphabetical words, please")
        user_input = input("Enter a word: ").upper()
    else:
        print(nato_code)
        break
