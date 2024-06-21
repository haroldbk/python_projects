from tkinter import *
from PIL import Image, ImageFont, ImageDraw

root = Tk()
root.title("Codemy.com - add text to images")
root.geometry('600x650')

#add text to image

def add_it():
	pass


#define image
jazz_dancer = PhotoImage(file=r'D:\odfb\OneDrive - Microsoft\Pictures\radar.png')

my_label = Label(root, image=jazz_dancer)
my_label.pack(pady=20)

#entry box
my_entry=Entry(root,font=('Helvetica',24))
my_entry.pack(pady=20)
#button
my_button = Button(root, text="Add Text to image", command=add_it,font=('Helvetica',24))
my_button.pack(pady=20)

root.mainloop()