from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/cyc/Documents/Udemy_100_Days_of_Code/D24_track_snake_high_score/data.txt") as file:
            self.highest_score = int(file.read())        
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("/Users/cyc/Documents/Udemy_100_Days_of_Code/D24_track_snake_high_score/data.txt", mode = 'w') as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
