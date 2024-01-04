from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.level = 0
        self.goto(-290, 270)
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', font = FONT, align='center')

    def update_level(self):
        self.clear()
        self.write(f'Level : {self.level}', font=FONT, align = 'left')

    def add_level(self):
        self.level += 1
        self.update_level()