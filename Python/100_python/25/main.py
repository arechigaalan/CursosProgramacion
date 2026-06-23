from turtle import Turtle, Screen
import pandas as pd

s = Screen()
s.setup(730, 500)
s.title('U.S. States Game')
s.addshape('./blank_states_img.gif')
t = Turtle('./blank_states_img.gif')
t_writer = Turtle()
t_writer.hideturtle()
t_writer.penup()
data = pd.read_csv('./50_states.csv')
score = 0
states_guessed = []
all_states = data.state.to_list()

while score < 50:
    answer = s.textinput(f'{score}/50 States Correct', prompt='What\'s another state\'s name')
    if not data[data.state == answer].empty:
        data_state = data[data.state == answer].iloc[0]
        state = data_state.state
        x = data_state.x
        y = data_state.y
        t_writer.goto(x, y)
        t_writer.write(state, False, 'center', ('Arial', 8, 'normal'))
        states_guessed.append(state)
        score += 1
    if answer == 'exit':
        left_states = [st for st in all_states if st not in states_guessed]
        df = pd.DataFrame(left_states)
        df.to_csv('left_states.csv')
        break

s.exitonclick()
