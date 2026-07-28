import tkinter as tk
from tkinter import ttk
import pandas  as pd

root = tk.Tk()
root.geometry('200x200')
root.title("data table usng Pandas")


data_file = 'pandas/developer.csv'
data=pd.read_csv(data_file)
data.set_index('respondent_id')
#print(data.index)
filt=(data['survey_year']==2026) & (data['country'].str.startswith('United S') 
                                    & (data['languages_used']=='Python') &
                                    (data['employment_status']=='Full-time'))
#filt=(data['NOC']=='USA') & (data['Medal']=='Silver')
#df=data.loc[filt,['Athlete','NOC','Event','Medal']]
df=data.loc[filt,['country','annual_salary_usd','languages_used']].sort_values(by='annual_salary_usd',ascending=False)
#print(data.columns)
columns = ['country','annual_salary_usd','languages_used']
table = ttk.Treeview(root,columns=columns, show='headings')
scrollbar = ttk.Scrollbar(root,orient='vertical',command=table.yview)
# Define headings
#table.heading("MedalistID", text="MedalistID")
table.heading("country", text="country")
table.heading('annual_salary_usd',text='annual salary')
table.heading('languages_used',text='languages')
table.column('country',width=180, minwidth=150, stretch=tk.YES)
table.column('annual_salary_usd',width=1, minwidth=1, stretch=tk.YES)
table.column('languages_used',width=180, minwidth=150, stretch=tk.YES)

for row in df.itertuples():       
            table.insert("", tk.END, values=(row.country,row.annual_salary_usd,row.languages_used))

    
table.pack(side='left',expand=True,fill='both')
scrollbar.pack(side='right',fill='y')


root.mainloop()
