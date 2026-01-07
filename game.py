import tkinter as tk
from tkinter import messagebox
import random

ESCAPE_KEY = "escapekey"


class WordGame:
    def __init__(self, master):
        self.master = master
        self.master.title("X-letter Word Game")
        self.wordlist = []
        self.secret = ""
        self.is_game_on = False
        self.word_length = 6
        self.create_mode_widgets()

    def create_mode_widgets(self):
        self.clear_window()
        self.mode_label = tk.Label(self.master, text="Select word length to play:")
        self.mode_label.pack(pady=10)

        self.length_var = tk.IntVar(value=self.word_length)
        for word_length in (4, 5, 6):
            rb = tk.Radiobutton(
                self.master,
                text=f"{word_length} letters",
                variable=self.length_var,
                value=word_length,
            )
            rb.pack()
        self.start_btn = tk.Button(
            self.master, text="Start Game", command=self.start_game
        )
        self.start_btn.pack(pady=10)

    def start_game(self):
        self.word_length = self.length_var.get()
        filename = f"words_{self.word_length}_letters.txt"
        try:
            with open(filename) as f:
                self.wordlist = [
                    line.strip().lower()
                    for line in f
                    if len(line.strip()) == self.word_length
                ]
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"Could not find {filename}.")
            return
        if not self.wordlist:
            messagebox.showerror(
                "No Words",
                f"No words of length {self.word_length} found in {filename}.",
            )
            return
        self.secret = random.choice(self.wordlist)
        self.is_game_on = True
        self.create_widgets()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def create_widgets(self):
        self.clear_window()
        self.info_label = tk.Label(
            self.master,
            text=f"Guess the {self.word_length}-letter secret word! Type '{ESCAPE_KEY}' to give up.",
        )
        self.info_label.pack(pady=10)

        self.entry = tk.Entry(self.master, font=("Arial", 16), width=10)
        self.entry.pack(pady=5)
        self.entry.focus()
        self.entry.bind("<Return>", lambda event: self.check_guess())

        self.submit_btn = tk.Button(
            self.master, text="Submit Guess", command=self.check_guess
        )
        self.submit_btn.pack(pady=5)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Toggle button for guess history
        self.show_history = True
        self.toggle_btn = tk.Button(
            self.master, text="Hide Guess History", command=self.toggle_history
        )
        self.toggle_btn.pack(pady=2)

        self.guess_history = tk.Text(self.master, height=10, width=40, state="disabled")
        self.guess_history.pack(pady=5)

    def toggle_history(self):
        if self.show_history:
            self.guess_history.pack_forget()
            self.toggle_btn.config(text="Show Guess History")
            self.show_history = False
        else:
            self.guess_history.pack(pady=5)
            self.toggle_btn.config(text="Hide Guess History")
            self.show_history = True

    def check_guess(self):
        if not self.is_game_on:
            return
        guess = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)
        if guess == "":
            return
        if guess == ESCAPE_KEY:
            self.result_label.config(
                text=f"You gave up! The secret word was: {self.secret}"
            )
            self.end_game()
            return
        if len(guess) != self.word_length:
            self.result_label.config(
                text=f"Error: Enter a {self.word_length}-letter word."
            )
            return
        if guess == self.secret:
            self.result_label.config(text="Congratulations! You found the secret word!")
            self.append_history(guess, self.word_length, self.word_length)
            self.end_game()
            return
        letter_match, position_match = self.process_guess(guess, self.secret)
        self.result_label.config(
            text=f"{guess} has {letter_match} letter(s) in secret word, {position_match} in correct position."
        )
        self.append_history(guess, letter_match, position_match)

    def end_game(self):
        self.is_game_on = False
        self.result_label.config(text=f"Game Over! The secret word was: {self.secret}")
        if not self.show_history:
            self.toggle_history()

    def process_guess(self, guess, secret):
        letter_match = 0
        position_match = 0
        X = len(secret)
        is_dup = [False] * X
        # Count letter matches
        for i in range(X):
            for j in range(X):
                if not is_dup[j] and guess[i] == secret[j]:
                    letter_match += 1
                    is_dup[j] = True
                    break
        # Count position matches
        for i in range(X):
            if guess[i] == secret[i]:
                position_match += 1
        return letter_match, position_match

    def append_history(self, guess, letter_match, position_match):
        self.guess_history.config(state="normal")
        self.guess_history.insert(
            tk.END,
            f"{guess}: {letter_match} letter(s) match, {position_match} in position\n",
        )
        self.guess_history.config(state="disabled")
        self.guess_history.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    game = WordGame(root)
    root.mainloop()
