from turtle import Turtle,Screen
from snake import Snake
import time


screen = Screen()
screen.title("my snake game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()










screen.exitonclick()