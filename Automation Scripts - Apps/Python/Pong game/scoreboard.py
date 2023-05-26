from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_paddle_score = 0
        self.l_paddle_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=0, y=250)
        self.write(arg=f"{self.l_paddle_score}        {self.r_paddle_score}", font=("arial", 30, "bold"), align="center")

    def l_point(self):
        self.l_paddle_score += 1

    def r_point(self):
        self.r_paddle_score += 1