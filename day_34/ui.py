#!/usr/bin/python3
"""Quiz interface model"""
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizGUI:
    """Quiz graphical user interface"""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivial Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score: 0", fg="#fff", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="#fff")
        self.quiz_txt = self.canvas.create_text(150, 125, text="Quiz", width=280, font=("Arial", 20, "italic"), fill="#000")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        truebtn = PhotoImage(file="images/true.png")
        self.true = Button(image=truebtn, highlightthickness=0, command=self.is_true)
        self.true.grid(column=0, row=2)
        falsebtn = PhotoImage(file="images/false.png")
        self.false = Button(image=falsebtn, highlightthickness=0, command=self.is_false)
        self.false.grid(column=1, row=2)
        self.get_next_quiz()
        self.window.mainloop()

    def get_next_quiz(self):
        self.canvas.config(bg="#fff")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_txt, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_txt, text="You've reached the end of the quiz.")
            self.true.config(state="disable")
            self.false.config(state="disable")

    def is_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right == True:
            self.canvas.config(self.canvas, bg="#00ff00")
        else:
            self.canvas.config(self.canvas, bg="#ff0000")
        self.window.after(1000, self.get_next_quiz)
