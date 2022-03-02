import random
from turtle import Turtle, Screen

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

direction = [0,90,180,270]
tim.width(15)
tim.speed("fastest")
for d in range(1000):
    tim.color(random.choice(colours))
    tim.forward(70)
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
