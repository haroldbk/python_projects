specials=[
    'carmel macchiato',
    'drip',
    'pumpkin spice latte',
    'cappuccino',
    'americano',
    'mocha latte'
]

iterator = iter(specials)
while True:
    try:
        item= next(iterator)
    except StopIteration:
        break
    else:
        print(item)
    
 
for item in specials:
    print(item)