"""Generar una caminata aleatoria"""

from turtle import Turtle, Screen
from random import choice
import random

ANGLES = [0, 90, 180, 270]

timmy = Turtle()
screen = Screen()

screen.colormode(255)
timmy.pensize(15)
timmy.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(500):
    timmy.color(random_color())
    timmy.setheading(choice(ANGLES))
    timmy.forward(25)

screen.exitonclick()
