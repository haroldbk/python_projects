#from FAcebook 
class CarDealership:
    def __init__(self,inventory):
        self.inventory = inventory

    def search(self,car):
        if car not in self.inventory:
            raise ValueError('car not in inventory')
        return f"Found{car} in inventory"
    
dealer = CarDealership(["sedan","Suv","hatchback"])
try:
    print(dealer.search("electric car"))
except ValueError as e:
    print(e)
