# Write your code here :-)
lunch_order = input("What would you like for lunch?")

match lunch_order:
        case 'Pizza':
            print ("Pizza Time")
        case 'Sandwich':
            print ("Here's your sandwich!")
        case 'Taco':
            print ("Taco - must be Tuesday")
        case 'salad' | 'soup':
            print("Eating healthy, eh")
        case order:
            print(f"enjoy your {order}.")





