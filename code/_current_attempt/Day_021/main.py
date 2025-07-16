from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.title('Welcome to Snake Game')
my_screen.bgcolor('black')
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

my_screen.listen()

my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend_snake()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if segment.distance(snake.head) < 10:
            score.game_over()
            game_is_on = False

my_screen.exitonclick()