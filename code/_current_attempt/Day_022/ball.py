from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_ball_speed = 10
        self.y_ball_speed = 10

    def move(self):
        new_x = self.xcor() + self.x_ball_speed
        new_y = self.ycor() + self.y_ball_speed
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_ball_speed *= -1

    def x_bounce(self):
        self.x_ball_speed *= -1

    def reset_position(self):
        self.home()
        self.x_bounce()
