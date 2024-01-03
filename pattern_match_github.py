class Special:
    TODAY = 'lasagna'

lunch_order = input("What would you like for lunch? ")
if ' ' in lunch_order:
   lunch_order = lunch_order.split(maxsplit=1)

match lunch_order:
    case Special.TODAY:
        print("Today's special is awesome!")
    case ice_cream if 'ice cream' in ice_cream:
        flavor = ice_cream.replace('ice cream','').strip()
        print(f"Here's your very grown-up {flavor}...lunch.")
    case order:
        print(f"Enjoy your {order}.")






