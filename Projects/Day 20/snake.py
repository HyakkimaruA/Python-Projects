from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITION:
            snake_block = Turtle(shape="square")
            snake_block.penup()
            snake_block.color("white")
            snake_block.setpos(i)
            self.segments.append(snake_block)

    def move(self):
        for i in range(len(self.segments) - 1, -1, -1):
            if i != 0:
                x_as = self.segments[i - 1].xcor()
                y_as = self.segments[i - 1].ycor()
                self.segments[i].setpos(x_as, y_as)
            else:
                self.segments[i].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
