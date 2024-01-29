#from https://www.pythontutorial.net/python-basics/python-read-text-file/

with open('D:/odLIve\OneDrive/documents/the_zen_of_python.txt') as f:
    #contents = f.read()
    #print(contents)
   # [print(line.strip()) for line in f.readlines()]
      #while True:     
     #   line = f.readline()
      #  if not line:
       #     break
        #print(line.strip())
    for line in f:
        print(line.strip())


with open('D:/odLIve\OneDrive/documents/quotes.txt',encoding='utf8') as f:
    for line in f:
        print(line)


    
   