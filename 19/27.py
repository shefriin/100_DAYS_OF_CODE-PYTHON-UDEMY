import tkinter

window = tkinter.Tk()

window.title("GUI program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am label", font=("Arial", 20, "bold"))
my_label.pack()



window.mainloop()