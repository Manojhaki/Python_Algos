import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user = input("Press enter to pick a card, or q then enter to quit")
    if user in ["q", "Q"]:
        break
    else:
        pickedCard = random.choice(diamonds)
        index = diamonds.index(pickedCard)

        diamonds.pop(index)

        hand.append(pickedCard)
        print("Your Hand: ", hand)
        print("Remaining Cards: ", diamonds)

if not diamonds:
    print("There are no more cards to pick.")
