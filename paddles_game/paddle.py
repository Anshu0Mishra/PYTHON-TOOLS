from turtle import Turtle


class Paddle(Turtle):
    # setting the paddles
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    # making the paddle to move upward
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # making the paddle to move downward
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
