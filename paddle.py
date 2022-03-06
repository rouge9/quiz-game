from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.y_cord = 0
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(350, self.y_cord)
        self.move_up
        self.move_down


    def move_up(self):
        self.y_cord += 20
        self.goto(350, self.y_cord)

    def move_down(self):
        self.y_cord -= 20
        self.goto(350, self.y_cord)
