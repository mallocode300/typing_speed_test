import tkinter as tk
from tkinter import messagebox
import time
import random

SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "How vexingly quick daft zebras jump!",
    "Sphinx of black quartz, judge my vow.",
    "Waltz, nymph, for quick jigs vex Bud."
]

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")
        self.sample_text = random.choice(SAMPLE_TEXTS)
        self.start_time = None
        self.ended = False

        self.label = tk.Label(root, text="Type the text below as fast as you can:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.text_display = tk.Label(root, text=self.sample_text, wraplength=550, font=("Arial", 12), fg="blue")
        self.text_display.pack(pady=10)

        self.entry = tk.Text(root, height=5, width=70, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_result)
        self.submit_btn.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def check_result(self):
        if self.ended:
            return
        user_input = self.entry.get("1.0", tk.END).strip()
        end_time = time.time()
        if self.start_time is None:
            self.result_label.config(text="Please start typing first!")
            return
        elapsed = end_time - self.start_time
        word_count = len(user_input.split())
        wpm = (word_count / elapsed) * 60 if elapsed > 0 else 0
        correct = user_input == self.sample_text
        if correct:
            self.result_label.config(text=f"Correct! Your speed: {wpm:.2f} WPM")
        else:
            self.result_label.config(text=f"Text does not match. Your speed: {wpm:.2f} WPM")
        self.ended = True
        self.submit_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop() 