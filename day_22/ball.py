#!/usr/bin/env python3
"""Pong ball module"""
from turtle import Turtle


class Ball(Turtle):
    """Pong ball"""
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("#fff")

    def move(self):
        """Move the ball from one angle to another"""
        xpos = self.xcor() + 10
        ypos = self.ycor() + 10
        self.goto(xpos, ypos)
