from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

timmy.shape('turtle')
timmy.color('blue')

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

screen.exitonclick()
