import random
import string
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


# Password generation
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(var.get()))
    output.config(text=password)
    output.config(text=password, font=("Ubuntu", 20), justify="center")


# Copy to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output["text"])


# Create themed tkinter window
root = ThemedTk(theme="arc")
root.title("Password Generator")
root.geometry("300x200")

# Password's length
var = tk.IntVar()
var.set(8)

# Length's dropdown menu
dropdown = ttk.Combobox(root, textvariable=var, values=[x for x in range(8, 21)])
dropdown.pack(pady=5)

# "Generate" button
generate_button = ttk.Button(root, text="Generate", command=generate_password)
generate_button.pack(pady=5)

# "Copy" button
copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Output field
output = ttk.Label(root)
output.pack(pady=20)

# Main loop
root.mainloop()
