#!/usr/bin/python3
"""Draw square challenge"""
from turtle import Turtle, Screen

draw_square = Turtle()
draw_square.begin_fill()
draw_square.forward(90)
draw_square.lt(90)
draw_square.bk(90)
draw_square.rt(90)
draw_square.bk(90)
draw_square.lt(90)
draw_square.forward(90)
draw_square.color("#CDCDC0")
draw_square.fillcolor('#8B8B83')
draw_square.end_fill()
screen = Screen()
screen.exitonclick()
