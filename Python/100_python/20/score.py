from turtle import Turtle

FONT = ('Arial', 30, 'normal')
ALIGMENT = 'center'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(-75, 270)
        self.color('white')
        self.hideturtle()
        self.set_score()
    
    def update_score(self):
        self.score += 1
        self.clear()
        self.set_score()    

    def set_score(self):
        self.write(arg=(f"Score: {self.score}"), font=FONT)

    
    def game_over(self):
        self.goto(0,0)
        self.write('Game Over', align=ALIGMENT, font=FONT)
