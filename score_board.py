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
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update

    def update(self):
        self.clear()
        self.write(f"scoreboard: {self.score}     High Score {self.high_score}", align=AlIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update()

