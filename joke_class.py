# Write your code here :-)
class Joke:
    def __init__(self, joke_type):
        if joke_type == "funny":
            self.question = "How can you tell an elephant is in your fridge?"
            self.answer = "There are footprints in the butter"
        elif joke_type =="lethal":
            self.question ="Wenn ist das Nunstick get und slotermeyer?"
            self.answer = "Jai Beiherhund das oder die Flipperwaldt gersput!"
        else:
            self.question = "Why did the chicken cross the street"
            self.answer = "to get to the other side"

    def tell(self):
        print(self.question)
        print (self.answer)

print("what type of joke do you want- funny, lethal or other?")
myType = input()
lethal_joke = Joke(myType)
lethal_joke.tell()


