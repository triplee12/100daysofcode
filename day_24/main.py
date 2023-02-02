#!/usr/bin/env python3
"""Mail merging program"""

REMOVE_WORD = "[name]"

# Read names of the invited people
with open("./input/names/invited_names.txt", mode="r") as invited:
    invited_n = invited.readlines()

# Read content of the mail
with open("./input/letters/starting_letter.txt", mode="r") as file:
    content = file.read()
    for name in invited_n:
        s_name = name.strip() # strip off newline character and extra spaces
        letter = content.replace(REMOVE_WORD, s_name) # replace the "[name]" with invited name
        
        # Write letter to the invited names
        with open(f"./output/readyToSend/{s_name}.txt", mode="w") as invited_name:
            invited_name.write(letter)

