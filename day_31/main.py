#!/usr/bin python3
"""Flash card"""
import pandas as pd
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

rand_word = {}
to_learn = {}

try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    """
    Next card
    """
    global rand_word, timer
    window.after_cancel(timer)
    rand_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="#B1DDC6")
    canvas.itemconfig(card_word, text=rand_word["French"], fill="#B1DDC6")
    canvas.itemconfig(card_bg, image=card_front)
    timer = window.after(5000, func=flip_card)

def flip_card():
    """
    Flip card
    """
    global rand_word
    canvas.itemconfig(card_title, text="English", fill="#fff")
    canvas.itemconfig(card_word, text=rand_word["English"], fill="#fff")
    canvas.itemconfig(card_bg, image=card_back)

def is_known():
    """
    Remove item from list and call the next item
    """
    to_learn.remove(rand_word)
    data1 = pd.DataFrame(to_learn)
    data1.to_csv("data/word_to_learn.csv", index=False)
    next_card()

# Window configuration
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(5000, func=flip_card)

# Canvas configuration
canvas = Canvas()
canvas.config(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 100, text="Title", font=("Arial", 35, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button configuration
right = PhotoImage(file="images/right.png")
right_btn = Button(image=right, bg=BACKGROUND_COLOR, width=100, height=100, highlightthickness=0, command=is_known)
right_btn.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong, bg=BACKGROUND_COLOR, width=100, height=100, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

next_card()

window.mainloop()
