# Write your code here :-)
import random

health = 10
xp = 10

def attempt(action, min_roll, outcome):
    global health, xp
    roll = random.randint(1,20)
    if roll >=min_roll:
        print(f"{action} succeeded.")
        result=True
    else:
        print(f"{action} Failed.")
        result = False
    score = outcome(result)
    health = health + score[0]
    print (f"Health is now {health}")
    xp=xp + score[1]
    print (f"Experience is now {xp}")

    return result

def eat_bread(success):
    if success:
        return(1,0)
    return (-1, 0)

def fight_ice_weasel(success):
    if success:
        return (0,10)
    return (-10,10)

attempt("eat_bread", 5,eat_bread)
attempt("fight_ice_weasel", 15, fight_ice_weasel)

#using lambda
print ("using lambda...")
print ("========================")

attempt("eating break", 5, lambda success: (1,0) if success else (-1,0))

attempt("fighting ice weasel", 15, lambda success: (0,10) if success else (-10, 10))
