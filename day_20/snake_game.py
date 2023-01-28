#!/usr/bin/env python3
"""Snake game"""
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("#c3c3a2")
screen.title("Anaconda")
screen.tracer(0)
positions = [(-40, 0), (-20, 0), (0, 0)]
game_level = [("easy", 10), ("hard", 5), ("harder", 0)]
snakes = []

for i in range(3):
    snake = Turtle(shape="square")
    snake.penup()
    snake.goto(positions[i])
    snakes.append(snake)

is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    for move in range(len(snakes) - 1, 0, -1):
        pos_x = snakes[move - 1].xcor()
        pos_y = snakes[move - 1].ycor()
        snakes[move].goto(pos_x, pos_y)
    snakes[0].forward(20)

screen.exitonclick()
