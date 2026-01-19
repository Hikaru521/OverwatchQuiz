import tkinter as tk
from logic import GuessGame
from data import characters
import random

SECRET = random.choice(list(characters.keys()))
game = GuessGame(characters, SECRET)

root = tk.Tk()
root.title("Overwatch Quiz")
root.geometry("1000x700")

MAX_GUESSES = 6
guess_count = 0

title = tk.Label(root, text="Guess the Character!", font=("Arial", 16))
title.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

entry = tk.Entry(input_frame, width=25)
entry.pack(side=tk.LEFT, padx=5)

history_frame = tk.Frame(root)
history_frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(history_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

history_box = tk.Text(
    history_frame,
    height=10,
    width=50,
    yscrollcommand=scrollbar.set
)

history_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=history_box.yview)

history_box.tag_config("correct", foreground="green")
history_box.tag_config("wrong", foreground="red")
history_box.tag_config("name", foreground="blue")
history_box.tag_config("close", foreground="orange")

feedback = tk.Label(root, text="", font=("Arial", 12))
feedback.pack(pady=5)

def submit_guess():
    global guess_count

    if guess_count >= MAX_GUESSES:
        feedback.config(text="No guesses left! Game over.")
        return

    guess = entry.get().lower()

    result = game.check_guess(guess)
    if result is None:
        feedback.config(text="Not in database!")
        return

    guess_count += 1

    history_box.insert(tk.END, f"{guess.capitalize()}  |  ", "name")

    guess_data = characters[guess]
    secret_data = characters[SECRET]

    all_correct = True

    for key in result:
        guessed_value = guess_data[key]
        correct_value = secret_data[key]

        if guessed_value == correct_value:
            tag = "correct"
        elif guessed_value[2].lower() == correct_value[2].lower():
            tag = "close"
            all_correct = False
        else:
            tag = "wrong"
            all_correct = False

        text = f"{key.capitalize()}: {guessed_value}  "
        history_box.insert(tk.END, text, tag)

    history_box.insert(tk.END, "\n")
    history_box.see(tk.END)

    if all_correct:
        feedback.config(text=f"🎉 You won in {guess_count} guesses!")
        entry.config(state="disabled")
    elif guess_count >= MAX_GUESSES:
        feedback.config(text=f"💀 Game over! The answer was {SECRET.capitalize()}")
        entry.config(state="disabled")
    else:
        feedback.config(
            text=f"Guesses left: {MAX_GUESSES - guess_count}"
        )

    entry.delete(0, tk.END)

button = tk.Button(input_frame, text="Guess", command=submit_guess)
button.pack(side=tk.LEFT)

root.mainloop()
