
def reverse(str):
    strLength = len(str)

    reverseCollect = str[strLength::-1]
    return reverseCollect


name = input("What is your name? ")
print("Your name reversed is:", reverse(name))
