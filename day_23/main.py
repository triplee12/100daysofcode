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

    #Detect when the turtle reach the positive y-axis
    if t_player.ycor() > 240:
        screen.update()
        score.update_score()
        t_player.goto(0, -270)
        car.increase_speed()

    #Detect when the turtle collide with a car
    for ca in car.cars:
        if ca.distance(t_player) < 29:
            score.game_over()
            is_on = False

screen.exitonclick()
