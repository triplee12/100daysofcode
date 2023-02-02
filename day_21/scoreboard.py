#!/usr/bin/env python3
"""Scoreboard module"""
from turtle import Turtle


class ScoreBoard(Turtle):
    """Dynamically updates the player's score"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.score = 0
        self.highest_score = 0
        self.goto(0, 300)
        self.write(f"Score: {self.score} | HighestScore: {self.highest_score}", align="center", font=("Arial", 12, "normal"))
        self.hideturtle()

    def update_score(self):
        """Updates the player's score"""
        self.clear()
        with open("highest.txt", "r") as f:
            h_score = f.read()
            self.highest_score = int(h_score)
            self.write(f"Score: {self.score} | HighestScore: {self.highest_score}", align="center", font=("Arial", 12, "normal"))

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest.txt", "w") as f:
                f.write(str(self.highest_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        """Increases the score"""
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 12, "normal"))


