from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.current_score()

    def current_score(self):
        self.write(arg=f"Score: {self.score}", align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center")


    def new_score(self):
        self.score += 1
        self.clear()
        self.current_score()