#!/usr/bin/python3
"""Drawing different shapes"""
from turtle import Screen, Turtle

shape = Turtle()


def shapes():
    """Draws different shapes"""
    # Draw triangle
    for i in range(3):
        shape.forward(120)
        shape.rt(120)

    # Draw square
    for i in range(4):
        shape.forward(120)
        shape.rt(90)

    # Draw Pentagon
    for i in range(5):
        shape.forward(120)
        shape.rt(72)

    # Draw hexagon
    for i in range(6):
        shape.forward(120)
        shape.rt(60)

    # Draw heptagon
    for i in range(7):
        shape.forward(120)
        shape.rt(51.43)

    # Draw octagon
    for i in range(8):
        shape.forward(120)
        shape.rt(45)

    # Draw nonagon
    for i in range(9):
        shape.forward(120)
        shape.rt(40)

    # Draw decagon
    for i in range(10):
        shape.forward(120)
        shape.rt(36)

shapes()
screen = Screen()
screen.exitonclick()
