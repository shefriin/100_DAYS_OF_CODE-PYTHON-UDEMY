# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)

# # import csv
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     # print(data)
# #     temperatures = []
# #     for row in data:
# #         # print(row)
# #         if row[1].isdigit():
# #             temperatures.append(int(row[1]))

# #     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["day"]))
# dic = data.to_dict()
# # print(dic)
# temp_list = data["temp"].tolist()
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)

# # print(temp_list)
# # print(data["temp"].mean())
# # print(data["temp"].max())

# # print(data.day)

# # print(data[data["day"] == "Monday"])

# # print(data[data.temp == data["temp"].max()])

# # mon = data[data.day == "Monday"]
# # print(mon.condition)

# # mon = data[data.day == "Monday"]
# # mon.temp = (mon.temp * 9/5) +32
# # print(mon)
# # print(data)

# d = {
#     "students": ["Ajay", "Ann","James"],
#     "scores" : [76,85,79]
# }
# data = pandas.DataFrame(d)
# print(data)
# data.to_csv("new.csv")



import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_list = data["Primary Fur Color"].to_list()

gray = 0
cinnamon = 0
black = 0
for data in fur_list:
    if data == "Gray":
        gray += 1
    elif data == "Cinnamon":
        cinnamon += 1
    elif data == "Black":
        black += 1
#OR JUST FINF THE LENGTH OF THE WHOLE THING THAT IS LENGTH OF GRAY, RED, BLACK, IE LIKE, DATA[DATA["PRIMARY FUR COLOR"] == "GRAY"] DRN TAKE ITS LENGTH, SO THATS TOO EAAAZZYY

d = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count":[gray, cinnamon, black]
}
new_data = pandas.DataFrame(d)

new_data.to_csv("squirrel_count.csv")
