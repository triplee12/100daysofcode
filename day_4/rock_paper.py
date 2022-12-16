#!/usr/bin/python3
#!/bin/env/python3
import random
"""Paper, rock and scissors game"""

paper = """88888b.  8888b. 88888b.  .d88b. 888d888 
888 "88b    "88b888 "88bd8P  Y8b888P"   
888  888.d888888888  88888888888888     
888 d88P888  888888 d88PY8b.    888     
88888P" "Y88888888888P"  "Y8888 888     
888             888                     
888             888                     
888             888  """

rock = """             888      
                       888      
                       888      
888d888 .d88b.  .d8888b888  888 
888P"  d88""88bd88P"   888 .88P 
888    888  888888     888888K  
888    Y88..88PY88b.   888 "88b 
888     "Y88P"  "Y8888P888  888 """

scissors = ''',--.
             (    )____ ___________________________
              `--'---,-'  ,.  T--------------------`-.
              ,--.---`-.  `'  |_dd____________________`>
             (    )"""" """""""""""""""""""""""""""""""
              `--' '''

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
computer = random.randint(0, 2)
if human == 0 and computer == 1:
    print(rock)
    print("Computer chose:")
    print(paper)
    print("You win")
elif human == 1 and computer == 0:
    print(paper)
    print("Computer chose:")
    print(rock)
    print("You lose")
elif human == 2 and computer == 0:
    print(scissors)
    print("Computer chose:")
    print(rock)
    print("You lose")
elif human == 0 and computer == 2:
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You win")
elif human == 2 and computer == 1:
    print(scissors)
    print("Computer chose:")
    print(paper)
    print("You win")
elif human == 1 and computer == 2:
    print(paper)
    print("Computer chose:")
    print(scissors)
    print("You lose")
elif human == computer:
    print("Draw game")
else:
    print("Game over")
