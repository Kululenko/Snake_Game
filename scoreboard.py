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
        self.highscore = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score_points} Highscore: {self.highscore}",align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score_points > self.highscore:
            with open("data.txt",mode="w") as highscore:
                highscore.write(self.score_points)

        self.score_points = 0
    
    
    
    #def game_over(self):
        #self.goto(x=-60,y=0)
        #self.write(arg="GAME OVER !",font=FONT)

    def score(self):
        self.score_points += 1
        self.update_scoreboard()
