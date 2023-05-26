from turtle import Screen
from myturtle import MyTurtle
import time
from cars_manager import CarsManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Game")
screen.tracer(0)

bozo = MyTurtle()
cars_manager = CarsManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=bozo.move)



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars_manager.generate_car()
    cars_manager.cars_move()

    # Detect collision with cars
    for car in cars_manager.all_cars:
        if car.distance(bozo) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with wall
    if bozo.ycor() > 280:
        bozo.starting_position()
        scoreboard.update_score()


















screen.exitonclick()