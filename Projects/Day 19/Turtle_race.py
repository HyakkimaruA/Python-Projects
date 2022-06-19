from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win this race? (Color)").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_axis = -100
for i in range(len(colors)):
    new_t = Turtle(shape="turtle")
    new_t.color(colors[i])
    new_t.penup()
    new_t.setpos(x=-230, y=y_axis)
    y_axis += 40
    all_turtles.append(new_t)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtles in range(len(all_turtles)):
        rand_distance = random.randint(0, 10)
        all_turtles[turtles].forward(rand_distance)
        turtle_number = all_turtles[turtles]
        if turtle_number.xcor() >= 230:
            is_race_on = False
            if user_bet == turtle_number.color()[0]:
                print(f"The {turtle_number.color()[0]} turtle is the Winner! Which means you have won!")
            else:
                print(f"The {turtle_number.color()[0]} turtle is the winner.... Which means your {user_bet} turtle lost....")
    turtles = 0

screen.exitonclick()
