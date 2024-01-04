from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_list = []
        self.car_speed = MOVE_INCREMENT

    def add_new_car(self):
        new_car = Turtle('square')
        new_car.penup()
        new_car.shape
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randint(-240,240))
        new_car.setheading(180)
        self.car_list.append(new_car)
        
    def car_move(self):
        for i in range(len(self.car_list)):
            self.car_list[i].forward(self.car_speed)
