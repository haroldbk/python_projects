import tkinter as tk
from tkinter import ttk
import pandas  as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
filename = 'pandas/developer.csv'
base = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base,filename)
df=pd.read_csv(csv_path)
x=[1,2,3,4,5,6,7,8,9,10]
r_y=[10,3,6,7,3,9,11,8,4,5]
l_y=[1,2,5,9,8,4,10,7,5,4]

root = tk.Tk()
root.geometry('1200x800')
root.title('2 frames - 2 graphs')
left_frame=tk.Frame(root,bg="lightgray", bd=2, relief="groove")
left_frame.pack(side='left',padx=10,pady=10,fill="both", expand=True)
right_frame=tk.Frame(root,bg="lightgray", bd=2, relief="groove")
right_frame.pack(side='left',fill="both", expand=True,padx=10,pady=10)
l_label=tk.Label(left_frame,text="left frame")
l_label.pack()
r_label=tk.Label(right_frame,text='right frame')
r_label.pack()

#left frame graph
fig1=Figure(figsize=(4,4),dpi=100)
ax1=fig1.add_subplot(111)
ax1.plot(x,l_y,color='royalblue',linewidth=2)
ax1.set_title('left frame graph')
ax1.set_xlabel('X axis')
ax1.set_ylabel('y values')
ax1.grid(True)
#embed fig1 into left frame
canvas1=FigureCanvasTkAgg(fig1,master=left_frame)
canvas1_widget = canvas1.get_tk_widget()
canvas1_widget.pack(fill='both',expand=True)

# Create 2nd graph in right frame
filt=(df['survey_year']==2025) & (df['country']=='United States')
#df.loc[filt,['age','annual_salary_usd']]df.loc[filt,['age','annual_salary_usd']]
data=df.loc[filt,['age','annual_salary_usd']].sort_values(by='age',ascending=False)

ag=data['age']
slry=data['annual_salary_usd']
fig2=Figure(figsize=(4,4),dpi=100)
ax2=fig2.add_subplot(111)
ax2.plot(ag,slry,color='crimson',linewidth=2)
ax2.set_title('salary by age')
ax2.set_xlabel('age')
ax2.set_ylabel('Salary(usd)')
ax2.grid(True)

# embed fig2 into right frame
canvas2 = FigureCanvasTkAgg(fig2,master=right_frame)
canvas2_widget = canvas2.get_tk_widget()
canvas2_widget.pack(fill='both',expand=True)

#add table of salaries
columns = ("age", "salary")
table = ttk.Treeview(right_frame, columns=columns, show="headings")
# Define headings
table.heading("age", text="age")
table.heading("salary", text="salary")
scrollbar = ttk.Scrollbar(right_frame,orient='vertical',command=table.yview)
# Define headings
table.heading("age", text="age")
table.heading('salary',text='salary')
table.column('age',width=180, minwidth=150, stretch=tk.YES)
table.column('salary',width=1, minwidth=1, stretch=tk.YES)


for row in df.itertuples():       
            table.insert("", tk.END, values=(row.age,row.annual_salary_usd))    
table.pack(side='left',expand=True,fill='both')
scrollbar.pack(side='right',fill='y')




root.mainloop()