from turtle import Turtle

HEIGHT_UP = 280
HEIGHT_BELOW = -280

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.y_move = 6
        self.x_move = 4
        self.penup()

    def move(self):
        x_as = self.xcor() + self.x_move
        y_as = self.ycor() + self.y_move
        self.goto(x_as, y_as)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def set_ball_back(self):
        self.home()
        self.bounce_x()
        self.bounce_y()

    def ball_faster(self):
        self.x_move *= 1.2
        self.y_move *= 1.2

    def set_speed_back(self):
        self.x_move = 4
        self.y_move = 6


