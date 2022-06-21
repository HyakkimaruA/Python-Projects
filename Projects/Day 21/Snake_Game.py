from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=650)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.written()

    z = 3
    #Detect collision with food.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        scoreboard.score += 1
        snake.create_block()


    #Detect collision with wall.
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290:
        scoreboard.game_over()
        game_is_on = False
    elif snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail
    for i in range(2, len(snake.segments), 1):
        if snake.segments[0].distance(snake.segments[i]) < 15:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
