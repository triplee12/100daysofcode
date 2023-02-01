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
        self.goto(0, -270)
        self.setheading(90)

    def go_up(self):
        """Sets the towards north (default) and move forward"""
        self.setheading(UP)
        self.forward(20)

    def go_down(self):
        """Sets the towards south and move forward"""
        self.setheading(DOWN)
        self.forward(20)

    def go_right(self):
        """Sets the towards east and move forward"""
        self.setheading(RIGHT)
        self.forward(20)

    def go_left(self):
        """Sets the towards west and move forward"""
        self.setheading(LEFT)
        self.forward(20)
