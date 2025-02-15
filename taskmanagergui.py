import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    update_task_list()

def delete_task(task_index):
    try:
        tasks.pop(task_index)
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def view_tasks():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        task_list.insert(tk.END, f'{i + 1}. {task["task"]} [{status}]')

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        task_list.insert(tk.END, f'{i + 1}. {task["task"]} [{status}]')

def add_task_ui():
    task = task_entry.get()
    if task:
        add_task(task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

def delete_task_ui():
    try:
        task_index = int(task_entry.get()) - 1
        delete_task(task_index)
        task_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid task number")

def mark_task_completed_ui():
    try:
        task_index = int(task_entry.get()) - 1
        mark_task_completed(task_index)
        task_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid task number")

# Create the main window
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")
root.configure(bg='lightgrey')

# Create widgets
task_entry = tk.Entry(root, font=("Helvetica", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", font=("Helvetica", 14), bg='green', fg='white', command=add_task_ui)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Helvetica", 14), bg='red', fg='white', command=delete_task_ui)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Complete Task", font=("Helvetica", 14), bg='blue', fg='white', command=mark_task_completed_ui)
complete_button.pack(pady=5)

task_list = tk.Listbox(root, font=("Helvetica", 14), width=50, height=10)
task_list.pack(pady=10)

# Initial view of tasks
view_tasks()

# Run the application
root.mainloop()