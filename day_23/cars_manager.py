#!/usr/bin/env python3
"""Car manager module for turtle crossing the road"""
from turtle import Turtle
import random

COLORS = ["#f98866", "#ff420e", "#80bd9e", "#89da59", "#90afc5", "#336b87", "#2a3132", "#763626", "#46211a", "#693d3d", "#a43820", "#598234"]


class CarsManager:
    """
    CarsManager class manages the creation of the cars, positions, 
    speed and colors of the cars.
    """

    def __init__(self):
        self.cars = []
        #self.create_cars()

    def car_color(self):
        """Returns color randomly"""
        ran_color = random.choice(COLORS)
        return ran_color

    def create_cars(self):
        """
        Creates cars of different colors, position them at 
        different positions on x-axis
        """
        move_by = random.randint(2, 7)
        if move_by == 7:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(self.car_color())
            ypos = random.randint(-250, 250)
            new_car.goto(300, ypos)
            self.cars.append(new_car)

    def move(self):
        """Moves the cars from positive x-axis to negative x-axis"""
        for car in self.cars:
            distance = random.randint(3, 9)
            car.backward(distance)
