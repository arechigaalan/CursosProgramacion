from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, move=False, align='center', font=('Arial', 40, 'bold'))
