from random import choice

colors =[
    'red',
    'greem',
    'blue',
    'silver',
    'white',
    'black'
]
vehicles =[
    'car','truck','semi','motorcycle',None
]

def traffic():
    while True:
        vehicle = choice(vehicles)

        if vehicle is None:
            return

        color = choice(colors)
        yield f"{color} {vehicle}"

count = 0
for count, vehicle in enumerate(traffic(),start=1) :
    print (f"wait for {(vehicle)}...")  
print(f"merged after {count} vehicles!")