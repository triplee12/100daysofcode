#!/usr/bin/env python3
"""Snake game main module"""
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=650, height=650)
screen.bgcolor("#c3c3a2")
screen.title("Anaconda")
screen.tracer(0)
game_level = [("easy", 10), ("hard", 5), ("harder", 0)]
fd = Food()
snake = Snake()
score = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_on = True

while is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(fd) < 15:
        fd.refresh()
        snake.extends_()
        score.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 315 or snake.head.xcor() < -315 or snake.head.ycor() > 315 or snake.head.ycor() < -315:
        score.game_over()
        is_on = False

    # Detect collision with any part of the snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_on = False
            score.game_over()

screen.exitonclick()
