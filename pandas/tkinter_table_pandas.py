import tkinter as tk
from tkinter import ttk
import pandas  as pd

root = tk.Tk()
root.geometry('200x200')
root.title("data table usng Pandas")


data_file = 'OlympicsData_3.csv'
data=pd.read_csv(data_file)
data.set_index('MedalistID')
#print(data.index)
filt=(data['NOC']=='USA') & (data['Medal']=='Silver')
df=data.loc[filt,['Athlete','NOC','Event','Medal']]

#print(data.columns)
columns = ['Athlete','NOC','Event','Medal']
table = ttk.Treeview(root,columns=columns, show='headings')
scrollbar = ttk.Scrollbar(root,orient='vertical',command=table.yview)
# Define headings
#table.heading("MedalistID", text="MedalistID")
table.heading("Athlete", text="Athlete")
table.heading('NOC',text='NOC')
table.heading('Event',text='Event')
table.heading('Medal',text='Medal')
table.column('Athlete',width=180, minwidth=150, stretch=tk.YES)
table.column('NOC',width=1, minwidth=1, stretch=tk.YES)
table.column('Event',width=180, minwidth=150, stretch=tk.YES)
table.column('Medal',width=10, minwidth=5, stretch=tk.YES)

for row in df.itertuples():       
            table.insert("", tk.END, values=(row.Athlete,row.NOC,row.Event,row.Medal))

    
table.pack(side='left',expand=True,fill='both')
scrollbar.pack(side='right',fill='y')


root.mainloop()
