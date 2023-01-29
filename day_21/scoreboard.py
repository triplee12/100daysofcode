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
        self.goto(0, 300)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))
        self.hideturtle()

    def update_score(self):
        """Updates the player's score"""
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 12, "normal"))


