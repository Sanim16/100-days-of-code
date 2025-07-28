import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_generator():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_input.delete(0, 'end')

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate_entry(entry1, entry2):
    if len(entry1) > 0 and len(entry2) >0:
        return True
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return False


def add_password():
    website_to_save = web_input.get()
    email_to_save = email_input.get()
    password_to_save = password_input.get()

    if validate_entry(website_to_save, password_to_save):
        is_ok = messagebox.askokcancel(
            title=website_to_save, message=f"These are the details entered: \nEmail: {email_to_save} "
                                           f"\nPassword: {password_to_save}\n Is it ok to save")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_to_save} | {email_to_save} | {password_to_save}\n")
            web_input.delete(0,'end')
            password_input.delete(0,'end')
            email_input.delete(0,'end')
            email_input.insert(0, "notmyrealemail@yahoo.com")
# ---------------------------- UI SETUP ------------------------------- #

my_screen = tkinter.Tk()
my_screen.title("Password Manager")
my_screen.config(padx=35, pady=35)


logo_image = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column = 1, row=0)

web_label = tkinter.Label(text="Website:")
web_label.grid(column=0, row=1)

web_input = tkinter.Entry(width=38)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = tkinter.Entry(width=38)
email_input.insert(0, "notmyrealemail@yahoo.com")
email_input.grid(column=1, row=2, columnspan=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = tkinter.Entry(width=21)
password_input.grid(column=1, row=3)

pw_button = tkinter.Button(text="Generate Password", command=pw_generator)
pw_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)




my_screen.mainloop()