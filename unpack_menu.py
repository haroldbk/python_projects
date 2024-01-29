# Write your code here :-)
menu = {"drip":1.95,"cappuccino":2.95, "Americano":2.49}

#a,b,c = menu.values()
a,b,c = menu.items()
print(a)
print(b)
print(c)

(a_name,a_price),(b_name,b_price),*_=menu.items()
print(a_name)
print(a_price)
print(b_name)
print(b_price)
