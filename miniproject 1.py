import tkinter as tk
from tkinter import messagebox, simpledialog

class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        return "\n".join(str(workout) for workout in self.workouts)

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for workout in self.workouts:
                file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                date, exercise_type, duration, calories_burned = line.strip().split(',')
                workout = Workout(date, exercise_type, int(duration), int(calories_burned))
                self.workouts.append(workout)

def add_workout(user):
    date = simpledialog.askstring("Date", "Enter the date (YYYY-MM-DD):")
    exercise_type = simpledialog.askstring("Exercise Type", "Enter the exercise type:")
    duration = simpledialog.askinteger("Duration", "Enter the duration (minutes):")
    calories_burned = simpledialog.askinteger("Calories Burned", "Enter the calories burned:")
    workout = Workout(date, exercise_type, duration, calories_burned)
    user.add_workout(workout)
    messagebox.showinfo("Success", "Workout added successfully!")

def view_workouts(user):
    workouts = user.view_workouts()
    if workouts:
        messagebox.showinfo("Workouts", workouts)
    else:
        messagebox.showinfo("Workouts", "No workouts found.")

def save_data(user):
    filename = simpledialog.askstring("Filename", "Enter the filename to save data:")
    if filename:
        user.save_data(filename)
        messagebox.showinfo("Success", "Data saved successfully!")

def load_data(user):
    filename = simpledialog.askstring("Filename", "Enter the filename to load data:")
    if filename:
        user.load_data(filename)
        messagebox.showinfo("Success", "Data loaded successfully!")

def main():
    root = tk.Tk()
    root.title("Workout Tracker")
    root.configure(bg="#2e2e2e")  # Dark background color

    # Style configurations for dark theme
    label_font = ("Arial", 14)
    button_font = ("Arial", 12)
    button_bg = "#4caf50"
    button_fg = "#ffffff"
    entry_bg = "#4d4d4d"
    entry_fg = "#ffffff"
    label_bg = "#2e2e2e"
    label_fg = "#ffffff"

    name_label = tk.Label(root, text="Enter your name:", font=label_font, bg=label_bg, fg=label_fg)
    name_label.pack(pady=5)

    name_entry = tk.Entry(root, width=50, font=label_font, bg=entry_bg, fg=entry_fg)
    name_entry.pack(pady=5)

    age_label = tk.Label(root, text="Enter your age:", font=label_font, bg=label_bg, fg=label_fg)
    age_label.pack(pady=5)

    age_entry = tk.Entry(root, width=50, font=label_font, bg=entry_bg, fg=entry_fg)
    age_entry.pack(pady=5)

    weight_label = tk.Label(root, text="Enter your weight:", font=label_font, bg=label_bg, fg=label_fg)
    weight_label.pack(pady=5)

    weight_entry = tk.Entry(root, width=50, font=label_font, bg=entry_bg, fg=entry_fg)
    weight_entry.pack(pady=5)

    def create_user():
        name = name_entry.get()
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        return User(name, age, weight)

    def handle_add_workout():
        user = create_user()
        add_workout(user)

    def handle_view_workouts():
        user = create_user()
        view_workouts(user)

    def handle_save_data():
        user = create_user()
        save_data(user)

    def handle_load_data():
        user = create_user()
        load_data(user)

    button_bg = "#2196f3"  # Blue color for buttons

    add_button = tk.Button(root, text="Add Workout", command=handle_add_workout, bg=button_bg, fg=button_fg, font=button_font)
    add_button.pack(pady=5)

    view_button = tk.Button(root, text="View Workouts", command=handle_view_workouts, bg=button_bg, fg=button_fg, font=button_font)
    view_button.pack(pady=5)

    save_button = tk.Button(root, text="Save Data", command=handle_save_data, bg=button_bg, fg=button_fg, font=button_font)
    save_button.pack(pady=5)

    load_button = tk.Button(root, text="Load Data", command=handle_load_data, bg=button_bg, fg=button_fg, font=button_font)
    load_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit, bg=button_bg, fg=button_fg, font=button_font)
    exit_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

