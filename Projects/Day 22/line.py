from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.width(5)
        self.goto(0, 300)
        self.draw_line()

    def draw_line(self):
        for i in range(300, -300, -15):
            if i % 2 == 0:
                self.pendown()
                self.goto(0, i)
            elif i % 2 != 0:
                self.penup()
                self.goto(0, i)