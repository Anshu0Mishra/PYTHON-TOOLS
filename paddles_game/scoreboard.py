from turtle import Turtle


# scoreboard for calculating the points of right paddle and left paddle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    # it will update the score
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_score,  align="center", font=("Courier", 80, "normal"))

    # adds the left side a point whenever the right side paddles misses the ball
    def l_point(self):
        self.l_score += 1
        self.update_score()

    # adds the left side a point whenever the right side paddles misses the ball
    def r_point(self):
        self.r_score += 1
        self.update_score()
