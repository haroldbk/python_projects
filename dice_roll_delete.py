# Write your code here :-)
import random


def make_dice_cup(sides=6, dice=1):
    def roll(dice=dice):
        # nonlocal dice
        if dice < 1:
            return ()
        die = random.randint(1, sides)
        dice -= 1
        return (die, ) + roll(dice - 1)

    return roll

dice_cup = make_dice_cup(sides=6, dice =5)
print (dice_cup)
