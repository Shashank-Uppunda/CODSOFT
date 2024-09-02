# To-Do List :

# TASK-1 : A To-Do List application is a useful project that helps users manage
#          and organize their tasks efficiently. This project aims to create a
#          command-line or GUI-based application using Python, allowing
#          users to create, update, and track their to-do lists


import tkinter as tk  # Import the tkinter module for creating GUI applications
from tkinter import messagebox  # Import messagebox for showing pop-up messages
import os  # Import os module to interact with the operating system

TASKS_FILE = 'tasks.txt'  # Define the file where tasks are stored

def load_tasks():
    """Loads tasks from the file and displays them in the listbox."""
    if os.path.exists(TASKS_FILE):  # Check if the tasks file exists
        with open(TASKS_FILE, 'r') as file:  # Open the file in read mode
            tasks = file.readlines()  # Read all lines from the file
            listbox.delete(0, tk.END)  # Clear existing tasks in the listbox
            for task in tasks:
                listbox.insert(tk.END, task.strip())  # Add each task to the listbox, removing leading/trailing whitespace

def append_task_to_file(task):
    """Appends a new task to the file."""
    with open(TASKS_FILE, 'a') as file:  # Open the file in append mode
        file.write(task + '\n')  # Write the new task to the file followed by a newline

def save_tasks():
    """Saves all tasks in the listbox to the file, overwriting existing tasks."""
    tasks = listbox.get(0, tk.END)  # Get all tasks from the listbox
    with open(TASKS_FILE, 'w') as file:  # Open the file in write mode to overwrite existing content
        for task in tasks:
            file.write(task + '\n')  # Write each task to the file followed by a newline

def add_task():
    """Adds a new task to the listbox and appends it to the file."""
    task = entry.get()  # Get the task text from the entry widget
    if task:  # Check if the task is not empty
        listbox.insert(tk.END, task)  # Add the task to the listbox
        entry.delete(0, tk.END)  # Clear the entry widget
        append_task_to_file(task)  # Append the new task to the file
    else:
        messagebox.showwarning("Warning", "Please enter a task.")  # Show a warning if no task is entered

def delete_task():
    """Deletes the selected task from the listbox and updates the file."""
    selected_task_index = listbox.curselection()  # Get the index of the selected task
    if selected_task_index:  # Check if a task is selected
        listbox.delete(selected_task_index)  # Remove the selected task from the listbox
        save_tasks()  # Save the remaining tasks to the file
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")  # Show a warning if no task is selected

def update_task():
    """Updates the selected task with the new text from the entry widget."""
    selected_task_index = listbox.curselection()  # Get the index of the selected task
    if selected_task_index:  # Check if a task is selected
        new_task = entry.get()  # Get the new task text from the entry widget
        if new_task:  # Check if the new task text is not empty
            listbox.delete(selected_task_index)  # Remove the old task from the listbox
            listbox.insert(selected_task_index, new_task)  # Insert the updated task at the same index
            entry.delete(0, tk.END)  # Clear the entry widget
            save_tasks()  # Save the updated list to the file
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")  # Show a warning if no new task is entered
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")  # Show a warning if no task is selected

def mark_as_done():
    """Marks the selected task as done by appending "(Done)" to it."""
    selected_task_index = listbox.curselection()  # Get the index of the selected task
    if selected_task_index:  # Check if a task is selected
        task = listbox.get(selected_task_index)  # Get the current text of the selected task
        if not task.endswith(" (Done)"):  # Check if the task is not already marked as done
            task += " (Done)"  # Append "(Done)" to the task text
            listbox.delete(selected_task_index)  # Remove the old task from the listbox
            listbox.insert(selected_task_index, task)  # Insert the updated task at the same index
            save_tasks()  # Save the updated list to the file
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")  # Show a warning if no task is selected

def clear_all_tasks():
    """Clears all tasks from the listbox and updates the file."""
    listbox.delete(0, tk.END)  # Remove all tasks from the listbox
    open(TASKS_FILE, 'w').close()  # Clear the content of the tasks file by opening in write mode and closing it immediately

def on_closing():
    """Callback function to handle window close event."""
    save_tasks()  # Save tasks when closing the window
    root.destroy()  # Destroy the window and exit the application

def on_window_open(event):
    """Callback function to handle window open event."""
    load_tasks()  # Load tasks from the file when the window is opened

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")  # Set the title of the window

# Set the size of the window (width x height)
window_width = 650
window_height = 500

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position x and y coordinates to center the window on the screen
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a frame to center the instructions label
frame = tk.Frame(root)
frame.pack(padx=20, pady=10, fill='both', expand=True)

# Create a label for instructions with center alignment
instructions_text = (
    "Instructions:\n\n"
    "1. Enter a task in the text box and click 'Add Task' to add it to the list.\n"
    "2. Select a task from the list and click 'Delete Task' to remove it.\n"
    "3. Select a task, edit the text in the box, and click 'Update Task' to update it.\n"
    "4. Select a task and click 'Mark as Done' to mark it as done.\n"
    "5. Click 'Clear All Tasks' to remove all tasks from the list and clear the tasks file."
)

instructions = tk.Label(frame, text=instructions_text, justify='left', font=('Helvetica', 12), padx=10, pady=5)
instructions.pack(expand=True, fill='both', anchor='center')

# Create an entry widget for task input with larger text and centered
entry = tk.Entry(root, width=35, font=('Helvetica', 14), justify='center')
entry.pack(pady=10)

# Create buttons for various actions with a slightly larger font
add_button = tk.Button(root, text="Add Task", command=add_task, font=('Helvetica', 12))
delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=('Helvetica', 12))
update_button = tk.Button(root, text="Update Task", command=update_task, font=('Helvetica', 12))
mark_as_done_button = tk.Button(root, text="Mark as Done", command=mark_as_done, font=('Helvetica', 12))
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks, font=('Helvetica', 12))  # New button

# Pack buttons with padding in between
add_button.pack(pady=5)
delete_button.pack(pady=5)
update_button.pack(pady=5)
mark_as_done_button.pack(pady=5)
clear_button.pack(pady=5)  # New button

# Create a listbox to display tasks with a larger font and adjusted width
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=15, font=('Courier New', 12))
listbox.pack(pady=10, expand=True)

# Bind the window open event to the function that loads tasks
root.bind("<Map>", on_window_open)  # Bind the "<Map>" event to on_window_open function

# Set the callback for the window close event
root.protocol("WM_DELETE_WINDOW", on_closing)  # Set the protocol to handle the window close event

# Start the main event loop
root.mainloop()  # Start the Tkinter event loop to display the window and handle user interactions