# Write your code here :-)
from collections import deque

customers = deque(['Kyle', 'Denis', 'Simon'])
customers.append('Daniel')
#first, second,third,_ = customers  #the _ ignores the value

first, second, *rest = customers

print(first)
print (second)
print(rest)
