orders=[
    'carmel macchiato',
    'drip',
    'pumpkin spice latte',
    'cappuccino',
    'americano',
    'mocha latte'
]

new_orders=orders[:]
print (new_orders)

for order in orders:
    new_orders.append(order)
orders=new_orders
print("==========revised orders++++++")
print(orders)