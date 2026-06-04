"""Crear figuras de 3 a 10 lados"""

from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

GRADOS = 360

colores = ['yellow', 'aquamarine4', 'azure4', 'blue4', 'coral3', 
           'brown3', 'DarkGreen', 'DarkSlateGrey', 'DarkOrchid1', 'CornflowerBlue']

for _ in range(3, 11, 1):
    color = random.choice(colores)
    colores.remove(color)
    timmy.color(color)

    angulos_figura = GRADOS/_

    for lado in range(_):
        timmy.left(angulos_figura)
        timmy.forward(100)

screen.exitonclick()
