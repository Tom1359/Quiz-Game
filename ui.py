from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.canvas.grid(columnspan=2, column=0, row=1, pady=20)
        self.scoreboard = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.scoreboard.grid(row=0, column=1)
        self.true_img = PhotoImage(file='images/true.png')
        self.false_img = PhotoImage(file='images/false.png')
        self.true = Button(image=self.true_img, command=self.guess_true)
        self.true.grid(column=0, row=2)
        self.false = Button(image=self.false_img, command=self.guess_false)
        self.false.grid(column=1, row=2)
        self.question_text = self.canvas.create_text(150, 125, text=f"{self.quiz}", fill=THEME_COLOR, font=("Arial", 20, "normal"), width=280)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your score is {self.quiz.score}/10")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def guess_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def guess_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
