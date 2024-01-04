from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 80, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.L_score = 0
        self.R_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 200)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f'{self.L_score} : {self.R_score}', align=ALIGNMENT, font=FONT)

    def add_L_score(self):
        self.L_score += 1
        self.update_scoreboard()

    def add_R_score(self):
        self.R_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.L_score == 5:
            self.write(f"GAME OVER\nLeft side wins!", align=ALIGNMENT, font=('Arial', 40, 'normal'))
        elif self.R_score == 5:
            self.write(f"GAME OVER\nRight side wins!", align=ALIGNMENT, font=('Arial', 40, 'normal'))