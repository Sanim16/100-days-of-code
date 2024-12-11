from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("green")
        self.pu()
        self.goto(0, 280)
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over! Final Score = {self.score} ", align=ALIGN, font=FONT)


    def update_score(self):
        self.write(f"Score = {self.score} ", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

