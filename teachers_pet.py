# teachers_pet
#https://www.pythonforbeginners.com/strings/how-to-use-python-split-function
file = open("D:\\PythonTestSamples\\grades.txt")

grade_data=[]
while (True):
    line=file.readline()
    if not line:
        break
    grade_data.append(line.split(','))
print(grade_data)
file.close()

#this function will loop through student's grades
def calculate_averages(grades_data):
    for grades in grade_data:
         total=0
        # the student's name occupies the first spot
         for i in range(1,len(grades)):
             total +=float(grades[i].strip())
         avg=total/float(len(grades)-1)
         print("{} has an average of {}".format(grades[0],avg))
calculate_averages(grade_data)
        
            
             
             
    
        
        