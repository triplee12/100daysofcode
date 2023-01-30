#!/usr/bin/env python3
"""Paddle module for pong game"""
from turtle import Turtle

X_POS = 350 # y position of the paddle on canvas
Y_POS = 0 # x position of the paddle on canvas
UP = 90
DOWN = 270

class Paddle(Turtle):
    """Paddles the pong ball. It moves up and down using onkey 
    press.
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("#fff")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.shape("square")
        self.goto(X_POS, Y_POS)

    def go_up(self):
        """Moves the paddle up when press up arrow key"""
        paddle_y = self.ycor() + 20
        self.goto(self.xcor(), paddle_y)

    def go_down(self):
        """Moves the paddle up when press up arrow key"""
        paddle_y = self.ycor() - 20
        self.goto(self.xcor(), paddle_y)

    def move(self):
        """Moves the paddle up and down using onkey press"""

        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_down, "Down")
