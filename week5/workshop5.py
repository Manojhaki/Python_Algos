import random


def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)
    print("Random Number: ", random_number)
    while (tries != 0):
        print("You have ", tries, " left")
        guess = int(input("Guess a number: "))
        if (guess == random_number):
            print("You got it.")
            break
        elif (guess < random_number):
            print("Guess a little higher.")
        elif (guess > random_number):
            print("Guess a little lower.")
        else:
            print("You Loose.")
        tries -= 1


#guess_random_number(3, 0, 5)


def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    print("Random Number: ", random_number)

    list_random_number = range(start, stop+1)
    for x in range(len(list_random_number)):
        print(list_random_number[x])

    for guess in list_random_number:
        print("Tries", tries)
        print("guess", guess)
        tries -= 1
        if guess == random_number:
            print("You got it.")
            break
        elif tries == 0:
            print("You Loose.")
            break
        elif guess < random_number:
            print("Guess a little higher.")


#guess_random_num_linear(3, 0, 5)


def guess_random_num_binary(start, stop):
    random_number = random.randint(start, stop)
    print("Random Number: ", random_number)
    tries = 5
    list_random_number = range(start, stop+1)
    lower_bound = 0
    upper_bound = len(list_random_number) - 1

    while lower_bound <= upper_bound:
        print("Tries:  ", tries)
        tries -= 1
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = list_random_number[pivot]

        print("current guess:   ", pivot_value)
        if pivot_value == random_number:
            print("Right. You Got it.")
            return pivot
        elif tries == 0:
            print("You have emptied your tries.")
            break
        if pivot_value > random_number:
            print("Wrong. Guessing lower.")
            upper_bound = pivot - 1
        else:
            print("Wrong. Guessing higher.")
            lower_bound = pivot + 1

    return -1


guess_random_num_binary(10, 100)
