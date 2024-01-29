specials=[
    'carmel macchiato',
    'drip',
    'pumpkin spice latte',
    'cappuccino',
    'americano',
    'mocha latte'
]

first_iterator = specials.__iter__()
second_iterator = specials.__iter__()
print(type(first_iterator))

item=first_iterator.__next__()
print(item)

item=first_iterator.__next__()
print(item)

item=second_iterator.__next__()
print(item)

print(next(first_iterator))
print(next(first_iterator))
print(next(first_iterator))
print(next(first_iterator))