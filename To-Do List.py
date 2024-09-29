import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks_to_file()

def edit_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task_text = task_listbox.get(selected_task_index)
        edited_task = task_entry.get()
        if edited_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, edited_task)
            task_entry.delete(0, tk.END)
            save_tasks_to_file()
        else:
            messagebox.showwarning("Warning", "Please enter a task to edit.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        save_tasks_to_file()

def save_tasks_to_file():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=10, pady=10)
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.grid(row=1, column=0, rowspan=3, padx=10, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=1, column=1, padx=5, pady=5)

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.grid(row=2, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=3, column=1, padx=5, pady=5)

load_tasks_from_file()

root.mainloop()




