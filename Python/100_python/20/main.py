import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) #! Hace que la pantalla no se actualice automáticamente. 
screen.listen()

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.add_segment()

    if snake.head.xcor() < -300 or snake.head.xcor() > 300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        scoreboard.reset()
        snake.reset()
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
