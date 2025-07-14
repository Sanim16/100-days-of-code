import turtle as t
import random

"""This section was used to generate the color list used in the program
import colorgram

# Extract 36 colors from an image.
colors = colorgram.extract('hirst.jpg', 36)

color_for_painting = []
for num in range(len(colors)):
    r = colors[num].rgb.r
    g = colors[num].rgb.g
    b = colors[num].rgb.b
    color = (r,g,b)
    color_for_painting.append(color)
print(color_for_painting)
"""
color_list = [(235, 226, 87), (210, 161, 109), (113, 177, 212), (201, 5, 68), (230, 52, 128), (196, 77, 19), (217, 133, 177), (193, 164, 15), (34, 106, 166), (11, 21, 62), (32, 189, 114), (232, 224, 4), (18, 28, 171), (122, 188, 161), (204, 32, 127), (233, 165, 197), (14, 183, 211), (10, 45, 24), (38, 132, 72), (45, 15, 10), (105, 92, 210), (139, 219, 203), (185, 13, 6), (135, 218, 232), (229, 73, 45), (169, 180, 229), (79, 7, 25), (12, 97, 49), (233, 173, 163), (253, 5, 47), (22, 36, 246), (13, 85, 101)]

my_screen = t.Screen()
my_screen.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.penup()


x_coord = -200
y_coord = -200
for num in range(10):
    tim.teleport(x_coord,y_coord)
    for new_num in range(10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)
    y_coord += 50





my_screen.exitonclick()