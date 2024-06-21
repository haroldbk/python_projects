#https://www.youtube.com/atch?v=NoTM8JciWaQ&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=8
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root= Tk()
root.title('create new window')
root.iconbitmap(r'D:\odfb\OneDrive - Microsoft\Pictures\download.ico')

def  open():
	global my_image  #without this it won't display the image or label
	top = Toplevel()
	top.title("An image of Dancer")
	my_image=ImageTk.PhotoImage(Image.open(r"images\jazzDancer.jpg"))
	myLabel=Label(top,image=my_image).pack()
	btn=Button(top,text="close window", command=top.destroy).pack()


btn=Button(root, text="Open new window",command=open).pack()



root.mainloop()