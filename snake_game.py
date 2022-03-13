from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

screen = Screen()
screen.title("my snake game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    # Detect collusion with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_scoreboard()
        food.refresh()
        snake.extend()

    # Detect collusion with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collusion with its self
    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()

    snake.move()

screen.exitonclick()
