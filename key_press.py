import random
from turtle import Turtle,Screen
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="make a bet",prompt="which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_postion = [-70,-40,-10,20,50,80]
is_race_on = False
all_turtle = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_postion[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won: {winning_color} is the winner")
            else:
                print(f"you have lost: {winning_color} is the winner")

        random_number = random.randint(0,10)
        turtle.forward(random_number)


screen.exitonclick()