# Write your code here :-)
menu = {"drip":1.95,"cappuccino":2.95, "Americano":2.49}

#def checkout(order):
#try:
#        print(f"Your total is {menu[order]}")
 #   except KeyError:
  #      print(f"That item is not on the menu")

#checkout("drip")
#checkout("tea")

def checkout(order):
    if order in menu:
        print(f"Your total is {menu[order]}")
    else:
       print(f"That item is not on the menu")

checkout("drip")
checkout("tea")
