#!/usr/bin/python3
"""Draw a spirograph"""
from turtle import Screen, Turtle
from color import random_color
import turtle as t
import random

spiro = Turtle()
t.colormode(255)
spiro.speed(0)

for i in range(int(360 / 5)):
    spiro.color(random_color())
    spiro.circle(45)
    spiro.setheading(spiro.heading() + 5)

screen = Screen()
screen.exitonclick()
