from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.up()
        self.hideturtle()
        self.goto(-255,260)
        self.current_score()

    def current_score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.current_score()
    
    def over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

