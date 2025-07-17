from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")
my_screen.tracer(0)

right_paddle = Paddle((380,0))
left_paddle = Paddle((-380,0))
ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()

my_screen.onkey(right_paddle.go_up, "Up")
my_screen.onkey(right_paddle.go_down, "Down")

my_screen.onkey(left_paddle.go_up, "w")
my_screen.onkey(left_paddle.go_down, "s")

sleep_time = 0.1

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    my_screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()

    # Detect collision with paddle
    if (ball.distance(right_paddle) <= 50 and ball.xcor() >= 360) or (ball.distance(left_paddle) <= 50 and ball.xcor() <= -360):
        sleep_time *= 0.8
        ball.x_bounce()

    # Detect ball out of bounds right side
    if ball.xcor() >= 380:
        sleep_time = 0.1
        ball.reset_position()
        scoreboard.l_point()

    # Detect ball out of bounds left side
    if ball.xcor() <= -380:
        sleep_time = 0.1
        ball.reset_position()
        scoreboard.r_point()

my_screen.exitonclick()
