from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="score : 0", fg="white", bg=THEME_COLOR, font=('arial', 12, 'normal'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text= self.canvas.create_text(150, 130, width=280, text="Question goes here", fill=THEME_COLOR, font=('arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, command=self.true_pressed)
        self.true_btn.grid(row=3, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, command=self.false_pressed)
        self.false_btn.grid(row=3, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached end of the quiz")
            self.canvas.config(bg="white")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)






