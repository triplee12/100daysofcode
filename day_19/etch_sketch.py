#!/usr/bin/env python3
"""Etch a sketch"""
from turtle import Screen, Turtle

etch = Turtle()
etch.speed(0)
screen = Screen()
screen.listen()


def go_forward():
    """Move the turtle forward"""
    etch.forward(20)


def go_backward():
    """Move the turtle backward"""
    etch.backward(20)


def counter_clockwise():
    """Turns the turtle counter clockwise"""
    etch.lt(20)


def clockwise():
    """Turns the turtle clockwise"""
    etch.rt(20)


def clear_drawing():
    """Clears all the images on the turtle's canvas"""
    etch.clear()
    screen.reset()


if __name__ == "__main__":
    # move turtle forward
    screen.onkey(go_forward, "w")
    # move turtle backward
    screen.onkey(go_backward, "s")
    # go left
    screen.onkey(counter_clockwise, "a")
    # go right
    screen.onkey(clockwise, "d")
    # clear screen
    screen.onkey(clear_drawing, "c")
    # close the window
    screen.exitonclick()
