from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars_all = []
        self.speed_val = STARTING_MOVE_DISTANCE

    def rand_cars(self):
        random_chance = random.randint(1,5)
        if random_chance == 1:
            new_car = Turtle()
            new_car.up()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            ycord = random.randint(-250,250)
            new_car.goto((380,ycord))
            self.cars_all.append(new_car)
        

    def move_car(self):
        for i in self.cars_all:
            i.backward(self.speed_val)
    
    def increase_speed(self):
        self.speed_val += MOVE_INCREMENT


