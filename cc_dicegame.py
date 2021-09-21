import random

high_score = 0


def dice_game():
    global high_score
    while(True):
        print("Your current High score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")

        choice = int(input(" Enter your Choice: "))
        if choice == 1:
            sum = 0
            for x in range(0, 2):
                rolls = random.randint(1, 6)
                print("Your", x+1, "dice rolled ", rolls)
                sum = sum+rolls
            if(sum > high_score):
                print("You are our new high scrorer")

                high_score = sum

        else:
            print("Good Bye.")
            break


dice_game()
