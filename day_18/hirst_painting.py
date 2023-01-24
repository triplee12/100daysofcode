#!/usr/bin/python3
"""Hirst painting project"""
from turtle import Screen
import turtle as turtl
import random
import colorgram

screen = Screen()
hirst = turtl.Turtle()
hirst.speed(0)
turtl.colormode(255)
hirst.ht()
screen.bgcolor("#f1f1f2")
hirst.setheading(230)
hirst.up()
hirst.forward(345)
hirst.setheading(0)
hirst.down()

images = ["images/dots.jpeg", "images/pointart.jpg", "images/clifford-possum-tjapaltjarri.jpg"]

rgb_colors = []

# Extract rgb colors from images
for i in range(len(images)):
    colors = colorgram.extract(images[i], 50)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb = rgb_colors.append((r, g, b))

# Create dots paintings
for i in range(12):
    for j in range(12):
        hirst.begin_fill()
        hirst.filling()
        hirst.dot(20, random.choice(rgb_colors))
        hirst.end_fill()
        hirst.up()
        hirst.forward(45)

    hirst.setheading(90)
    hirst.forward(45)
    hirst.setheading(180)
    hirst.forward(540)
    hirst.setheading(0)

screen.exitonclick()
