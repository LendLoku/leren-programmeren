import random
import string
import tkinter as tk

def generate_password(length, use_numbers=True, use_symbols=True):
    characters = string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_click():
    password_length = int(length_entry.get())
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    generated_password = generate_password(password_length, include_numbers, include_symbols)
    password_label.config(text="Generated Password: " + generated_password)

# Create a tkinter window
root = tk.Tk()
root.title("Password Generator")

# Label and Entry for password length
length_label = tk.Label(root, text="Enter the desired password length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for including numbers and symbols
numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include numbers?", variable=numbers_var)
numbers_checkbox.pack()
numbers_var.set(True)  # Default to including numbers

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include symbols?", variable=symbols_var)
symbols_checkbox.pack()
symbols_var.set(True)  # Default to including symbols

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password_button_click)
generate_button.pack()

# Label to display the generated password
password_label = tk.Label(root, text="")
password_label.pack()

# Start the GUI event loop
root.mainloop() 