from random import randint
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=600, height=500)

y_coordinate = 200

colors_of_turtles = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []

for number in range(len(colors_of_turtles)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors_of_turtles[number])
    new_turtle.teleport(x=-280, y=y_coordinate)
    new_turtle.penup()
    y_coordinate -= 50
    all_turtles.append(new_turtle)

is_race_on = False
user_choice = my_screen.textinput(title="Pick your winner", prompt="Select the winning turtle")

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_choice == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")

        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
















my_screen.exitonclick()