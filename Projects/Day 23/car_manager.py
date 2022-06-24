from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CARS = []


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speeding = STARTING_MOVE_DISTANCE
        self.cars = 0

    def create_cars(self):
        self.car = Turtle(shape="square")
        self.car.color(random.choice(COLORS))
        self.car.penup()
        self.car.shapesize(stretch_len=2)
        self.car.goto(320, random.randint(-200, 250))
        self.car.setheading(180)
        CARS.append(self.car)


    def moving_car(self):
        for self.car in CARS:
            self.car.forward(self.speeding)
            self.cars += 1

    def increase_speed(self):
        self.speeding += MOVE_INCREMENT




