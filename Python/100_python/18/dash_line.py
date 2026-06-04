from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

timmy.shape('turtle')
timmy.color('purple')

for _ in range(50):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen.exitonclick()
