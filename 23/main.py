import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.rand_cars()
    cars.move_car()

    for i in cars.cars_all:
          if player.distance(i) < 20:
            score.over()
            game_is_on = False

    if player.ycor() > 280:
        player.next_level()
        cars.increase_speed()
        score.update_score()
            
screen.exitonclick()
