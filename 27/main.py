from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)
# window.minsize(width=300, height=100)

input = Entry(width=10)
input.grid(row=0, column=1)

text_label_1 = Label(text="Miles")
text_label_1.grid(row=0, column=2)

text_label_2 = Label(text="is equal to")
text_label_2.grid(row=1, column=0)

text_label_3 = Label(text=" ")
text_label_3.grid(row=1, column=1)

text_label_4 = Label(text="Km")
text_label_4.grid(row=1, column=2)

def button_clicked():
    val = int(float(input.get()) * 1.609)
    text_label_3.config(text=val)
button = Button(text="CALCULATE", command=button_clicked)
button.grid(row=2, column=1)


window.mainloop()