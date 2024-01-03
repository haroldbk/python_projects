# Write your code here :-)
spam=True
eggs = False
potatoes = None

if spam is True:
    print("we have spam")

if spam is not False:
    print ("I don't like spam")
if spam:
    print ("spam, spam, spam")

if potatoes is not None:
    print("Yum")   # Evaluates to false, We never reach the print

if potatoes is None:
    print("Yes, we have no potatoes")

if(eggs is spam):
    print("this won't work")

if(spam != eggs):
   print("they are not equal")

answer = 42
if answer:
    print("evaluates to true")
print(bool(answer))

print("shout \"Cuidado, llamas!\"")

print('shout "cuidado, llamas!"')



print(r"I love backslashes:\ Aren't they cools?")

print("A\nB")
print (r"A\nB")

#formatted strings using f
in_stock = 0
print("This cheese shop has " + str(in_stock) + " types of cheese")

print(f"This cheese shop has {in_stock} types of cheese.")

# print(f"{ord('\')}")  #SyntaxError: f-string expression part cannot include a backslash

print (f"""{ord('"')}""")

newline_ord = ord('\n')
print(f"{newline_ord} ")

