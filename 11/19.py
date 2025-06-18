'''free drawing'''
# from turtle import Turtle, Screen

# t = Turtle()
# screen = Screen()

# def move_fwd():
#     t.forward(25)

# def move_bwd():
#     t.backward(25)

# def move_c_clock():
#     t.left(10)

# def move_clock():
#     t.right(10)

# def clear():
#     screen.resetscreen()

# screen.listen()
# screen.onkey(key="w",fun=move_fwd)
# screen.onkey(key="s",fun=move_bwd)
# screen.onkey(key="a",fun=move_c_clock)
# screen.onkey(key="d",fun=move_clock)
# if screen.onkey(key="c",fun=clear):
#     t.home()

# screen.exitonclick()

""" DE PROJECT..."""

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="MAKE YOUR BET", prompt="Which turtle will win the race? Place your bet.")
colors = ["red", "blue", "yellow", "green", "purple", "orange"]
turtle_list = []
x = -230
y = -150
for i in range(6):
    t = Turtle(shape="turtle")
    t.up()
    t.color(colors[i])
    t.goto((x,y))
    y += 50
    turtle_list.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in turtle_list:
        rand_dist = random.randint(0,10)
        i.forward(rand_dist)

        if i.pos()[0] > 230:
            is_race_on = False
            win_color = i.pencolor()
            if win_color == user_bet:
                print(f"You've won! The winning color is {win_color}")
            else:
                print(f"You've Lost! The winning color is {win_color}")


screen.exitonclick()