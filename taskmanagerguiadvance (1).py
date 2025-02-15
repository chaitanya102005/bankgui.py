import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring

# Task list
tasks = []

def add_task():
    task = task_entry.get()
    if task:
        due_date = askstring("Due Date", "Enter due date (YYYY-MM-DD) or leave blank:")
        priority = askstring("Priority", "Enter priority (High/Medium/Low) or leave blank:")
        category = askstring("Category", "Enter category or leave blank:")
        task_details = {
            "task": task,
            "completed": False,
            "due_date": due_date if due_date else "No due date",
            "priority": priority if priority else "No priority",
            "category": category if category else "No category"
        }
        tasks.append(task_details)
        update_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def complete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["completed"] = True
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def search_tasks():
    keyword = search_entry.get()
    if keyword:
        search_results = [task for task in tasks if keyword.lower() in task["task"].lower()]
        task_listbox.delete(0, tk.END)
        for task in search_results:
            status = "Completed" if task["completed"] else "Pending"
            task_listbox.insert(tk.END, f'{task["task"]} [{status}] - Due: {task["due_date"]} - Priority: {task["priority"]} - Category: {task["category"]}')
    else:
        messagebox.showwarning("Warning", "Search keyword cannot be empty!")

def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f'{task["task"]} [{status}] - Due: {task["due_date"]} - Priority: {task["priority"]} - Category: {task["category"]}')

def clear_all_tasks():
    tasks.clear()
    update_tasks()

# Create the main window
root = tk.Tk()
root.title("Task Manager")
root.configure(bg="#2E2E2E")  # Set background color
root.geometry("500x500")

# Styles
button_style = {"font": ("Arial", 12), "fg": "white", "width": 20, "bd": 2, "relief": "raised"}
input_style = {"font": ("Arial", 14), "width": 40, "bg": "#333333", "fg": "white", "insertbackground": "white", "highlightthickness": 1, "highlightbackground": "#FFFFFF", "highlightcolor": "#FFFFFF"}

# UI Components
task_label = tk.Label(root, text="Enter a task:", font=("Arial", 14, "bold"), fg="white", bg="#2E2E2E")
task_label.pack()

task_entry = tk.Entry(root, **input_style)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", **button_style)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#F44336", **button_style)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Complete Task", command=complete_task, bg="#2196F3", **button_style)
complete_button.pack(pady=5)

search_label = tk.Label(root, text="Search tasks:", font=("Arial", 14, "bold"), fg="white", bg="#2E2E2E")
search_label.pack()

search_entry = tk.Entry(root, **input_style)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_tasks, bg="#FF9800", **button_style)
search_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks, bg="#9C27B0", **button_style)
clear_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=60, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

# Start the main loop
root.mainloop()
