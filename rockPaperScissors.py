# Rock-Paper-Scissors Game : 
 
# TASK-4 : User Input: Prompt the user to choose rock, paper, or scissors.
#          Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
#          Game Logic: Determine the winner based on the user's choice and the computer's choice.
#          Rock beats scissors, scissors beat paper, and paper beats rock.
#          Display Result: Show the user's choice and the computer's choice.
#          Display the result, whether the user wins, loses, or it's a tie.
#          Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
#          Play Again: Ask the user if they want to play another round.
#          User Interface: Design a user-friendly interface with clear instructions and feedback.


import tkinter as tk  # Import the tkinter module for GUI creation
import random  # Import the random module to generate random choices for the computer

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)  # Return a random choice for the computer

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"  # If choices are the same, it's a tie
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"  # User wins if their choice beats the computer's choice
    else:
        return "You lose!"  # User loses if their choice is beaten by the computer's choice

# Function to handle button clicks
def button_click(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    
    # Update labels with user's choice, computer's choice, and result
    user_choice_label.config(text=f"Your choice: {choice.capitalize()}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
    result_label.config(text=result)
    
    # Update the scores based on the result
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    
    # Update the score label
    score_label.config(text=f"Scores - You: {user_score} | Computer: {computer_score}")

# Function to handle the Exit button
def exit_game():
    root.destroy()  # Close the application

# Initialize the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("600x450")  # Set window size
root.configure(bg="#e0e0e0")  # Set a light gray background color

# Initialize scores
user_score = 0
computer_score = 0

# Create and style the title label
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=('Helvetica', 20, 'bold'), bg="#e0e0e0")
title_label.grid(row=0, column=0, columnspan=3, pady=(20, 10), padx=10)  # Center title with padding

# Create and style the Rock button
rock_button = tk.Button(root, text="Rock", command=lambda: button_click('rock'),
                        font=('Helvetica', 14, 'bold'), bg='#4CAF50', fg='white', padx=20, pady=10)
rock_button.grid(row=1, column=0, padx=20, pady=10)

# Create and style the Paper button
paper_button = tk.Button(root, text="Paper", command=lambda: button_click('paper'),
                         font=('Helvetica', 14, 'bold'), bg='#2196F3', fg='white', padx=20, pady=10)
paper_button.grid(row=1, column=1, padx=20, pady=10)

# Create and style the Scissors button
scissors_button = tk.Button(root, text="Scissors", command=lambda: button_click('scissors'),
                            font=('Helvetica', 14, 'bold'), bg='#FFC107', fg='white', padx=20, pady=10)
scissors_button.grid(row=1, column=2, padx=20, pady=10)

# Create and style the Exit button
exit_button = tk.Button(root, text="Exit", command=exit_game,
                        font=('Helvetica', 14, 'bold'), bg='#f44336', fg='white', padx=20, pady=10)
exit_button.grid(row=2, column=0, columnspan=3, pady=(20, 10))

# Create and style the user's choice label
user_choice_label = tk.Label(root, text="Your choice: ", font=('Helvetica', 14, 'bold'), bg="#e0e0e0")
user_choice_label.grid(row=3, column=0, columnspan=3, pady=10, padx=10)

# Create and style the computer's choice label
computer_choice_label = tk.Label(root, text="Computer chose: ", font=('Helvetica', 14, 'bold'), bg="#e0e0e0")
computer_choice_label.grid(row=4, column=0, columnspan=3, pady=10, padx=10)

# Create and style the result label
result_label = tk.Label(root, text="", font=('Helvetica', 14, 'bold'), bg="#e0e0e0")
result_label.grid(row=5, column=0, columnspan=3, pady=20, padx=10)

# Create and style the score label
score_label = tk.Label(root, text="Scores - You: 0 | Computer: 0", font=('Helvetica', 14, 'bold'), bg="#e0e0e0")
score_label.grid(row=6, column=0, columnspan=3, pady=(10, 20), padx=10)  # Padding for better spacing

# Start the Tkinter event loop
root.mainloop()
