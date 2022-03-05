from turtle import Turtle
AlIGNMENT = "center"
FONT = ("Times Roman", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update

    def update(self):
        self.write(f"scoreboard: {self.score}", align=AlIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update()
