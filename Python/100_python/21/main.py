from turtle import Screen as S
from paddle import Paddle
import time

s = S()
s.title("Pong Game")
s.bgcolor("#000000")
s.setup(800, 600)

paddle1 = Paddle().create_paddle(1)
paddle2 = Paddle().create_paddle(2)

s.exitonclick()
