#!/usr/bin/env python3
"""Scoreboard module"""
from turtle import Turtle


class ScoreBoard(Turtle):
    """Dynamically updates the player's score"""

    def __init__(self):
        super().__init__()
        self.color("black")
        self.score = 0
        self.goto(0, 300)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """Updates the player's score"""
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))


