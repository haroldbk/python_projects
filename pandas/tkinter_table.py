import tkinter as tk
from tkinter import ttk
import pandas as pd
import csv

root = tk.Tk()
root.title("Tkinter Table Example")
root.geometry("500x200")

columns = ("timestamp", "price")
table = ttk.Treeview(root, columns=columns, show="headings")

# Define headings
table.heading("timestamp", text="timestamp")
table.heading("price", text="price")
with open('bcData.csv','r') as f:
    data=csv.DictReader(f)
    for row in data:       
            table.insert("", tk.END, values=(row['timestamp'],row['price']))
    table.pack(fill=tk.BOTH, expand=True)


root.mainloop()