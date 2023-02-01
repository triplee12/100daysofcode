#!/usr/bin/env python3
"""Main module of turtle crossing the road"""
from turtle import Screen
from cars_manager import CarsManager
from player import Player
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.screensize(600, 600)
screen.tracer(0)
t_player = Player()
car = CarsManager()
score = ScoreBoard()
screen.listen()
screen.onkey(t_player.go_up, "Up")
screen.onkey(t_player.go_down, "Down")
screen.onkey(t_player.go_left, "Left")
screen.onkey(t_player.go_right, "Right")

is_on = True

while is_on:
    time.sleep(0.1)
    screen.update()
    car.move()
    car.create_cars()

    if t_player.ycor() > 240:
        time.sleep(0.2)
        screen.update()
        score.update_score()

screen.exitonclick()
