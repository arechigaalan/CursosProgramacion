from turtle import Turtle as t, Screen as s

timmy = t()
screen = s()

def move_forward():
    timmy.fd(20)

def move_backward():
    timmy.bk(20)

def move_left():
    timmy.left(20)
    
def move_right():
    timmy.right(20)

def clear_screen():
    screen.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_screen, "c")




screen.exitonclick()
