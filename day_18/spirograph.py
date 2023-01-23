#!/usr/bin/python3
"""Draw a spirograph"""
from turtle import Screen, Turtle
from color import random_color
import turtle as t
import random

spiro = Turtle()
t.colormode(255)
spiro.speed(0)

for i in range(35):
    spiro.color(random_color())
    spiro.forward(10)
    spiro.rt(10)
    spiro.circle(45)
    spiro.distance(0,45)

screen = Screen()
screen.exitonclick()
