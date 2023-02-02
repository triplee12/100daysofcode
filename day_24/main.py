#!/usr/bin/env python3
"""Mail merging program"""

REMOVE_WORD = "[name]"

with open("./input/names/invited_names.txt", mode="r") as invited:
    invited_n = invited.readlines()


with open("./input/letters/starting_letter.txt", mode="r") as file:
    content = file.read()
    for name in invited_n:
        s_name = name.strip()
        letter = content.replace(REMOVE_WORD, s_name)
        with open(f"./output/readyToSend/{s_name}.txt", mode="w") as invited_name:
            invited_name.write(letter)

