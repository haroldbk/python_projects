from operator import add
carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]

TAX = 0.1
carts = map(lambda item: [item[0], item[1], item[1] * TAX], carts)

print(list(carts))

cost=[5.94,4.95,5.45,3.45,2,95]
tip=[0.25,1.00,2.00,0.15,0.00]

for total in map(add, cost, tip):
    print(f"{total:.02f}")