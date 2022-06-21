from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score = 0
        self.setposition(0, 250)
        self.written()

    def written(self):
        self.penup()
        self.setposition(25, 290)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.setposition(0, 0)
        self.write(f"Game Over.", align=ALIGNMENT, font=FONT)