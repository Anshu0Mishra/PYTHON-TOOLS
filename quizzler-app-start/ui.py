from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UiGenerator:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="This is trail base",
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_pic = PhotoImage(file="images/true.png")
        wrong_pic = PhotoImage(file="images/false.png")
        self.true_button = Button(image=right_pic, command=self.right_check)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=wrong_pic, command=self.wrong_answer)
        self.false_button.grid(row=2, column=1)
        self.get_next()
        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached end of the question")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def right_check(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def wrong_answer(self):
        # self.feedback()
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next)
