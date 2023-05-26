from turtle import Turtle


class MyTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(1.2)
        self.left(90)
        self.starting_position()

    def starting_position(self):
        self.goto(x=0, y=-260)

    def move(self):
        self.forward(10)