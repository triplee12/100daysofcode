#!/usr/bin/env python3
"""Paddle module for pong game"""
from turtle import Turtle


class Paddle(Turtle):
    """Paddles the pong ball. It moves up and down using onkey 
    press.
    Args:
        side (tuple): side of the paddle. Example (350, 0) for right
        and (-350, 0) for left
    """

    def __init__(self, side:(tuple)):
        super().__init__()
        self.penup()
        self.color("#fff")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.shape("square")
        self.side = self.goto((side))

    def go_up(self):
        """Moves the paddle up when press up arrow key"""
        paddle_y = self.ycor() + 20
        self.goto(self.xcor(), paddle_y)

    def go_down(self):
        """Moves the paddle up when press up arrow key"""
        paddle_y = self.ycor() - 20
        self.goto(self.xcor(), paddle_y)

    def right_side(self):
        """Moves the paddle at the right, up and down using onkey 
        press 'Up' arrow key and 'Down' arrow key
        """

        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_down, "Down")

    def left_side(self):
        """Moves the paddle at the left up and down using 
        onkey press 'w' and 's'
        """
        self.screen.onkey(self.go_up, "w")
        self.screen.onkey(self.go_down, "s")
