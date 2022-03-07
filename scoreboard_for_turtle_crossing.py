from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"level: {self.level}", font=FONT)

    def count(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
