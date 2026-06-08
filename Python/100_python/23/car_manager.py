from random import randint as r
from turtle import Turtle as T
from random import choice as c

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        if r(1, 6) == 1:
            new_car = T('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(c(COLORS))
            new_car.goto(320, r(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.bk(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
