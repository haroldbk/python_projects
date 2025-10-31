#SQLite3 tutorial
#https://docs.python.org/3/library/sqlite3.html#tutorial
import sqlite3
import random
import os
import sys
import time
from datetime import datetime
folder_path =r"D:\python"
db_path = os.path.join(os.getcwd(), "py_scripts.db" )
con=sqlite3.connect(db_path)
cursor = con.cursor()
#cursor.execute("SELECT id,name from Dance_names")

#recs = cursor.fetchall()
#con.close()

""" for rec in recs:
     print (f'id: {rec[0]} name: {rec[1]}') """

for file in os.listdir(folder_path):
   # found = False
    if file.endswith(('.py')):
         #print("file:" , file)
                path = os.path.join(folder_path, file)
                stats = os.stat(path)
                #print(f"size: {stats.st_size}bytes")
                #print(f'Created:{time.ctime(stats.st_ctime)} ')
                #print(f'Modified: {time.ctime(stats.st_mtime)}')
                timestamp = os.path.getctime(path)  
                formatted_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
                print(f'formatted date: {formatted_date}')
                
                cursor.execute("""Insert INTO scripts(script_name,purpose,description,date,location) Values
                (?,?,?,?,?)""",(file,'','',formatted_date,folder_path)) 
                print(path)
               # found = True
           
       
con.commit()
con.close()
print('completed!')

