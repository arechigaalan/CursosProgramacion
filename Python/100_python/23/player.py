from turtle import Turtle as T

STARTING_POSTITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(T):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSTITION)
        self.setheading(90)
    
    def move(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSTITION)
