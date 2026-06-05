from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.write_scoreboard()

    def write_scoreboard(self):
        self.write(f'Score: {self.score}', False, align='center', font=('Arial', 20, 'bold'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over :(', False, align='center', font=('Arial', 20, 'bold'))
        
