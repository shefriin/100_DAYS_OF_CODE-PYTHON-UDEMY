import pandas
import turtle

data_file = pandas.read_csv("50_states.csv")
states_list = data_file["state"].to_list()


screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
t = turtle.Turtle()
t.hideturtle()
t.up()

guess_list = []
correct_state = 0
while correct_state <= 50:
    answer_state = screen.textinput(title=f"{correct_state}/50 States Correct", prompt="What's another states's name?").title()
    if answer_state == "Exit":
          break
    if answer_state in states_list and answer_state not in guess_list:
            correct_state += 1
            loc_x =  data_file[data_file["state"] == answer_state].x
            loc_y =  data_file[data_file["state"] == answer_state].y
            t.goto(x=loc_x.iloc[0], y=loc_y.iloc[0])
            t.write(answer_state,align='center', font=('Arial', 8, 'normal'))

            guess_list.append(answer_state)

# screen.exitonclick()


# list_miss = [] 
# # d = {
# #     "other_states" :[]
# # }
# for state in states_list:
#       if state not in guess_list:
#         # d["other_states"].append(state)
#         list_miss.append(state)

list_miss = [state for state in states_list if state not in guess_list]  # USE THE LIST COMPREHENSION WE STUDIES THE NEXT DAY THAT IS DAY-26

# data = pandas.DataFrame(d)
data = pandas.DataFrame(list_miss)
data.to_csv("study_1.csv")