from turtle import Turtle

WIDTH = 5 # means 5*20 pixel = 100
LENGTH = 1 # means 1*20 pixel = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(WIDTH, LENGTH)
        self.penup()
        self.color('white')
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
