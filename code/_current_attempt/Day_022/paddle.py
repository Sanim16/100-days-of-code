from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y_coord = self.ycor() + 20
        self.goto(self.xcor(), new_y_coord)

    def go_down(self):
        new_y_coord = self.ycor() - 20
        self.goto(self.xcor(), new_y_coord)


    def move_paddle(self):
        self.forward(10)
        if self.ycor() >= 290:
            self.setheading(270)

    def up(self):
        self.setheading(90)
