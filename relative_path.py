#relative_path
#from pathlib import PurePath
from pathlib import Path
#path = PurePath('D:\PythonTestSamples\\213AnywhereAve.txt')
path =Path('D:\PythonTestSamples\\213AnywhereAve.txt')

with open(path, 'r') as file:
    print (file.read())            #this is ok assuming file exists

#create empty file is none exists
#path.touch()
