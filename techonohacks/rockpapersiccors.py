import tkinter as tk
import random

def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create the buttons
rock_button = tk.Button(window, text="Rock", width=10, command=lambda: play_game("rock"))
paper_button = tk.Button(window, text="Paper", width=10, command=lambda: play_game("paper"))
scissors_button = tk.Button(window, text="Scissors", width=10, command=lambda: play_game("scissors"))

# Create a label for displaying the result
result_label = tk.Label(window, text="")

# Arrange the widgets in the window
rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)
result_label.pack(pady=10)

# Start the GUI
window.mainloop()
