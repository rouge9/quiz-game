# color exteractor form image
# import colorgram
# colors = colorgram.extract('Addictive---detail-of-Dam-007.jpg', 104)
# rgb_color = []
# for beep in colors:
#     r = beep.rgb.r
#     g = beep.rgb.g
#     b = beep.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
colors = [(153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72), (145, 178, 148), (91, 73, 75), (233, 176, 165), (160, 143, 159), (54, 47, 50), (184, 205, 172), (35, 61, 75), (22, 85, 89), (146, 19, 21), (86, 146, 130), (38, 67, 91), (13, 72, 66), (106, 128, 155), (175, 99, 101), (176, 192, 209), (114, 135, 138), (207, 182, 188), (69, 63, 57), (179, 197, 201)]

tim = Turtle()
tim.speed("fastest")
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot in range(1,num_of_dots+1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)


    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen = Screen()
screen.exitonclick()
