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
# tim.width(15)
tim.speed("fastest")
def draw_circle(size):
    for d in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)


draw_circle(5)
screen = Screen()
screen.exitonclick()
