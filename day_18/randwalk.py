#!/usr/bin/python3
"""Random walk challenge"""
from turtle import Screen, Turtle
import random

walk = Turtle()
walk.pensize(5)
walk.speed(0)

moves = [0, 90, 180, 270]
colors = ["#598234", "#003b46", "#07575b", "#aebd38", "#68829e", "#505160", "#a43820", "#ba5536", "#693d3d", "#46211a", "#90afc5", "#763626", "#2a3132", "#336b87", "#80bd9e", "#89da59", "#ff420E"]


def random_walk():
    for i in range(1000):
        walk.color(random.choice(colors))
        walk.forward(45)
        walk.setheading(random.choice(moves))


random_walk()
screen = Screen()
screen.exitonclick()
