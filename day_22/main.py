#!/usr/bin/env python3
"""Main module of pong game"""
from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.tracer(0)
screen.title("Advance Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("#000")
screen.listen()
pong_ball = Ball()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
is_on = True

while is_on:
    time.sleep(0.08)
    screen.update()
    right_paddle.right_side()
    left_paddle.left_side()
    pong_ball.move()
    # Detect collision of the ball with the wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.y_bounce()

    # Detect collision with the paddles
    if pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 335:
        pong_ball.x_bounce()
    elif pong_ball.distance(left_paddle) < 50 and pong_ball.xcor() < -335:
        pong_ball.x_bounce()
    else:
        # Detect when the paddle misses the ball
        if pong_ball.distance(right_paddle) > 50 and pong_ball.xcor() > 335:
            screen.update()
            pong_ball.goto(0, 0)
            pong_ball.x_bounce()
        elif pong_ball.distance(left_paddle) > 50 and pong_ball.xcor() < - 335:
            screen.update()
            pong_ball.goto(0, 0)
            pong_ball.x_bounce()

screen.exitonclick()
