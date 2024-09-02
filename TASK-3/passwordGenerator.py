# Password Generator :

# TASK-3 : A password generator is a useful tool that generates strong and
#          random passwords for users. This project aims to create a
#          password generator application using Python, allowing users to
#          specify the length and complexity of the password.
#          User Input: Prompt the user to specify the desired length of the password.
#          Generate Password: Use a combination of random characters to generate a password of the specified length.
#          Display the Password: Print the generated password on the screen.


import tkinter as tk  # Import the Tkinter library for creating the graphical user interface
import random  # Import the random library to generate random values for the password
import string  # Import the string library to access predefined character sets (letters, digits, punctuation)

def generate_password():
    """Generate a random password based on the user-specified length."""
    try:
        # Retrieve the desired length from the entry field
        length_str = length_entry.get()
        
        # Validate if the length is numeric
        if not length_str.isdigit():
            raise ValueError("Length must be a positive integer.")
        
        # Convert the length to an integer
        length = int(length_str)
        
        # Validate the length to ensure it's a positive integer and within the allowed range
        if length <= 0:
            raise ValueError("Length must be positive.")
        if length > 100:  # Set maximum password length to 100 characters
            raise ValueError("Length exceeds maximum limit of 100 characters.")
        
        # Define the characters that will be used in the password
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate a random password by selecting 'length' number of characters from 'characters'
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password in the password_entry field
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_label.config(text="Generated Password:")
    
    except ValueError as ve:
        # Update the label with error messages related to invalid length
        password_label.config(text=f"Error: {ve}")
    except Exception as e:
        # Catch any other unexpected errors
        password_label.config(text=f"Unexpected error: {e}")

# Create the main window
window = tk.Tk()
window.title("Random Password Generator")

# Set the initial size of the window (width x height)
window.geometry("600x300")  # Adjusted to better fit the content

# Define a larger font size for better readability
font_size = 14

# Label for password length input
length_label = tk.Label(window, text="Enter Password Length:", font=("Helvetica", font_size))
length_label.pack(pady=10)

# Entry field for password length with a larger size
length_entry = tk.Entry(window, width=15, font=("Helvetica", font_size), justify="center")
length_entry.pack(pady=5)

# Button to generate password with a larger font size
generate_button = tk.Button(window, text="Generate Random Password", command=generate_password, font=("Helvetica", font_size))
generate_button.pack(pady=10)

# Label to display the generated password or error messages
password_label = tk.Label(window, text="", font=("Helvetica", font_size))
password_label.pack(pady=5)

# Frame to contain the password entry field with padding to prevent spilling
password_frame = tk.Frame(window)
password_frame.pack(pady=10, padx=10)  # Add padding around the frame

# Entry field to display the generated password with increased size for better visibility
password_entry = tk.Entry(password_frame, width=70, font=("Helvetica", font_size), justify="center")
password_entry.pack(padx=10, pady=5)  # Add padding inside the frame for the entry widget

# Run the GUI application
window.mainloop()