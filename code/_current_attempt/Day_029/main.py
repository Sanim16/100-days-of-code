import tkinter
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

DEFAULT_EMAIL = "notmyrealemail@yahoo.com"

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

        new_data = {website_to_save: {
            "Email": email_to_save,
            "Password": password_to_save
        }}

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data_dictionary = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=2)
            else:
                with open("data.json", "w") as file:
                    data_dictionary.update(new_data)
                    json.dump(data_dictionary, file, indent=2)
            web_input.delete(0,'end')
            password_input.delete(0,'end')
            email_input.delete(0,'end')
            email_input.insert(0, DEFAULT_EMAIL)

# ---------------------------- FIND PASSWORD ------------------------------- #
def search_pw_file():
    website_to_search = web_input.get()

    if validate_entry(website_to_search, "text"):
        is_ok = messagebox.askokcancel(
            title=website_to_search, message=f"You would like to retrieve the details for {website_to_search}")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data_dictionary = json.load(file)
            except FileNotFoundError:
                messagebox.showinfo(title="Error", message="No datafile found")
            else:
                if website_to_search in data_dictionary:
                    email = data_dictionary[website_to_search]["Email"]
                    password = data_dictionary[website_to_search]["Password"]
                    messagebox.showinfo(title=website_to_search, message=f"Email: {email}\n Password: {password}")
                else:
                    messagebox.showinfo(title="oops", message="No details for the website exists")
            web_input.delete(0,'end')
            password_input.delete(0,'end')
            email_input.delete(0,'end')
            email_input.insert(0, DEFAULT_EMAIL)
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

web_input = tkinter.Entry(width=21)
web_input.grid(column=1, row=1)
web_input.focus()

search_button = tkinter.Button(text="Search", width=13, command=search_pw_file)
search_button.grid(column=2, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = tkinter.Entry(width=38)
email_input.insert(0, DEFAULT_EMAIL)
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