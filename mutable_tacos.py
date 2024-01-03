# Write your code here :-)
import copy

class Taco:
    def __init__(self, toppings):
        #self.ingredients = toppings  # this will impact all references to Taco ingredients.
        self.ingredients = copy.copy(toppings)

    def add_sauce(self, sauce):
        self.ingredients.append(sauce)


default_toppings = ["lettuce","tomato", "beef"]
mild_taco = Taco(default_toppings)
#hot_taco = Taco(default_toppings)
hot_taco = copy.deepcopy(mild_taco)
hot_taco.add_sauce("Salsa")

print(f"Hot: {hot_taco.ingredients}")
print(f"Mild: {mild_taco.ingredients}")
print(f"Default: {default_toppings}")
