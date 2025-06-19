# import tkinter 
from tkinter import * #IMPORTING ALL SO NECESSARY CHANGES MADE

# window = tkinter.Tk()
window = Tk()

window.title("GUI program")
window.minsize(width=500, height=300)
# window.config(padx=200, pady=200) 

# my_label = tkinter.Label(text="I am label", font=("Arial", 20, "bold"))
my_label = Label(text="I am label", font=("Arial", 20, "bold"))
# my_label.pack(side="bottom")
my_label.grid(row=0, column=0)
my_label.config(padx=25, pady=10)

my_label["text"] = "CHANGED"
my_label.config(text="BLOODY")


input = Entry(width=10)
# input.pack()
input.grid(row=2, column=3)

def button_clicked():
    my_label.config(text=input.get())
    # my_label.config(text="Button got clicked!")
    # print("I got clicked")
    # print(input.get())

button = Button(text="PRESS", command=button_clicked)
# button.pack(side="top")
# button.place(x=50,y=100)
button.grid(row=1, column=1)

new_button = Button(text="HEY", command=button_clicked)
new_button.grid(row=0, column=2)

window.mainloop()


#ARGS
"""
def add(*args):
    sum_of_nos = 0
    for num in args:
        sum_of_nos += num
    return sum_of_nos

print(add(5,4,9))
"""

#KWARGS 
"""
# def calc(n,**kwargs):
#     # print(kwargs)
#     # for key,val in kwargs.items():
#     #     print(key,":",val)
#     n += kwargs["add"]
#     print(n)
#     n *= kwargs["mul"]
#     print(n)
#     n /= kwargs["div"]
#     print(n)

# print(calc(2,add=5, mul=8, div=5))

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]

        # RATHER THAN USING [], WE USE GET() SO THAT WE DONT MEET WITH ERROR, BECAUSE IF KEY NOT FOUND THEN, GET WILL JUST RETURN NONE, BUT [] GIVES ERROR

        self.make = kw.get("make")
        self.model = kw.get("model")
        # self.color = kw.get("color")


my_car = Car(make = "Nissan", model= "GT", color="Blue")
print(my_car.model)
print(my_car.make)
"""