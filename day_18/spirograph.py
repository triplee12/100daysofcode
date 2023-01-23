#!/usr/bin/python3
"""Draw a spirograph"""
from turtle import Screen, Turtle
import random

spiro = Turtle()
colors = ["#598234", "#003b46", "#07575b", "#aebd38", "#68829e", "#505160", "#a43820", "#ba5536", "#693d3d", "#46211a", "#90afc5", "#763626", "#2a3132", "#336b87", "#80bd9e", "#89da59", "#ff420E"]

for i in range(35):
    spiro.color(random.choice(colors))
    spiro.forward(10)
    spiro.rt(10)
    spiro.circle(45)
    spiro.distance(45, 180)

screen = Screen()
screen.exitonclick()
