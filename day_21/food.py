#!/usr/bin/env python3
"""Detect collisions with food"""
from turtle import Turtle
import random


class Food(Turtle):
    """Snake's food inherits from Turtle class"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Refreshes the food position on the canvas"""
        dist_x = random.randint(-315, 315)
        dist_y = random.randint(-315, 315)
        self.goto(dist_x, dist_y)
