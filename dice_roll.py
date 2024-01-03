# Write your code here :-)
import random
def roll_dice(sides,dice):
    #return random.randint(1,sides)
    return tuple(random.randint(1,sides) for _ in range(dice))


print("Roll for Initiative...")

Player1 = roll_dice(20,2)
Player2 = roll_dice(20,2)
if Player1 >= Player2:
    print(f"Player 1 goes first (rolled {Player1}).")
else:
    print(f"Player 2 goes first(rolled {Player2}). " )

