# Write your code here :-)

high_score = 10
def score():
    global high_score
    new_score = 465
    if new_score > high_score:  # ERROR unboundLocalError
        print("New High Score")
        high_score = new_score


score()
print (high_score)


