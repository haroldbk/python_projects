import pandas as pd
import random
class jokes():
    def __init__(self):
            super().__init__()
            self.dataFile= "jokes.xlsx"
            self.df = pd.read_excel(self.dataFile)
            self.index_df=self.df['index']
            self.used_jokes=set()
            
    def ask(self): 
          available = list(set(self.index_df)-self.used_jokes)
          if not available:
                self.used_jokes.clear()
                available=list(self.index_df)
          idx = random.choice(available)     
               
          self.used_jokes.add(idx) 
          self.myIndex = idx       
          question = self.df.loc[self.df['index']==idx,'question'].iloc[0]   
          return idx,question
              
    def my_answer(self,idx):
          answer = self.df.loc[self.df['index']==idx,'answer'].iloc[0]
          return answer
          


