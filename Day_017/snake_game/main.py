from turtle import Turtle, Screen
import time
from snake import Snake

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Snake Game")
my_screen.bgcolor("black")
my_screen.tracer(0)


snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    snake.move_snake()
    my_screen.update()
    time.sleep(0.3)








my_screen.exitonclick()