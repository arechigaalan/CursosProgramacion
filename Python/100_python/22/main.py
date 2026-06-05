from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.title('Pong game')
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_scoreboard = Scoreboard((-200, 240))
r_scoreboard = Scoreboard((200, 240))

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(r_paddle.go_up, 'Up')

game_is_on = True
sleep_time = 0.1

dash_line = Turtle()
dash_line.shape('turtle')
dash_line.color('White')
dash_line.teleport(0, 300)
dash_line.begin_fill()
dash_line.goto(0, -300)
dash_line.hideturtle()

while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    y = ball.ycor()

    if y > 280 or y < -280:
        ball.change_direction_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.change_direction_x()
        sleep_time *= 0.9

    if ball.xcor() > 380:
        ball.reset()
        l_scoreboard.update_score()
        sleep_time = 0.1

    if ball.xcor() < -380:
        ball.reset()
        r_scoreboard.update_score()
        sleep_time = 0.1

screen.exitonclick()
