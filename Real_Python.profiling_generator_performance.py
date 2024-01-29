#https://realpython.com/introduction-to-python-generators/
import sys

num_squared_lc = [i**2 for i in range(10000)]
print( sys.getsizeof(num_squared_lc))

num_squared_gc=(i**2 for i in range(10000))

print(sys.getsizeof(num_squared_gc))
