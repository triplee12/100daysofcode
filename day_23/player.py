#!/usr/bin/env python3
"""Player module"""
from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player(Turtle):
    """Player module"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(1.2, 1.2)
        self.color("brown")
        self.goto(0, -260)
        self.setheading(90)

    def go_up(self):
        self.setheading(UP)
        self.forward(20)

    def go_down(self):
        self.setheading(DOWN)
        self.forward(20)

    def go_right(self):
        self.setheading(RIGHT)
        self.forward(20)

    def go_left(self):
        self.setheading(LEFT)
        self.forward(20)

    def move(self):
        self.forward(20)
