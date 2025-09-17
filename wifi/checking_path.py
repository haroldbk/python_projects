import os
import json

sub = "wifi"
fileN = "myData.json"

fPath = os.path.join(os.getcwd(),sub,fileN)
#print(fPath)

cd = os.getcwd()
print(cd)

if not os.path.exists(fileN):
    with open(fileN, 'w') as f:
        json.dump([],f)
  