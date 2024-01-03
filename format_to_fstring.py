# Write your code here :-)
a= 42
b =64
print("old method using format")
print("{:#x} and {:#o}".format(a,b))

print ("print using f string")
print(f"{a:#x} and {b:#o}")

print ("{0:d}={0:#x} | {1:d}={1:#x}".format(a,b))

print(f"{a:d} = {a:#x} | {b:d}={b:#x}")
