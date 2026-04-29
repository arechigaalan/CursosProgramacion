from turtle import Turtle as T

class Paddle():
    def __init__(self):
        self.create_paddle()

    def create_paddle(self):
        t = T('square')
        t.penup()
        t.color('white')
        t.shapesize(5, 1)
        t.goto(350, 0)
