#from https://www.pythontutorial.net/python-basics/python-read-text-file/

with open('D:\odLIve\OneDrive\Drone shots\Mini Pro 3\2024\DJI_0429.SRT') as f:
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


#with open('"D:\odLIve\OneDrive\Drone shots\Mini Pro 3\2024\DJI_0429.SRT"',encoding='utf8') as f:
    for line in f:
        print(line)


    
   