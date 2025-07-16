from turtle import Turtle, Screen

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVING_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_body(position)

    def add_snake_body(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def extend_snake(self):
        self.add_snake_body(self.snake_body[-1].pos())

    def move(self):
        for snake_body_number in range(len(self.snake_body) - 1, 0, -1):
            new_x_pos = self.snake_body[snake_body_number - 1].xcor()
            new_y_pos = self.snake_body[snake_body_number - 1].ycor()
            self.snake_body[snake_body_number].goto(new_x_pos, new_y_pos)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)