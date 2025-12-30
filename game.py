import tkinter as tk
import random

WORD_LENGTH = 6
ESCAPE_KEY = "escapekey"


class WordGame:
    def __init__(self, master, wordlist):
        self.master = master
        self.master.title("X-letter Word Game")
        self.wordlist = wordlist
        self.secret = random.choice(wordlist)
        self.is_game_on = True
        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(
            self.master,
            text=f"Guess the {WORD_LENGTH}-letter secret word! Type '{ESCAPE_KEY}' to give up.",
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

        self.guess_history = tk.Text(self.master, height=10, width=40, state="disabled")
        self.guess_history.pack(pady=5)

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
            self.is_game_on = False
            return
        if len(guess) != WORD_LENGTH:
            self.result_label.config(text=f"Error: Enter a {WORD_LENGTH}-letter word.")
            return
        if guess == self.secret:
            self.result_label.config(text="Congratulations! You found the secret word!")
            self.append_history(guess, WORD_LENGTH, WORD_LENGTH)
            self.is_game_on = False
            return
        letter_match, position_match = self.process_guess(guess, self.secret)
        self.result_label.config(
            text=f"{guess} has {letter_match} letter(s) in secret word, {position_match} in correct position."
        )
        self.append_history(guess, letter_match, position_match)

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
    with open("words_6_letters.txt") as f:
        wordlist = [
            line.strip().lower() for line in f if len(line.strip()) == WORD_LENGTH
        ]
    root = tk.Tk()
    game = WordGame(root, wordlist)
    root.mainloop()
