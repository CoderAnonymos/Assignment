import tkinter as tk
from tkinter import ttk
import random
import string

# Main Application Window
window = tk.Tk()
window.title("Advanced Password Generator")
window.geometry("800x650")
window.config(bg="#2b3e50")

# Styling Configuration
style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background="#34495e", foreground="white")
style.configure("TNotebook.Tab", background="#2b3e50", foreground="white", padding=[10, 5])
style.map("TNotebook.Tab", background=[("selected", "#1abc9c")])

# Notebook for Tabs
tab_control = ttk.Notebook(window)
tab_control.pack(expand=1, fill="both")

# Password Generator Tab
password_tab = tk.Frame(tab_control, bg="#34495e")
tab_control.add(password_tab, text="Password Generator")

password_label = tk.Label(password_tab, text="Generated Password:", bg="#34495e", fg="white", font=("Arial", 14))
password_label.pack(pady=(20, 10))

generated_password_display = tk.Label(password_tab, text="", bg="#2c3e50", fg="#1abc9c", font=("Arial", 16, "bold"), relief="solid", padx=10, pady=5)
generated_password_display.pack(pady=(0, 20))

length_label = tk.Label(password_tab, text="Password Length:", bg="#34495e", fg="white", font=("Arial", 14))
length_label.pack(pady=10)

password_length = tk.IntVar(value=12)
password_length_entry = tk.Spinbox(password_tab, from_=8, to=32, textvariable=password_length, font=("Arial", 12))
password_length_entry.pack(pady=10)

use_uppercase = tk.BooleanVar(value=True)
uppercase_checkbox = tk.Checkbutton(password_tab, text="Include Uppercase Letters", variable=use_uppercase, bg="#34495e", fg="white", font=("Arial", 12), selectcolor="#34495e")
uppercase_checkbox.pack(pady=5)

use_numbers = tk.BooleanVar(value=True)
numbers_checkbox = tk.Checkbutton(password_tab, text="Include Numbers", variable=use_numbers, bg="#34495e", fg="white", font=("Arial", 12), selectcolor="#34495e")
numbers_checkbox.pack(pady=5)

use_special = tk.BooleanVar(value=True)
special_checkbox = tk.Checkbutton(password_tab, text="Include Special Characters", variable=use_special, bg="#34495e", fg="white", font=("Arial", 12), selectcolor="#34495e")
special_checkbox.pack(pady=5)

hint_label = tk.Label(password_tab, text="Hints for Password Characters:", bg="#34495e", fg="white", font=("Arial", 14))
hint_label.pack(pady=(20, 10))

hint_entry = tk.Entry(password_tab, bg="#2c3e50", fg="white", font=("Arial", 12))
hint_entry.pack(pady=10, fill="x", padx=20)

purpose_label = tk.Label(password_tab, text="Password Purpose (Optional):", bg="#34495e", fg="white", font=("Arial", 14))
purpose_label.pack(pady=(20, 10))

purpose_entry = tk.Entry(password_tab, bg="#2c3e50", fg="white", font=("Arial", 12))
purpose_entry.pack(pady=10, fill="x", padx=20)

def generate_password():
    length = password_length.get()
    characters = string.ascii_lowercase

    if use_uppercase.get():
        characters += string.ascii_uppercase
    if use_numbers.get():
        characters += string.digits
    if use_special.get():
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    hint = hint_entry.get()
    purpose = purpose_entry.get().lower()

    if purpose:
        if "bank" in purpose:
            password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
            hint = "Contains uppercase letters and numbers for secure banking."
        elif "social" in purpose:
            password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
            hint = "Easy to remember but strong for social media."
        elif "email" in purpose:
            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
            hint = "Highly secure with special characters for email."
        else:
            hint = hint or "General purpose password."

    display_text = f"Password: {password}\n"
    display_text += f"Hint: {hint}\n"
    if purpose:
        display_text += f"Purpose: {purpose.capitalize()}\n"

    generated_password_display.config(text=display_text)

generate_button = tk.Button(password_tab, text="Generate Password", command=generate_password, bg="#1abc9c", fg="white", font=("Arial", 14))
generate_button.pack(pady=20)

# Start Application
window.mainloop()
