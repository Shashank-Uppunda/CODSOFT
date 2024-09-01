# Calculator :

# TASK-2 : Design a simple calculator with basic arithmetic operations.
#          Prompt the user to input two numbers and an operation choice.
#          Perform the calculation and display the result.


import tkinter as tk  # Import the tkinter module for creating the GUI
import math           # Import the math module for mathematical functions like square root

# Variable to track whether a new calculation is started
new_calculation = True

def button_click(event):
    global new_calculation
    text = event.widget.cget("text")  # Get the text of the clicked button

    if text == "=":
        calculate_result()
    elif text == "C":
        # Clear the entry widget
        entry.delete(0, tk.END)
        new_calculation = True  # Set new calculation flag
    elif text == "√":
        # Get the current expression from the entry widget
        expression = entry.get()
        try:
            # Compute the square root
            result = math.sqrt(float(expression))
            # Display the result
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            new_calculation = True  # Set new calculation flag
        except Exception as e:
            # Handle errors (e.g., invalid input for square root)
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        if new_calculation:
            # If it's a new calculation, start with the result from previous calculation
            entry.delete(0, tk.END)
            new_calculation = False  # Clear new calculation flag
        entry.insert(tk.END, text)

def calculate_result():
    try:
        # Evaluate the current expression
        expression = entry.get()
        result = eval(expression)
        # Display the result
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        global new_calculation
        new_calculation = True  # Set new calculation flag
    except Exception as e:
        # Handle errors (e.g., invalid expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def on_key_press(event):
    if event.keysym == 'Return':
        calculate_result()

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Set a fixed size for the window
window.geometry("300x400")

# Define the entry widget with a larger font size and padding
entry = tk.Entry(window, font=("Arial", 24), bd=7, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Bind the Enter key to the on_key_press function
window.bind('<Return>', on_key_press)

# Define button labels in rows and columns
button_labels = [
    ('C', '√', '(', ')'),
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Create and place buttons in a grid
row = 1
for button_row in button_labels:
    column = 0
    for label in button_row:
        button = tk.Button(window, text=label, padx=12, pady=12, font=("Arial", 14), width=3, height=2, bd=2, relief="ridge")
        button.grid(row=row, column=column, sticky="nsew")
        button.bind("<Button-1>", button_click)
        column += 1
    row += 1

# Configure row and column weights for resizing
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Run the GUI application
window.mainloop()