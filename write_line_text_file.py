#from https://www.pythontutorial.net/python-basics/python-write-text-file/
lines=["readme","how to write text files in Python"]
more_lines= ['', 'append text files', 'The end']
with open('D:/odLIve\OneDrive/documents/readme.txt','w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

with open('D:/odLIve\OneDrive/documents/readme2.txt','w') as f:
    #f.writelines(lines)
    f.write('\n'.join(lines))
    f.write('\n'.join(more_lines))


try:
    with open('D:/odLIve\OneDrive/documents3/readme2.txt','w') as f:
        
        f.write("create a new text file")
except FileNotFoundError:
        print("the documents3 folder doesn't exst")

with open('D:/odLIve\OneDrive/documents/readme2.txt','x') as f:
     f.write('create a new text file')


    
