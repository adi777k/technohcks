import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_display_password():
    length = int(length_entry.get())
    password = generate_password(length)
    password_var.set(password)

root = tk.Tk()
root.title("Random Password Generator")

canvas = tk.Canvas(root, width=400, height=200, bg='lightblue')
canvas.pack(fill='both', expand=True)

length_label = tk.Label(canvas, text="Password Length:")
length_label.place(relx=0.1, rely=0.3, anchor='center')

length_entry = tk.Entry(canvas)
length_entry.place(relx=0.3, rely=0.3, anchor='center')

generate_button = tk.Button(canvas, text="Generate Password", command=generate_and_display_password)
generate_button.place(relx=0.5, rely=0.3, anchor='center')

password_var = tk.StringVar()
password_label = tk.Label(canvas, textvariable=password_var)
password_label.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
