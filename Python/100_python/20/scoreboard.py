from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        with open('high_score.txt') as high_score_file:
            self.high_score = int(high_score_file.read())
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Arial', 20, 'bold'))

    def update_score(self):
        self.score += 1
        self.leer_high_score()
        self.write_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            with open('high_score.txt', mode='w') as high_score_file:
                high_score_file.write(str(self.score))
        self.score = 0
        self.leer_high_score()
        self.write_scoreboard()

    def leer_high_score(self):
        with open('high_score.txt') as high_score_file:
            self.high_score = int(high_score_file.read())
