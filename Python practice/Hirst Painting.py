# import colorgram

# # Extract 6 colors from an image.
# colors = colorgram.extract('hirst.jpg', 30)

# rgb_colours = []

# for color in colors :
#     c = (color.rgb[0], color.rgb[1], color.rgb[2])
#     rgb_colours.append(c) # e.g. (255, 151, 210)

# print(rgb_colours)

from turtle import Turtle, Screen, colormode
import random
colormode(255)


color_list = [(210, 165, 122), (246, 232, 234), (140, 49, 106), (164, 169, 38), (245, 79, 56), (218, 234, 231), (232, 112, 163), (3, 141, 50), (64, 200, 221), (1, 143, 185), (241, 65, 139), (162, 55, 52), (19, 165, 126), (254, 230, 0), (209, 219, 223), (237, 218, 76), (29, 197, 219), (143, 181, 159), (217, 176, 191), (247, 168, 148), (144, 213, 224), (190, 190, 193), (163, 211, 184), (103, 46, 96), (2, 121, 33), (144, 42, 38)]

t = Turtle()
t.speed(8)


t.teleport(-200,-150)
t.hideturtle()


def line():
    for i in range(10):
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)


def next_line():
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.left(180)

for i in range(10):
    line()
    next_line()

screen = Screen()
screen.exitonclick()