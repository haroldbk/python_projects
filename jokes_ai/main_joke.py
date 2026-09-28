import pandas as pd
import random
import customtkinter as ctk
import get_jokes
import texting_edge_tts_v2 as tt


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("jokes by AI")
        self.geometry('600x800')
        self.title("jokes by AI")
        self.geometry('600x600')
        self.jokes= get_jokes.jokes()

        self.askButton= ctk.CTkButton(self,text="the question is:", command=self.ask)
        self.askButton.pack(pady=10)
        #textbox for the question
        self.question_bx = ctk.CTkTextbox(self,width=400,height=140)
        self.question_bx.pack(pady=20)
        #get the answer 
        self.getAnswerButton = ctk.CTkButton(self,text='get answer:', command=self.getAnswer)
        self.getAnswerButton.pack(pady=20)
        #dispay the answer
        self.answer_bx = ctk.CTkTextbox(self, width=400,height=140)
        self.answer_bx.pack(pady=20)
        #clear both text boxes
        self.clearButton= ctk.CTkButton(self,text='Clear',command=self.clear)
        self.clearButton.pack(pady=20)
        global num

    def ask(self):
        #self.question_bx.insert("0.0","this is the question")
        self.num,question=self.jokes.ask()        
        self.question_bx.insert('0.0',question)
        tt.play(question)
        

    def getAnswer(self):
        #self.answer_bx.insert('0.0','Now the answer')
        theAnswer = self.jokes.my_answer(self.num)
        self.answer_bx.insert('0.0',theAnswer)
        tt.play(theAnswer)
    def clear(self):
         self.question_bx.delete('1.0','end')
         self.answer_bx.delete('1.0','end')


if __name__=="__main__":
    ctk.set_appearance_mode('System')
    app =App()
    app.mainloop()

