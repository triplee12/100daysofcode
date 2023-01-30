#!/usr/bin/env python3
"""Main module of pong game"""
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.tracer(0)
screen.title("Advance Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("#000")
screen.listen()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
is_on = True

while is_on:
    screen.update()
    right_paddle.right_side()
    left_paddle.left_side()

screen.exitonclick()
