#!/usr/bin/env python3
"""50 states of USA game"""
from turtle import Screen
import time

screen = Screen()
screen.setup(725, 500)
screen.bgpic("blank_states_img.gif")
screen.tracer(0)

is_on = True

while is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
