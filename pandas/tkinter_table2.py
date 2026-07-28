import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter Table Example")
root.geometry("500x200")

# Define columns
columns = ("first_name", "last_name", "email")
table = ttk.Treeview(root, columns=columns, show="headings")

# Define headings
table.heading("first_name", text="First Name")
table.heading("last_name", text="Last Name")
table.heading("email", text="Email")

# Add data
data = [
    ("John", "Doe", "john.doe@example.com"),
    ("Jane", "Smith", "jane.smith@example.com"),
    ("Bob", "Johnson", "bob.j@example.com")
]

for row in data:
    table.insert("", tk.END, values=row)

table.pack(fill=tk.BOTH, expand=True)
root.mainloop()