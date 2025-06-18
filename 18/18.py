'''1'''
# from turtle import Turtle
# t = Turtle()
# t.up()
# t.goto(-15,150)
# t.down()

# def draw(num):
#     for _ in range(num):
#         t.forward(100)
#         t.right(360/num)
# for i in range(3,11):
#     import random
#     t.color(random.choice(["red","yellow","coral","green","brown"]))
#     draw(i)
'''2'''
# import turtle
# from turtle import Turtle
# import random
# choice_list = ["north","east","south","west"]
# t = Turtle()
# t.speed(8)
# t.pensize(10)
# for i in range(155):
#     t.color(random.choice(["red","yellow","coral","green","brown","blue",]))
#     action = random.choice(choice_list) # WELL SIMPLE AAYYT SET HEADING ENNA PARNJA ORU METHOD IL KODTHTT JUST DEGREE EMNTION CHEYTHA MATHI LIKE 0 EAST AANE, NORTH 90 AND SOUTH, WEST OKKE, APPA INGANE IRINE ELLAM ELIF ILL EDANDA AAVISHYAM ILLA
#     if action == "north":
#         t.forward(50)
#     elif action == "east":
#         t.right(90)
#         t.forward(50)
#     elif action == "south":
#         t.backward(50)
#     else:
#         t.left(90)
#         t.backward(50)
# turtle.exitonclick()

'''3'''
# import random
# import turtle
# from turtle import Turtle

# t = Turtle()
# turtle.colormode(255)
# t.speed(0)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# choice_list = [0,90,180,270]
# t.pensize(15)
# for i in range(200):
#     t.color(random_color())
#     t.forward(25)
#     t.setheading(random.choice(choice_list))
'''4'''
# import turtle
# from turtle import Turtle
# import random
# turtle.colormode(255)
# def rand_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# t = Turtle()
# t.speed(0)
# for i in range(360//5):
#     t.color(rand_color())
#     t.circle(100)
#     t.setheading(t.heading()+5)
# turtle.exitonclick()

'''ACTUAL PROJECT BEGINS HERE...'''
# import colorgram
# colors = colorgram.extract('proj.jpg', 30)
# list_col = []
# for i in colors:
#     list_col.append(tuple(i.rgb))
    
# print(list_col)

color_list = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25), (243, 167, 156), (163, 211, 178), (26, 187, 225), (6, 116, 54), (138, 210, 232), (74, 135, 184), (170, 191, 221), (114, 10, 8)]

import turtle
from turtle import Turtle
import random
turtle.colormode(255)
t = Turtle()
t.speed(10)
t.up()
t.goto((-200,-300))
for i in range(100):
    if i % 10 != 0:
        x = t.pos()[0] + 50
        y = t.pos()[1] 
    else:
        x = -200
        y = t.pos()[1] + 50
    t.setpos((x,y))
    col = random.choice(color_list)
    print(x,y)
    t.dot(20,col)

turtle.exitonclick()