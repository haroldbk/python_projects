# Write your code here :-)
def spam():
    message = "Spam"
    word = "spam"
    for _ in range(100):
        separator = " , "
        message += separator + word
        message += separator
        message += "spam!"
    return message

output = spam()
print(output)


