from turtle import Screen as S
from snake import Snake
from food import Food
from score import Score
import time

s = S()
s.title("Snake game")
s.bgcolor("#000000")
s.setup(600, 600)
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

s.listen()
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
s.onkey(snake.down, "Down")
s.onkey(snake.up, "Up")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    #! Detect collision with food.
    if snake.head.distance(food) < 15:
        food.position()
        score.update_score()
        snake.extend()

    #! Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        score.game_over()

    #! Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

s.exitonclick()