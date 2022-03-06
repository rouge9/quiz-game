from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
screen = Screen()
is_game_on = True
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()


screen.listen()

screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect collusion with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collusion with the paddle
    if ball.distance(paddle_1) < 50 or ball.xcor() >320 or ball.distance(paddle_2) < 50 or ball.xcor() < -320:
        ball.bounce_x()
screen.exitonclick()
