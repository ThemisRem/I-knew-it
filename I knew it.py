import tkinter as tk
import random

def change_position():
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    yes_button.place(x=x, y=y)

def ask_question():
    question_label.config(text="Are you Clever?")
    yes_button.config(command=change_position)
    no_button.config(command=lambda: question_label.config(text="I Knew it"))

window = tk.Tk()
window.geometry("300x300")

question_label = tk.Label(window, text="")
question_label.pack(pady=50)

yes_button = tk.Button(window, text="Yes", command=change_position)
yes_button.pack(pady=10)

no_button = tk.Button(window, text="No", command=lambda: question_label.config(text="I Knew it"))
no_button.pack(pady=10)

ask_question()

window.mainloop()