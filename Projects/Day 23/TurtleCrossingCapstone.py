import time
import car_manager
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, 'w')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if car.cars % 4 == 0:
        car.create_cars()
    if player.ycor() >= 280:
        player.go_back_to_position()
        car.increase_speed()
        scoreboard.increase_level()
        time.sleep(0.5)
    car.moving_car()
    for cars in car_manager.CARS:
        if player.distance(cars) <= 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
