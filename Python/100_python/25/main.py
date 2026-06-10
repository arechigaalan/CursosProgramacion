from turtle import Turtle, Screen
import pandas as pd

s = Screen()
s.setup(730, 500)
s.title('U.S. States Game')
s.addshape('./blank_states_img.gif')
t = Turtle('./blank_states_img.gif')
data = pd.read_csv('./50_states.csv')
print(data)
score = 0

while score < 5:
    answer = s.textinput(title=f'{score}/50 States Correct', prompt='What\'s another state\'s name')
    if not data[data.state == answer].empty:
        data_state = data[data.state == answer]
s.mainloop()
