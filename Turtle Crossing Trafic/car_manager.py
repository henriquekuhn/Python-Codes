from turtle import Turtle
import random

color = ["green", "red", "yellow", "blue", "orange", "purple"]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 2)
        self.color(color[random.randint(0,5)])
        self.goto(280, random.randint(-260, 260))
    
    def move_forward(self):
        self.backward(10)