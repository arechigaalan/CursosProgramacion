from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.shapesize(1, 1)
        self.speed('fastest')
        self.color('blue')
        self.position

    def position(self):     
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.penup()
        self.goto(x, y)

    