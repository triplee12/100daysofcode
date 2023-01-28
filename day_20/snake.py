#!/usr/bin/env python3
"""snake module"""
from turtle import Turtle

# Move position
POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
# Move distance
MOVE_DIST = 20


class Snake:
    """Snake class"""
    
    def __init__(self):
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        """Creates snake"""

        for i in range(3):
            snake = Turtle(shape="square")
            snake.penup()
            snake.goto(POSITIONS[i])
            self.segments.append(snake)
        return self.segments

    def move(self):
        """Moves the snake forward"""

        for seg in range(len(self.segments) - 1, 0, -1):
            pos_x = self.segments[seg - 1].xcor()
            pos_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(pos_x, pos_y)

        self.segments[0].forward(MOVE_DIST)
