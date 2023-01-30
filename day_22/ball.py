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
        self.move_fast = 0.1
        self.x_cor = 10
        self.y_cor = 10

    def move(self):
        """Move the ball from one angle to another"""
        xpos = self.xcor() + self.x_cor
        ypos = self.ycor() + self.y_cor
        self.goto(xpos, ypos)

    def x_bounce(self):
        """Bounces the ball from 'x' position to '-x' position"""
        self.x_cor *= -1
        self.move_fast *= 0.2

    def y_bounce(self):
        """Bounces the ball from 'y' position to '-y' position"""
        self.y_cor *= -1

    def reset_time(self):
        self.move_fast = 0.1
