#Defining_a_decorator
#https://realpython.com/python-lambda/

def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func:{f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
    return wrap

#applying decorator to a function
@trace
def add_two(x):
    return x+2
#calling the decorated function
add_two(3)

#applying the decorator to a lambda
print((trace(lambda x:x**2))(3))

list(map(trace(lambda x:x*2),range(3)))




