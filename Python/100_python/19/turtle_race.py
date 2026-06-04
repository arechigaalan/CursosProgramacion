from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput('Make your bet', 'Wich turtle will win the race? Enter a color: ') 

COLORS = ['red', 'green', 'purple', 'blue', 'pink', 'gray']

def create_turtles():
    turtles = []
    random.shuffle(COLORS)
    for color in COLORS:
        t = Turtle('turtle')
        t.color(color)
        turtles.append(t)
    return turtles

def turtle_positions(turtles):
    y = 175
    for i, turtle in enumerate(turtles):
        turtle.penup()
        turtle.goto(-220, y - ((i + 1) * 50))

def create_finishing_line():
    t = Turtle('turtle')
    t.speed("slowest")
    t.penup()
    t.goto(220, 180)
    t.pendown()
    t.goto(220, -180)
    t.hideturtle()

def avance(turtles):
    for turtle in turtles:
        turtle.goto(turtle.xcor() + random.randint(1, 10), turtle.ycor())

def winner(turtles):
    for turtle in turtles:
        if turtle.xcor() > 220:
            ganador = turtle.color()
            return True, ganador
    return False, None

def race():
    turtles = create_turtles()
    turtle_positions(turtles)
    create_finishing_line()
    while True:
        avance(turtles)
        hay_ganador, color = winner(turtles)
        if hay_ganador:
            if user_bet == color[0]:
                print(f'You win. The winner was {color[0]}')
            else:
                print(f'You lost. The winner was {color[0]}')
            break

race()

screen.exitonclick()
