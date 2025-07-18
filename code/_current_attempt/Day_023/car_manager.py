from turtle import Turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def new_cars(self):
        random_car_generator = randint(1,10)
        if random_car_generator % 3 == 0:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(280, randint(-250, 250 ))
            self.cars.append(new_car)

    def move_car(self):
        for each_car in self.cars:
            each_car.backward(self.move_speed)

    def next_level(self):
        self.move_speed += MOVE_INCREMENT
