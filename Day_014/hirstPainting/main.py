import random
from turtle import Turtle, Screen

# import colorgram
# colors = colorgram.extract('./image.png', 30)

# image_colors = []
# for color in range(len(colors)):
#     get_color = (colors[color].rgb.r, colors[color].rgb.g, colors[color].rgb.b)
#     image_colors.append(get_color)

color_list = [(241, 229, 212), (230, 150, 79), (212, 227, 237), (239, 223, 231), (223, 237, 231), (33, 112, 159), (111, 174, 206), (160, 13, 38), (160, 54, 93), (182, 172, 18), (232, 84, 47), (33, 129, 71), (176, 78, 40), (18, 169, 206), (60, 16, 31), (226, 203, 105), (43, 24, 15), (18, 29, 66), (201, 70, 117), (125, 181, 151), (197, 137, 166), (5, 109, 80), (10, 48, 32), (64, 165, 110), (136, 214, 228), (23, 53, 126), (162, 19, 12), (233, 166, 192), (108, 113, 174), (158, 212, 185)]

my_canvas = Screen()
my_canvas.colormode(255)
timmy = Turtle()
timmy.hideturtle()
timmy.speed("fastest")
timmy.pu()
# timmy.setheading(0)


def draw_spot_painting(start_x, start_y, no_of_vertical_lines, no_of_horizontal_lines, color_selection):
    """
    A function to draw a spot painting
    :param start_x: starting x coordinate
    :param start_y: starting y coordinate
    :param no_of_vertical_lines: number of vertical lines
    :param no_of_horizontal_lines: number of horizontal lines
    :param color_selection: set of colors to choose from
    :return:
    """
    for number in range(no_of_horizontal_lines):
        timmy.teleport(start_x, start_y)
        for _ in range(no_of_vertical_lines):
            timmy.dot(20, random.choice(color_selection))
            timmy.fd(50)
        start_y += 50

draw_spot_painting(-350, -350, 15, 15, color_list)


my_canvas.exitonclick()
