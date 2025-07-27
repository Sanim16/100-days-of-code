import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_click():
    global reps
    reps = 0
    my_screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_click():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work Timer", fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break Timer", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break Timer", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(time):
    min_count = math.floor(time/60)
    sec_count = time % 60
    if min_count < 10:
        min_count = f"0{min_count}"
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if time > 0:
        global timer
        timer = my_screen.after(1000, count_down, time-1)
    else:
        start_click()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

my_screen = tkinter.Tk()
my_screen.title("Pomodoro")
my_screen.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)


timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", command=start_click, font=(FONT_NAME, 20), borderwidth=0, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset_click, font=(FONT_NAME, 20), borderwidth=0, highlightthickness=0)
reset_button.grid(column=2, row=2)


check_mark = tkinter.Label(bg=YELLOW, fg=GREEN)
check_mark.grid(column =1, row=3)



my_screen.mainloop()
