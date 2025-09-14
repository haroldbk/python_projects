#https://www.youtube.com/atch?v=NoTM8JciWaQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=8
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
root= Tk()
root.title('create new window')
root.iconbitmap(r'D:\odfb\OneDrive - Microsoft\Pictures\download.ico')
def open_txt():
    text_file=filedialog.askopenfilename(initialdir='files',title="File Open",filetypes=(('Text files','.txt'),))
    text_file=open(text_file,'r')    
    stuff=text_file.read()
    text_file.close()
    my_text.insert(END,stuff)

def save_text():
    text_file=open('files/sample_text.txt','w')
    text_file.write(my_text.get(1.0,END))


my_text=Text(root,width=40,height=10,font=('Helvetica',16))
my_text.pack(pady=20)

open_button=Button(root, text="open text file", command=open_txt)
open_button.pack(pady=20)
save_button=Button(root, text="savve text",command=save_text)
save_button.pack(pady=20)

root.mainloop()