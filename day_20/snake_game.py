#!/usr/bin/env python3
"""Snake game"""
from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("#c3c3a2")
screen.title("Anaconda")
screen.tracer(0)
positions = [(-40, 0), (-20, 0), (0, 0)]
game_level = [("easy", 10), ("hard", 5), ("harder", 0)]

snake = Snake()

is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
