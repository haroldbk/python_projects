# Write your code here :-)
import sys

print(sys.path)

paths=sys.path



print(len(paths))

for i in range(len(paths)):
    print(paths[i-1] +' ' + str(i))

print(sys.version)
