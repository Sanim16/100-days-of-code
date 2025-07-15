from turtle import Turtle, Screen
import random

my_screen = Screen()
is_race_on = False

my_screen.setup(width=500, height=400)
player_bet = my_screen.textinput(title='Place your Bets', prompt='Which turtle will win the race? Enter a color: ').lower()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
racing_turtles = []

x_coord = -230
y_coord = -150

for new_turtle in range(0, 7):
    turtle_racer = Turtle('turtle')
    turtle_racer.penup()
    turtle_racer.color(colors[new_turtle])
    turtle_racer.goto(x_coord, y_coord)
    y_coord += 50
    racing_turtles.append(turtle_racer)

if player_bet:
    is_race_on = True

while is_race_on:
    for turtle in racing_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    for turtle in racing_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == player_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")


my_screen.exitonclick()
