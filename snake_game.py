from turtle import Turtle,Screen
import time
screen = Screen()

screen.title("my snake game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
position = [(0, 0), (-20, 0), (-40, 0)]
x_pos = 0
y_pos = 0
segments = []
screen.tracer(0)
for tail in position:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(tail)
    segments.append(snake)


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)

    segments[0].forward(20)
    segments[0].left(90)












screen.exitonclick()