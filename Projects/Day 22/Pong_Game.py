from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
line = Line()

screen.listen()
screen.onkeypress(r_paddle.go_up, key='Up')
screen.onkeypress(r_paddle.go_down, key='Down')
screen.onkeypress(l_paddle.go_up, key='w')
screen.onkeypress(l_paddle.go_down, key='s')


game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(0.03)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.ball_faster()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.ball_faster()

    if ball.xcor() > 420:
        ball.set_ball_back()
        screen.update()
        scoreboard.l_point()
        ball.set_speed_back()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
        time.sleep(1)
    elif ball.xcor() < -420:
        ball.set_ball_back()
        screen.update()
        scoreboard.r_point()
        ball.set_speed_back()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
        time.sleep(1)


screen.exitonclick()
