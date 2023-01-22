#!/usr/bin/python3
"""Draw dashed line challenge"""
from turtle import Turtle, Screen

dashed = Turtle()
dashed.ht()

for i in range(20):
    dashed.forward(5)
    dashed.up()
    dashed.forward(5)
    dashed.down()

screen = Screen()
screen.exitonclick()
