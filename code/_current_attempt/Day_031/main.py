import tkinter
import pandas
import random
from tkinter import messagebox
import sys, os

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
finally:
    word_dict = {row.French: row.English for (index, row) in df.iterrows()}
    learn_dict = df.to_dict(orient="records")


current_card = {}

def random_word():
    global current_card, flip_english

    my_screen.after_cancel(flip_english)
    try:
        current_card = random.choice(learn_dict)
    except IndexError:
        messagebox.showinfo(message="Congrats, you have cleared all the cards. Goodbye!")
        os.remove("data/words_to_learn.csv")
        sys.exit(0)
    else:
        french_word = current_card["French"]
        canvas.itemconfig(language_text, text="French", fill=BACKGROUND_COLOR)
        canvas.itemconfig(word_text, text=french_word, fill=BACKGROUND_COLOR)
        canvas.itemconfig(card_display, image=front_image)
        flip_english = my_screen.after(3000, change_image)


def change_image():
    global current_card

    canvas.itemconfig(card_display, image=back_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

def know_word():
    learn_dict.remove(current_card)
    updated_word_dict = pandas.DataFrame(learn_dict)
    updated_word_dict.to_csv("data/words_to_learn.csv", index=False)
    random_word()


my_screen = tkinter.Tk()
my_screen.config(bg=BACKGROUND_COLOR)
my_screen.title("Flash Cards")
my_screen.config(padx=50, pady=50)


front_image = tkinter.PhotoImage(file="images/card_front.png")
back_image = tkinter.PhotoImage(file="images/card_back.png")
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_display = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'), fill=BACKGROUND_COLOR)
word_text = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'), fill=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tkinter.PhotoImage(file="images/wrong.png")
cross_button = tkinter.Button(image=cross_image, highlightthickness=0, command=random_word)
cross_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=know_word)
right_button.grid(row=1, column=1)

flip_english = my_screen.after(3000, change_image)
random_word()




my_screen.mainloop()
