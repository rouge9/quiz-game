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
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()


screen.listen()

screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect collusion with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collusion with the paddle
    if ball.distance(paddle_right) < 30 or ball.xcor() > 380 or ball.distance(paddle_left) < 30 or ball.xcor() < -380:
        ball.bounce_x()

    # detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()

    # detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()



screen.exitonclick()
