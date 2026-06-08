from turtle import Turtle as T
FONT = ('Courier', 24, 'normal')

class Scoreboard(T):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-210, 250)
    
    def write_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def level_up(self):
        self.level += 1

    def game_over(self):
         self.home()
         self.write(f'Game Over', align='center', font=FONT, )
