from turtle import Screen
from paddle import Paddle
from paddle_ball import Ball
from scoreboard import Scoreboard
import time

# Setting up the main screen

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# paddle with location on x-axis
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# taking ball into consideration
ball = Ball()

# taking scoreboard into consideration
scoreboard = Scoreboard()

# screen listen's for command and move the paddle accordingly
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# repeating the process with while
is_game_on = True
while is_game_on:
    # declaring speed of ball
    time.sleep(ball.move_speed)
    # wake the screen direct on this with the help of update()
    screen.update()
    # making the ball move accordingly
    ball.move()

    # if ball touches the upper or lower surface then bounce on y-axis
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # if ball contacts with paddles then move on x-axis
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if ball touches the wall on x-axis then restart from the beginning and score + 1 to opponent
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # if ball touches the wall on x-axis then restart from the beginning and score + 1 to opponent
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
