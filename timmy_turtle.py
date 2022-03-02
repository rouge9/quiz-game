import random
from turtle import Turtle, Screen

tim = Turtle()

def draw_side(num_side):
    angle = 360/num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for shape_side in range(3,11):
    tim.color(random.choice(colours))
    draw_side(shape_side)


screen = Screen()
screen.exitonclick()
