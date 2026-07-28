import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import tkinter as tk
import numpy as np
import matplotlib.figure
import pandas as pd

def get_data():
    data = pd.read_excel('fruit2.xlsx')
    return data 

def plot():
    ax.clear()
    my_data =get_data()
    unit_cost = my_data['cost']
    fruit=my_data['item']
    quantity=my_data['quantity']
    cost = unit_cost * quantity
    colors=['red','blue','green','purple']
    ax.pie(quantity,labels=fruit,autopct='%1.1f%%',colors=colors)
    ax.set_title('Fruits - by quantity')
 
  
    canvas.draw()

root = tk.Tk()
#fig,ax = plt.subplots()
#size is not right use Figure
fig=matplotlib.figure.Figure()
ax = fig.add_subplot()




#tkinter app
frame = tk.Frame(root)
label=tk.Label(text='Matplotlib + Tkinter')
label.config(font=('Courier',32))
label.pack()


canvas = FigureCanvasTkAgg(fig,master=root)
canvas.get_tk_widget().pack()

frame.pack()

#toolbar = NavigationToolbar2Tk(canvas,frame,pack_toolbar=False)
#toolbar.update()
#toolbar.pack(anchor="w",fill=tk.X)

canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
toolbar = NavigationToolbar2Tk(canvas,frame)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)


button = tk.Button(frame,text='Plot Graph', command=plot).pack(pady=10)


root.mainloop()
