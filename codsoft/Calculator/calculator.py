import tkinter as tk
from tkinter import messagebox

# Function to update the entry field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to change sign
def change_sign():
    current = entry.get()
    if current:
        if current[0] == '-':
            entry.delete(0)
        else:
            entry.insert(0, '-')

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")

# Set up the main window
root = tk.Tk()
root.title("Advanced Calculator")

# Define colors
bg_color = "#ffffff"
fg_color = "#000000"
button_bg = "#333333"
operator_bg = "#ff9500"
button_fg = "#ffffff"

# Create the entry widget for the display
entry = tk.Entry(root, font=('Helvetica', 24), borderwidth=10, relief=tk.FLAT, justify='right', bg=bg_color, fg=fg_color)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button layout
buttons = [
    ('AC', 1, 0), ('+/-', 1, 1), ('%', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3)
]

# Create buttons dynamically
for (text, row, col, *colspan) in buttons:
    action = lambda x=text: button_click(x) if x not in ('AC', '=', '+/-') else clear() if x == 'AC' else calculate() if x == '=' else change_sign() if x == '+/-' else None
    colspan = colspan[0] if colspan else 1
    bg = operator_bg if text in ('/', '*', '-', '+', '=') else button_bg
    tk.Button(root, text=text, font=('Helvetica', 20), command=action, height=2, width=5, bg=bg, fg=button_fg, borderwidth=0).grid(row=row, column=col, columnspan=colspan, sticky=tk.W+tk.E)

# Set background color
root.configure(bg=bg_color)

# Run the main event loop
root.mainloop()
