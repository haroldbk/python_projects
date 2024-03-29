#finding the correct value where 
#y+9 = x**

i=2
while i < 20:
     # print(y)
     x= i*1.5
     x*=8
     y=i**2
     if x==y:
         print(True)
         print(f"y is {y} and x is {x} and i is {i}")
         break
     else:
        i+=2
    
    