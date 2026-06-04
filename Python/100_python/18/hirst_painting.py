from turtle import Turtle, Screen
import colorgram
import random

timmy = Turtle()
screen = Screen()

timmy.speed(10)
screen.colormode(255)

def generar_paleta(url, num_of_colors):
    colors = colorgram.extract(url, num_of_colors)
    colors_list_rgb = []
    for color in colors:
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]
        color_rgb = (r, g, b)
        colors_list_rgb.append(color_rgb)
    return(colors_list_rgb)

paleta_colores = generar_paleta('image.jpg', 10)

def hirst_painting():
    timmy.hideturtle() 
    timmy.pencolor(255, 255, 255)
    timmy.goto(-200, -200)
    for _ in range(10):
        for _ in range(10):
            timmy.pendown()
            timmy.dot(20, random.choice(paleta_colores))
            timmy.penup()
            timmy.fd(50)
        timmy.penup()
        timmy.goto(-200, timmy.ycor() + 50)
    
        

hirst_painting()

screen.exitonclick()
