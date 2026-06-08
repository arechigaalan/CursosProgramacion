import time
from turtle import Screen as S
from player import Player as P
from car_manager import CarManager as CM
from scoreboard import Scoreboard

s = S()
s.setup(600, 600)
s.tracer(0)
s.listen()
p = P()
s.onkey(p.move, 'Up')
cm = CM()
sc = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    s.update()

    sc.write_score()

    cm.create_car()
    cm.move_cars()

    for car in cm.all_cars:
        if car.distance(p) < 20:
            game_is_on = False
            sc.game_over()

    if p.ycor() >= 280:
        cm.level_up()
        p.restart()
        sc.level_up()
        sc.write_score()

s.exitonclick()
