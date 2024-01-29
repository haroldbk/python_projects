#read_house_open
#"D:\\odfb\OneDrive - Microsoft\\Documents\\keys\\keysgenerated.txt"
#"D:\\PythonTestSamples\\213AnywhereAve.txt"
tfile="D:\\PythonTestSamples\\78SomewhereRd.txt"

"""
house = open(tfile)

print(house.read())
house.close
"""
""""
with open(tfile,'r') as house:
    lines = house.readlines()
    for line in lines:
        print(line.strip())
"""
"""
    contents = house.read(20)
    print(type(contents))
    print(contents)
    #print contents as a raw string use repr()
    print(repr(contents))
"""
"""
    line1=house.readline()
    line2=house.readline()
    print(repr(line1))
    print(repr(line2))
  """
with open(tfile, 'r+') as RealEstateListing:
    contents =RealEstateListing.readlines()
    new_contents=[]

    for line in contents:
        line = line.replace('Tiny','Cozy')
        line = line.replace('Needs repairs','Full of Potential')
        line = line.replace('Small','Compact')
        line = line.replace('old storage shed','detached workshop')
        line = line.replace('Built on ancient burial ground','Unique atmosphere')
        new_contents.append(line)
    RealEstateListing.seek(0)
    RealEstateListing.writelines(new_contents)
    RealEstateListing.truncate()
  
