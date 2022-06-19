from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def clockwise():
    tim.right(10)


def counter_clockwise():
    tim.left(10)


def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
