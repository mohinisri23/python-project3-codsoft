import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Create UI Elements
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=60, height=20)
        self.task_listbox.pack(pady=30)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=10)

        self.view_tasks_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_tasks_button.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=10)

    def add_task(self):
        task = simpledialog.askstring("Input", "Enter a new task:")
        if task:
            self.tasks.append(task)
            self.update_task_listbox()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_task = simpledialog.askstring("Input", "Enter the updated task:")
            if new_task:
                self.tasks[selected_index[0]] = new_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to delete.")

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Tasks", "No tasks in the list.")
        else:
            tasks_str = "\n".join(self.tasks)
            messagebox.showinfo("Tasks", tasks_str)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
