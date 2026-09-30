import pandas as pd
import random
import customtkinter as ctk
import CTkMenuBar
import get_jokes
import texting_edge_tts_v2 as tt
import tkinter as tk
from tkinter import font


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("jokes by AI")
        self.geometry('600x800')
        self.title("jokes by AI")
        self.geometry('600x600')
        self.jokes= get_jokes.jokes()
        bfont=('Arial',30)
        self.fontSize=16
        self.fontName='Helvetica'
        # adding a menu 
        self.menu=CTkMenuBar.CTkMenuBar(self)
        self.file_btn=self.menu.add_cascade('File')
        self.file_dropdown=CTkMenuBar.CustomDropdownMenu(widget=self.file_btn)
        self.file_dropdown.add_option(option="Open",command=lambda:self.menu_label.configure(text="Open"))
        self.file_dropdown.add_option(option='Save', command=lambda:self.menu_label.configure(text="Save"))
        self.file_dropdown.add_option(option="Exit",command=self.destroy)
        # add a menu option to change font name
        self.font_btn=self.menu.add_cascade("Font")
        self.font_dropdown=CTkMenuBar.CustomDropdownMenu(widget=self.font_btn)
        for f in font.families()[:20]:
            self.font_dropdown.add_option(option=f, command=lambda f =f:self.updateFont(f))
        self.num_btn=self.menu.add_cascade('Size')
        self.num_dropdown=CTkMenuBar.CustomDropdownMenu(widget=self.num_btn)
        for n in range(8,48,2):
            self.num_dropdown.add_option(option=str(n),command=lambda n=n:self.updateNum(n))      
  
        #-------------------
        self.menu_label = ctk.CTkLabel(self,text='menu command',width=100,height=50,font=(self.fontName,self.fontSize))
        self.menu_label.pack(padx=20,pady=(0,20),fill='both',expand=True)
        self.askButton= ctk.CTkButton(self,text="the question is:", command=self.ask)
        self.askButton.pack(pady=10)
        #textbox for the question
        self.question_bx = ctk.CTkTextbox(self,width=400,height=140,font=(self.fontName,self.fontSize))
        self.question_bx.pack(padx=20, pady=(0, 20), fill="both", expand=True)
        #get the answer 
        self.getAnswerButton = ctk.CTkButton(self,text='get answer:', command=self.getAnswer)
        self.getAnswerButton.pack(pady=20)
        #dispay the answer
        self.answer_bx = ctk.CTkTextbox(self, width=400,height=140,font=(self.fontName,self.fontSize))
        self.answer_bx.pack(padx=20, pady=(0, 20), fill="both", expand=True)
        #clear both text boxes
        self.clearButton= ctk.CTkButton(self,text='Clear',command=self.clear)
        self.clearButton.pack(pady=20)
        global num
    #menu commands
    #update the font name 
    def updateFont(self,name):
        self.fontName=name
        self.menu_label.configure(font=(self.fontName,self.fontSize))
        self.question_bx.configure(font=(self.fontName,self.fontSize))
        self.answer_bx.configure(font=(self.fontName,self.fontSize))

    #update font size
    def updateNum(self,n):
        self.fontSize=n
        self.menu_label.configure(font=(self.fontName,self.fontSize))
        self.question_bx.configure(font=(self.fontName,self.fontSize))
        self.answer_bx.configure(font=(self.fontName,self.fontSize))
       
   

    def ask(self):
        #self.question_bx.insert("0.0","this is the question")
        self.num,question=self.jokes.ask()        
        self.question_bx.insert('0.0',question)
        spkr='en-US-ChristopherNeural'
        tt.play(question,spkr)
        

    def getAnswer(self):
        #self.answer_bx.insert('0.0','Now the answer')
        theAnswer = self.jokes.my_answer(self.num)
        self.answer_bx.insert('0.0',theAnswer)
        spkr = "en-US-EmmaNeural"  # You can change this to any available voice
        tt.play(theAnswer, spkr)
    def clear(self):
         self.question_bx.delete('1.0','end')
         self.answer_bx.delete('1.0','end')
         tt.play('hahahahahah','en-GB-SoniaNeural')

if __name__=="__main__":
    ctk.set_appearance_mode('System')
    app =App()
    app.mainloop()

