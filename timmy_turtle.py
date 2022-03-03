import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r,g,b)
    return color_tuple

direction = [0,90,180,270]
tim.width(15)
tim.speed("fastest")

# for d in range(1000):
#     tim.color(random_color())
#     tim.forward(70)
#     tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
