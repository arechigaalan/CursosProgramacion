from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
screen = Screen()

screen.colormode(255)
timmy.speed(0)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

def spirograph():
    for _ in range (120):
        timmy.color(random_color())
        timmy.circle(250)
        timmy.right(3)
    


spirograph()

screen.exitonclick()
