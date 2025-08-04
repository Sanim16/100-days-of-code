import tkinter

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = tkinter.Label(text="Score: 0", font=("Arial", 20), fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(bg="white", height=250, width=300, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125, width=280,
            text="Starting text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.true_option)
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.false_option)
        self.false_button.grid(row=2, column=1)

        self.next_question()


        self.window.mainloop()

    def next_question(self):
        self.canvas.configure(bg="white")
        self.score.config(text=f"Score {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_option(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_option(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.next_question)
