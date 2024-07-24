import tkinter as tk
from tkinter import messagebox, StringVar, IntVar
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Variables to store user selections
        self.capital_letters = IntVar()
        self.small_letters = IntVar()
        self.numbers = IntVar()
        self.password_length = IntVar()
        self.generated_password = StringVar()

        # Define colors
        self.bg_color = "#D3E3F4"
        self.button_color = "#F1948A"
        self.entry_color = "#E6E6E6"
        self.label_color = "#0B3D91"
        self.button_text_color = "#FFFFFF"

        # Configure root window
        self.root.configure(bg=self.bg_color)

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Character set options
        tk.Checkbutton(self.root, text="Capital letters (A...Z)", variable=self.capital_letters, bg=self.bg_color, fg=self.label_color).grid(row=0, column=0, sticky='w', padx=10, pady=5)
        tk.Checkbutton(self.root, text="Small letters (a...z)", variable=self.small_letters, bg=self.bg_color, fg=self.label_color).grid(row=1, column=0, sticky='w', padx=10, pady=5)
        tk.Checkbutton(self.root, text="Numbers (0...9)", variable=self.numbers, bg=self.bg_color, fg=self.label_color).grid(row=2, column=0, sticky='w', padx=10, pady=5)

        # Password length
        tk.Label(self.root, text="Password Length", bg=self.bg_color, fg=self.label_color).grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.password_length, bg=self.entry_color).grid(row=3, column=1, padx=10, pady=5)

        # Generated password display
        tk.Label(self.root, text="Your Password:", bg=self.bg_color, fg=self.label_color).grid(row=4, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.generated_password, state='readonly', bg=self.entry_color, width=30).grid(row=4, column=1, padx=10, pady=5)

        # Generate button
        tk.Button(self.root, text="Generate Now!", command=self.generate_password, bg=self.button_color, fg=self.button_text_color).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = self.password_length.get()
        if length <= 0:
            messagebox.showerror("Error", "Please enter a valid password length")
            return

        characters = ""
        if self.capital_letters.get():
            characters += string.ascii_uppercase
        if self.small_letters.get():
            characters += string.ascii_lowercase
        if self.numbers.get():
            characters += string.digits

        if not characters:
            messagebox.showerror("Error", "Please select at least one character set")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.generated_password.set(password)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
