# Write your code here :-)
import random

def roll_dice(*dice):
    return tuple(random.randint(1,d) for d in dice)


dice_cup = roll_dice(6,6,6,6,6,6)
print (dice_cup)

bunch_o_dice = roll_dice(20,6,8,4)
print (bunch_o_dice)

#alternative using recursive
print ("alternative...")

def roll_dice2 (*dice):
    if dice:
        roll=random.randint(1,dice[0])
        return (roll,) + roll_dice2(*dice[1:])
    return()

dice_cup = roll_dice2(6,6,6,6,6,6)
print (dice_cup)

bunch_o_dice = roll_dice2(20,6,8,4)
print (bunch_o_dice)

# keyword-only parameters
#=====================
print("keyword only parameters")

print("------------------------")

def roll_dice3 (*, sides = 6, dice =1):
    return tuple(random.randint(1,sides) for _ in range(dice))

dice_cup = roll_dice3(sides=6, dice=5)
print (dice_cup)
