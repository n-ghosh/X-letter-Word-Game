import tkinter as tk
import random

# Constants
dict_6_letter_words = [
    "abroad", "accept", "access", "across", "acting", "action", "active", "actual", "advice", "advise", "affect", "afford", "afraid", "agency", "agenda", "almost", "always", "amount", "animal", "annual", "answer", "anyone", "anyway", "appeal", "appear", "around", "arrive", "artist", "aspect", "assess", "assist", "assume", "attack", "attend", "august", "author", "avenue", "backed", "barely", "battle", "beauty", "became", "become", "before", "behalf", "behind", "belief", "belong", "berlin", "better", "beyond", "bishop", "border", "bottle", "bottom", "bought", "branch", "breath", "bridge", "bright", "broken", "budget", "burden", "bureau", "button", "camera", "cancer", "cannot", "carbon", "career", "castle", "casual", "caught", "center", "centre", "chance", "change", "charge", "choice", "choose", "chosen", "church", "circle", "client", "closed", "closer", "coffee", "column", "combat", "coming", "common", "comply", "copper", "corner", "costly", "county", "couple", "course", "covers", "create", "credit", "crisis", "custom", "damage", "danger", "dealer", "debate", "decade", "decide", "defeat", "defend", "define", "degree", "demand", "depend", "deputy", "desert", "design", "desire", "detail", "detect", "device", "differ", "dinner", "direct", "doctor", "dollar", "domain", "double", "driven", "driver", "during", "easily", "eating", "editor", "effect", "effort", "eighth", "either", "eleven", "emerge", "empire", "employ", "enable", "ending", "energy", "engage", "engine", "enough", "ensure", "entire", "entity", "equity", "escape", "estate", "ethnic", "exceed", "except", "excess", "expand", "expect", "expert", "export", "extend", "extent", "fabric", "facing", "factor", "failed", "fairly", "fallen", "family", "famous", "father", "fellow", "female", "figure", "filing", "finger", "finish", "fiscal", "flight", "flying", "follow", "forced", "forest", "forget", "formal", "format", "former", "foster", "fought", "fourth", "French", "friend", "future", "garden", "gather", "gender", "german", "global", "golden", "ground", "growth", "guilty", "handed", "handle", "happen", "hardly", "headed", "health", "height", "hidden", "holder", "honest", "impact", "import", "income", "indeed", "injury", "inside", "intend", "intent", "invest", "island", "itself", "jersey", "joseph", "junior", "killed", "labour", "latest", "latter", "launch", "lawyer", "leader", "league", "leaves", "legacy", "length", "lesson", "letter", "lights", "likely", "linked", "liquid", "listen", "little", "living", "losing", "lucent", "luxury", "mainly", "making", "manage", "manner", "manual", "margin", "marine", "marked", "market", "martin", "master", "matter", "mature", "medium", "member", "memory", "mental", "merely", "merger", "method", "middle", "miller", "mining", "minute", "mirror", "mobile", "modern", "modest", "module", "moment", "morris", "mostly", "mother", "motion", "moving", "murder", "museum", "mutual", "myself", "narrow", "nation", "native", "nature", "nearby", "nearly", "nights", "nobody", "normal", "notice", "notion", "number", "object", "obtain", "office", "offset", "online", "option", "orange", "origin", "output", "oxford", "packed", "palace", "parent", "partly", "patent", "people", "period", "permit", "person", "phrase", "picked", "planet", "player", "please", "plenty", "pocket", "police", "policy", "prefer", "pretty", "prince", "prison", "profit", "proper", "proven", "public", "pursue", "raised", "random", "rarely", "rather", "rating", "reader", "really", "reason", "recall", "recent", "record", "reduce", "reform", "regard", "regime", "region", "relate", "relief", "remain", "remote", "remove", "repair", "repeat", "replay", "report", "rescue", "resort", "result", "retail", "retain", "return", "reveal", "review", "reward", "riding", "rising", "robust", "ruling", "safety", "salary", "sample", "saving", "saying", "scheme", "school", "screen", "search", "season", "second", "secret", "sector", "secure", "seeing", "select", "seller", "senior", "series", "server", "settle", "severe", "sexual", "should", "signal", "signed", "silent", "silver", "simple", "simply", "single", "sister", "slight", "smooth", "social", "solely", "sought", "source", "soviet", "speech", "spirit", "spoken", "spread", "spring", "square", "stable", "status", "steady", "stolen", "strain", "stream", "street", "stress", "strict", "strike", "string", "strong", "struck", "studio", "submit", "sudden", "suffer", "summer", "summit", "supply", "surely", "survey", "switch", "symbol", "system", "taking", "talent", "target", "taught", "tenant", "tender", "tennis", "thanks", "theory", "thirty", "though", "threat", "thrown", "ticket", "timely", "timing", "tissue", "toward", "travel", "treaty", "trying", "twelve", "twenty", "unable", "unique", "united", "unless", "unlike", "update", "useful", "valley", "varied", "vendor", "versus", "victim", "vision", "visual", "volume", "walker", "wealth", "weekly", "weight", "wholly", "window", "winner", "winter", "within", "wonder", "worker", "wright", "writer"
]

WORD_LENGTH = 6
ESCAPE_KEY = "escapeKey"

class WordGame:
    def __init__(self, master):
        self.master = master
        self.master.title("X-letter Word Game")
        self.secret = random.choice(dict_6_letter_words)
        self.is_game_on = True
        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.master, text=f"Guess the {WORD_LENGTH}-letter secret word! Type '{ESCAPE_KEY}' to give up.")
        self.info_label.pack(pady=10)

        self.entry = tk.Entry(self.master, font=("Arial", 16), width=10)
        self.entry.pack(pady=5)
        self.entry.focus()
        self.entry.bind('<Return>', lambda event: self.check_guess())

        self.submit_btn = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
        self.submit_btn.pack(pady=5)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.guess_history = tk.Text(self.master, height=10, width=40, state='disabled')
        self.guess_history.pack(pady=5)

        self.reset_btn = tk.Button(self.master, text="Restart Game", command=self.restart_game)
        self.reset_btn.pack(pady=5)

    def check_guess(self):
        if not self.is_game_on:
            return
        guess = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)
        if guess == "":
            return
        if guess == ESCAPE_KEY:
            self.result_label.config(text=f"You gave up! The secret word was: {self.secret}")
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
        self.result_label.config(text=f"{guess} has {letter_match} letter(s) in secret word, {position_match} in correct position.")
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
        self.guess_history.config(state='normal')
        self.guess_history.insert(tk.END, f"{guess}: {letter_match} letter(s) match, {position_match} in position\n")
        self.guess_history.config(state='disabled')
        self.guess_history.see(tk.END)

    def restart_game(self):
        self.secret = random.choice(dict_6_letter_words)
        self.is_game_on = True
        self.result_label.config(text="")
        self.guess_history.config(state='normal')
        self.guess_history.delete(1.0, tk.END)
        self.guess_history.config(state='disabled')
        self.entry.delete(0, tk.END)
        self.info_label.config(text=f"Guess the {WORD_LENGTH}-letter secret word! Type '{ESCAPE_KEY}' to give up.")
        self.entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    game = WordGame(root)
    root.mainloop()
