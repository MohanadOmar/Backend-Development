from turtle import Turtle
import random
COLORS = ["red", "blue", "yellow", "purple", "green"]
X_POSITION = 300


class CarsManager:

    def __init__(self):
        self.all_cars = []

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("turtle")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.shape("square")
            new_car.left(180)
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-240, 240)
            new_car.goto(x=X_POSITION, y=y_position)
            self.all_cars.append(new_car)

    def cars_move(self):
        for car in self.all_cars:
            car.forward(10)


