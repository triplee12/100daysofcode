#!/usr/bin/python3
"""Quiz interface model"""
from tkinter import *

THEME_COLOR = "#375362"


class QuizGUI:
    """Quiz graphical user interface"""
    def __init__(self):
        self.window = Tk()
        self.window.title("Trivial Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score: 0", fg="#fff", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="#fff")
        self.quiz = self.canvas.create_text(150, 125, text="Quiz", width=250, font=("Arial", 20, "italic"), fill="#000")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        truebtn = PhotoImage(file="images/true.png")
        self.true = Button(image=truebtn, highlightthickness=0)
        self.true.grid(column=0, row=2)
        falsebtn = PhotoImage(file="images/false.png")
        self.false = Button(image=falsebtn, highlightthickness=0)
        self.false.grid(column=1, row=2)
        self.window.mainloop()
