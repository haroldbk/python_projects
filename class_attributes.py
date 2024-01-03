# Write your code here :-)
class Nutrimatic:
    output="Something almost, but not quite, entirely unlike tea."

    def request(self, beverage):
        return self.output

machine = Nutrimatic()
mug = machine.request("tea")
print (mug)
print (machine.output)
print (Nutrimatic.output)
