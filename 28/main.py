
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.3
SHORT_BREAK_MIN = 0.1 
LONG_BREAK_MIN = 0.2
reps = 0
tick = ""
timer = None
# ✔

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN , bg= YELLOW)
    global tick
    tick = ""
    tick_marks.config(text=tick, fg= GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60

    reps += 1
    if reps % 2 == 1:
        label_timer.config(text="Work", font=(FONT_NAME, 30), fg=GREEN , bg= YELLOW)
        counter(work_sec)
    elif reps % 8 == 0:
        label_timer.config(text="Break", font=(FONT_NAME, 30), fg=RED , bg= YELLOW)
        counter(long_break_sec)
    else:
        label_timer.config(text="Break", font=(FONT_NAME, 30), fg=PINK , bg= YELLOW)
        counter(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def counter(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec % 10 == count_sec:
        count_sec = "0"+str(count_sec)

    if count_min % 10 == count_min:
        count_min = "0"+str(count_min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, counter, count-1)
    else:
        start_timer()
        # kind of different from the og solution, but if it works: we dont touch!
        if reps % 2 == 0:
            global tick
            tick += "✔" 
            tick_marks.config(text=tick, fg= GREEN, bg=YELLOW)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Tomato")
window.config(padx=90, pady=50, bg=YELLOW)
# def do_thing(a,b,c):
#     print(a,b,c)
# window.after(1000, do_thing, 1, 2, 1)




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,111, image=tomato_img)
timer_text = canvas.create_text(100,129, text = "00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

label_timer = Label()
label_timer.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg= GREEN, bg= YELLOW)
label_timer.grid(row=0, column=1)

start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

tick_marks = Label()
tick_marks.config(text="", fg= GREEN, bg=YELLOW)
tick_marks.grid(row=3, column=1)


window.mainloop()
