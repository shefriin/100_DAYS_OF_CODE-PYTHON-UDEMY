from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())
        super().__init__()
        self.score = 0
        self.up()
        self.hideturtle()
        self.goto((0,270))
        self.color("white")
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score = {self.high_score}", align="center", font=("Calbri", 15, "normal"))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt","w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER",align="center", font=("Courier", 20, "bold"))