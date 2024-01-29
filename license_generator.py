from itertools import product
from string import ascii_uppercase as alphabet
""""
def gen_license_plats():
    for letters in product(alphabet,repeat=3):
        letters = "".join(letters)
        if letters == "GOV":
            continue
        for numbers in range(1000):
            yield f"{letters} {numbers}"

license_plates = gen_license_plats()

#prints all combinations

#for Plate in license_plates:
 #   print(Plate)

registrations={}
def new_registration(owner):
    if owner not in registrations:
        plate = next(license_plates)
        registrations[owner] = plate
        return plate
    return None

for _ in range(4441888):
    next(license_plates)

name = "Jason C. McDonald"
my_plate = new_registration(name)
print(my_plate)
print(registrations[name])
"""

license_plates = (
    f'{"".join(letters)}{number:03}' 
    for letters in product(alphabet, repeat=3)
    for number in range(1000)
)

registrations = {}

def new_registration(owner):
    if owner not in registrations:
        plate = next(license_plates)
        registrations[owner]=plate
        return True
    return False

name = "Peter C. McDonald"
my_plate = new_registration(name)
print(registrations[name])

