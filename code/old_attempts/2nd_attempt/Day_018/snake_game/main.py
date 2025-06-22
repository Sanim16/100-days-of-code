from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Snake Game")
my_screen.bgcolor("black")
my_screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    snake.move_snake()
    my_screen.update()
    time.sleep(0.1)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend_segment()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_on = False

    # Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_on = False




my_screen.exitonclick()