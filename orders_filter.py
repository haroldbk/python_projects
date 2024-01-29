orders=[
    'carmel macchiato',
    'medium drip',
    'pumpkin spice latte',
    'cappuccino',
    'americano',
    'mocha latte'
]

drip_orders = list(filter(lambda s : 'drip' in s, orders))

print(f"there are {len(drip_orders)} orders for drip coffee.")

drip_order2=[]

for order in orders:
    if 'drip' in order:
        drip_order2.append(order)

print (f"drip orders 2 {drip_order2} and {len(drip_order2)}.")