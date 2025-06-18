from turtle import Turtle
SCORE = 0
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto((0,270))
        self.color("white")
        self.write("Score = 0", align="center", font=("Calbri", 15, "normal"))
    
    def update_score(self):
        self.clear()
        global SCORE
        SCORE += 1

        self.up()
        self.hideturtle()
        self.goto((0,270))
        self.color("white")
        self.write(f"Score = {SCORE}", align="center", font=("Calbri", 15, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER",align="center", font=("Courier", 20, "bold"))