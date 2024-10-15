from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        # Window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Label

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Canva
        self.canva_question = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.some_question = self.canva_question.create_text(150, 125, width=280, text="Some question text",
                                                             fill=THEME_COLOR,
                                                             font=("Arial", 20, "italic"))
        self.canva_question.grid(column=0, row=1, columnspan=2, pady=50)

        # Button
        right_img = PhotoImage(file="/Users/samuelrodriguesmelo/Desktop"
                                    "/TUDO/Python_to_GitHub/is_not_in_github/quizzler-app-start/images/true.png")
        self.button_right = Button(image=right_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_answer)
        self.button_right.grid(column=0, row=2)

        false_img = PhotoImage(file="/Users/samuelrodriguesmelo/Desktop/"
                                    "TUDO/Python_to_GitHub/is_not_in_github/quizzler-app-start/images/false.png")
        self.button_false = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_answer)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question = self.quiz_brain.next_question()
        if self.quiz_brain.still_has_questions():
            self.canva_question.itemconfig(self.some_question, text=question)
            self.score_label.config(text=f"score: {self.quiz_brain.score}")
            self.canva_question.config(bg="white")
        else:
            self.canva_question.itemconfig(self.some_question, text="You've reached the end of the quiz")
            self.canva_question.config(bg="white")
            self.button_right.config(state="disabled")
            self.button_false.config(state="disabled")

    def false_answer(self):
        is_wrong = self.quiz_brain.check_answer("false")
        self.give_feedback(is_wrong)

    def true_answer(self):
        is_right = self.quiz_brain.check_answer("true")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canva_question.config(bg="green")
        else:
            self.canva_question.config(bg="red")
        self.window.after(1000, self.get_next_question)
