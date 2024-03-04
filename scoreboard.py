from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-40,y=270)
        self.color("white")
        self.hideturtle()
        self.score_points = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score_points}",align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(x=-60,y=0)
        self.write(arg="GAME OVER !",font=FONT)

    def score(self):
        self.clear()
        self.score_points += 1
        self.update_scoreboard()
