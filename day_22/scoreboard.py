#!/usr/bin/env python3
"""Scoreboard module"""
from turtle import Turtle


class ScoreBoard(Turtle):
    """Keeps the track of the players scores"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("#fff")
        self.right_score = 0
        self.left_score = 0
        self.goto(0, 260)
        self.write(f"{self.left_score} : {self.right_score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def update_rscore(self):
        """Updates the player's score"""
        self.right_score += 1
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", align="center", font=("Arial", 24, "normal"))

    def update_lscore(self):
        """Updates the player's score"""
        self.left_score += 1
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 12, "normal"))
