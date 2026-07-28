import tkinter as  tk
from tkinter import ttk
import csv

root =tk.Tk()
root.title('Treeview with a scrollbar')

frame = ttk.Frame(root)
frame.pack(expand=True,fill='both',padx=10,pady=10)

columns='view_count','likes','ratio'
table = ttk.Treeview(frame,columns=('view_count','likes','ratio'),show='tree headings')
scrollbar = ttk.Scrollbar(frame,orient='vertical',command=table.yview)

# Define headings
table.heading("view_count", text="view_count")
table.heading("likes", text="likes")
table.heading('ratio',text='ratio')
with open('scatter_data.csv','r') as f:
    data=csv.DictReader(f)
    for row in data:       
            table.insert("", tk.END, values=(row['view_count'],row['likes'],row['ratio']))

table.pack(side='left',expand=True,fill='both')
scrollbar.pack(side='right',fill='y')


root.mainloop()