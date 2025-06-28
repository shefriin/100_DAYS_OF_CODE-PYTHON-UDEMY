from tkinter import *
from tkinter import messagebox
import random
import pyperclip 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]


    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    paswrd = "".join(password_list)

    password_input.insert(0,paswrd)
    pyperclip.copy(paswrd)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("password.txt", "a") as file:
                file.write(website+" | "+email+" | "+password+"\n")
            website_input.delete(0,END)
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
pass_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_logo)
canvas.grid(row=0, column=1)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label()
email_label.config(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="ew")
email_input.insert(0, "example@gmail.com")


password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="ew")

password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()