from turtle import Turtle, Screen
import time
from paddle import Paddle



screen = Screen()
is_game_on = True
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
time.sleep(0.1)

screen.listen()

screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

while is_game_on:
    screen.update()









screen.exitonclick()
