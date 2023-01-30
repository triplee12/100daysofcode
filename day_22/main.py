#!/usr/bin/env python3
"""Main module of pong game"""
from turtle import Screen
from ball import Ball
from scoreboard import ScoreBoard
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
score = ScoreBoard()
is_on = True

while is_on:
    time.sleep(pong_ball.move_fast)
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
            pong_ball.reset_time()
            screen.update()
            pong_ball.goto(0, 0)
            score.update_lscore()
            pong_ball.x_bounce()
        elif pong_ball.distance(left_paddle) > 50 and pong_ball.xcor() < - 335:
            pong_ball.reset_time()
            screen.update()
            pong_ball.goto(0, 0)
            score.update_rscore()
            pong_ball.x_bounce()

        #is_on = False

screen.exitonclick()
