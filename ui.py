import tkinter
import os
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.user_input = None
        self.quiz = quiz_brain
        # --- UI ---
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas_1 = tkinter.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.quiz_text = self.canvas_1.create_text(150, 125, width=280, text="", font=("Arial", 20, "italic"))
        self.canvas_1.grid(column=0, row=1, columnspan=2)
        self.canvas_2 = tkinter.Canvas(width=60, height=30, bg=THEME_COLOR, highlightthickness=0)
        self.score_text = self.canvas_2.create_text(30, 15, text="Score: 0", fill="white", font=("Arial", 10, "italic"))
        self.canvas_2.grid(column=1, row=0)
        self.true_image = tkinter.PhotoImage(file=os.path.abspath("./images/true.png"))
        self.true_button = tkinter.Button(image=self.true_image, highlightthickness=0, command=self.user_input_true)
        self.true_button.grid(column=1, row=2)
        self.false_image = tkinter.PhotoImage(file=os.path.abspath("./images/false.png"))
        self.false_button = tkinter.Button(image=self.false_image, highlightthickness=0, command=self.user_input_false)
        self.false_button.grid(column=0, row=2)

        self.update_quiz()
        self.window.mainloop()

    def update_score(self):
        user_was_right = self.quiz.check_answer(self.user_input)
        self.canvas_2.itemconfig(self.score_text, fill="white", text=f"Score: {user_was_right[0]}")
        self.give_feedback(user_was_right[1])

    def update_quiz(self):
        if self.quiz.still_has_questions():
            quiz_text = self.quiz.next_question()
            self.canvas_1.itemconfig(self.quiz_text, fill="black", text=quiz_text)
        else:
            self.canvas_1.itemconfig(self.quiz_text, text="You've reached the end of the questions!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def user_input_false(self):
        self.user_input = f"{False}"
        self.update_score()
        self.window.after(1000, lambda: self.update_quiz())

    def user_input_true(self):
        self.user_input = f"{True}"
        self.update_score()
        self.window.after(1000, lambda: self.update_quiz())

    def give_feedback(self, user_input_true_or_false):
        if user_input_true_or_false:
            self.canvas_1.configure(bg="green")
            self.window.after(1000, lambda: self.canvas_1.configure(bg="white"))
        else:
            self.canvas_1.configure(bg="red")
            self.window.after(1000, lambda: self.canvas_1.configure(bg="white"))

