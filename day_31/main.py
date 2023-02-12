#!/usr/bin python3
"""Flash card"""
import pandas as pd
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_card():
    rand_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=rand_word["French"])

# Window configuration
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas configuration
canvas = Canvas()
canvas.config(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 100, text="Title", font=("Arial", 35, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button configuration
right = PhotoImage(file="images/right.png")
right_btn = Button(image=right, bg=BACKGROUND_COLOR, width=100, height=100, highlightthickness=0, command=next_card)
right_btn.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong, bg=BACKGROUND_COLOR, width=100, height=100, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

next_card()

window.mainloop()
