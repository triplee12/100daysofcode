#!/usr/bin/python3
"""Drawing different shapes"""
from turtle import Screen, Turtle

shape = Turtle()


def shapes(side_size):
    """Draws different shapes
    Args:
        side_size (int): size of each shape
    """
    size = 360 / side_size

    for i in range(side_size):
        shape.forward(120)
        shape.rt(size)

for i in range(3, 11):
    shapes(i)

screen = Screen()
screen.exitonclick()
