from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)
    
    def create_paddle(self,pos):
        self.up()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(pos)

    def go_up(self):
        y = 20
        if self.ycor() > 250:
            y = 0
        val_y = self.ycor() + y
        self.goto((self.xcor(),val_y))

    def go_down(self):
        y = 20
        if self.ycor() < -230:
            y = 0
        val_y = self.ycor() - y
        self.goto((self.xcor(),val_y))
