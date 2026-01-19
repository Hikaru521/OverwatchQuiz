import tkinter as tk
from logic import GuessGame
from data import characters

SECRET = "Rammatra"

game = GuessGame(characters, SECRET)

root = tk.Tk()
root.title("Overwatch Quiz")
root.geometry("400x300")

title = tk.Label(root, text="Guess the Character!", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

feedback = tk.Label(root, text="", font=("Arial", 12))
feedback.pack(pady=10)

def submit_guess():
    guess = entry.get()
    result = game.check_guess(guess)

    if result is None:
        feedback.config(text="Not in database!")
        return

    text = ""
    for key, correct in result.items():
        status = "✅" if correct else "❌"
        text += f"{key.capitalize()}: {status}\n"

    feedback.config(text=text)

    if all(result.values()):
        feedback.config(text="🎉 You guessed it correctly!")

    entry.delete(0, tk.END)

button = tk.Button(root, text="Guess", command=submit_guess)
button.pack(pady=5)

root.mainloop()
