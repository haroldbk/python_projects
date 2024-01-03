# Write your code here :-)
def match_example(value):
    match value:
        case 1:
            print("Value is 1")
        case 2:
            print("Value is 2")
        case _:
            print("Value is something else")

match_example(1)  # Output: Value is 1
match_example(2)  # Output: Value is 2
match_example(3)  # Output: Value is something else


num=input("enter a number")
match_example(num)
