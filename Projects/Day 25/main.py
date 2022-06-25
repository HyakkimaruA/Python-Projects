import turtle
import pandas as pd
from correct import Correct


states_df = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


correct = Correct()
correct_states = 0
game_is_on = True
correct_answers = []

while game_is_on:
    answer_data = turtle.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another state's name?").capitalize()
    if answer_data == "Exit":
        game_is_on = False
    if answer_data in states_df['state'].to_list() and answer_data not in correct_answers:
        correct_states += 1
        values = states_df[states_df['state'] == answer_data]
        correct.goto(int(values['x']), int(values['y']))
        correct.write(answer_data, font=("Courier", 8, 'bold'))
        correct_answers.append(answer_data)
    if correct_states == 50:
        game_is_on = False
        correct.win()

all_states = states_df['state'].to_list()
states_to_learn = []

for state in all_states:
    if state not in correct_answers:
        states_to_learn.append(state)

learn_dict = {
    "state": states_to_learn
}

learn_states = pd.DataFrame(learn_dict)

learn_states.to_csv('states_to_learn.csv')
