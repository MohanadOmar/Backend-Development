from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.goto(x=-260, y=260)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=("arial", 15, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", font=("arial", 25, "bold"), align="center")
