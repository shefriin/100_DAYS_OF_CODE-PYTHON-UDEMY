from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.x = 10
        self.y = 10
        self.sleep_val = 0.1

    def move(self):
        x_cord = self.xcor() + self.x
        y_cord = self.ycor() + self.y
        self.goto((x_cord,y_cord))
    
    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.sleep_val *= 0.9

    def restart(self):
        self.home()
        self.bounce_x()
        self.sleep_val = 0.1
        