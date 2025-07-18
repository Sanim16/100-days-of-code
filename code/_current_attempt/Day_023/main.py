import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car1 = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car1.new_cars()
    car1.move_car()
    for car in car1.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.level_complete():
        scoreboard.update_score()
        car1.next_level()



screen.exitonclick()