#!/usr/bin/env python3
"""snake module"""
from turtle import Turtle

# Move position
POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
# Move distance
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Snake class"""
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        """Creates snake"""

        for i in range(3):
            snake = Turtle(shape="square")
            snake.penup()
            snake.goto(POSITIONS[i])
            self.segments.append(snake)
        return self.segments

    def up(self):
        """Moves the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turns the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turns the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        """Moves the snake forward"""

        for seg in range(len(self.segments) - 1, 0, -1):
            pos_x = self.segments[seg - 1].xcor()
            pos_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(pos_x, pos_y)

        self.head.forward(MOVE_DIST)
