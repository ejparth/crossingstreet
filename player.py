from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Green")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def upy(self):
        self.forward(10)
        print("Click")

