#!/usr/bin/env python3
"""Turtle race"""
from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
predict = screen.textinput(title="Turtle Race Prediction", prompt="Which turtle will win the race? Enter color")
colors = ["brown", "yellow", "blue", "purple", "red", "green", "pink", "black"]
y_pos = [-90, -70, -50, -30, -10, 10, 30, 50]
turtles = []


for i in range(0, 8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_pos[i])
    turtles.append(new_turtle)

is_race = False

if predict:
    is_race = True

while is_race:
    for turtle in turtles:
        if turtle.xcor() > 210:
            is_race = False
            win_color = turtle.pencolor()
            if win_color == predict:
                print(f"You've won! The race winner is {turtle.pencolor()}")
            else:
                print(f"You've lost! The race winner is {turtle.pencolor()}")
        distance = random.randint(1, 20)
        turtle.forward(distance)

screen.exitonclick()
