#working with lambda
import dis
def add(x,y):
    return x+y
print (type(add))
print(dis.dis(add))