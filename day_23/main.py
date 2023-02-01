#!/usr/bin/env python3
"""Main module of turtle crossing the road"""
from turtle import Screen
import time

screen = Screen()
screen.screensize(600, 600)
screen.tracer()


is_on = True

while is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
