import tkinter as tk
from quiz_logic import QuizGame
from questions import questions

game = QuizGame(questions)

root = tk.Tk()
root.title("Quiz Game")
root.geometry("400x300")

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350)
question_label.pack(pady=20)

def click_a():
    handle_answer(button_a["text"])

def click_b():
    handle_answer(button_b["text"])

def click_c():
    handle_answer(button_c["text"])

def click_d():
    handle_answer(button_d["text"])

def handle_answer(choice):
    game.check_answer(choice)

    if game.next_question():
        load_question()
    else:
        show_score()

def load_question():
    q = game.get_current_question()

    question_label.config(text=q["question"])

    button_a.config(text=q["choices"][0])
    button_b.config(text=q["choices"][1])
    button_c.config(text=q["choices"][2])
    button_d.config(text=q["choices"][3])

def show_score():
    question_label.config(
        text=f"Game Over!\nYour Score: {game.score}/{len(questions)}"
    )
    button_a.pack_forget()
    button_b.pack_forget()
    button_c.pack_forget()
    button_d.pack_forget()

button_a = tk.Button(root, text="", width=25, command=click_a)
button_b = tk.Button(root, text="", width=25, command=click_b)
button_c = tk.Button(root, text="", width=25, command=click_c)
button_d = tk.Button(root, text="", width=25, command=click_d)

button_a.pack(pady=5)
button_b.pack(pady=5)
button_c.pack(pady=5)
button_d.pack(pady=5)


load_question()
root.mainloop()
