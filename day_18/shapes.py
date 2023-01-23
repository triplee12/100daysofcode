#!/usr/bin/python3
"""Drawing different shapes"""
from turtle import Screen, Turtle

shape = Turtle()


def shapes(side_size, color):
    """Draws different shapes
    Args:
        side_size (int): size of each shape
        color (str): color of the shape line
    """
    size = 360 / side_size

    for i in range(side_size):
        shape.forward(120)
        shape.rt(size)
        shape.color(color)

colors = ["#0000FF", "#EEEE3B", "#45458B", "purple", "red", "green", "pink", "black"]

for i in range(3, 11):
    color = colors[i - 3]
    shapes(i, color)

screen = Screen()
screen.exitonclick()
