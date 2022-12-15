#!/usr/bin/python3
#!/bin/env/python3
"""Love calculator"""
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your partner name? \n")
score1 = 0
score2 = 0
for i in name1.lower():
    if i in "love":
        score1 += 1
    elif i in "true":
        score1 += 1
name1_score = str(score1)
for i in name2.lower():
    if i in "love":
        score2 += 1
    elif i in "true":
        score2 += 1
name2_score = str(score2)
percent = name1_score + name2_score

if int(percent) < 10 or int(percent) > 90:
    print(f"You score is {percent}, you go together like coke and mentos")
elif int(percent) >= 40 or int(percent) <= 50:
    print(f"Your score is {percent}, you're alright together.")
else:
    print(f"Your love score is %{percent}")
