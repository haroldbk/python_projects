orders=[
    'carmel macchiato',
    'medium drip',
    'pumpkin spice latte',
    'cappuccino',
    'americano',
    'mocha latte',
    'dark roast drip',
    'french press'
]

def brew(order):
    print(f"Making {order}...")
    return order

for order in map(brew,orders):
    print (f"One {order} is ready!")