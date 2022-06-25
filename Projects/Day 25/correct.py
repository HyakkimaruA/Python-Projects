from turtle import Turtle

FONT = ('Courier', 10, 'bold')


class Correct(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def win(self):
        self.home()
        self.write("Congratulations, you have completed the game!", align="center", font=FONT)
