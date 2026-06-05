from turtle import Turtle

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] 

    def create_snake(self):
        x = 0
        for _ in range(3):
            segment = Turtle('square')
            segment.penup()
            segment.color('white')
            segment.goto(x, 0)
            self.segments.append(segment)
            x -= 20

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].goto(self.segments[segment - 1].xcor(), self.segments[segment - 1].ycor())
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def add_segment(self):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(self.segments[-1].pos())
        self.segments.append(segment)
    