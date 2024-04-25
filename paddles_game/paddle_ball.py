from turtle import Turtle


class Ball(Turtle):

    # setting the ball
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # making the ball to move
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # making the ball to bounce from upper and lower wall
    def bounce_y(self):
        self.y_move *= -1

    # making the ball to bounce from left and right side of the wall
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # reset's the position back to middle
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
