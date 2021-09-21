

def show_balance(balance):
    print("Your current balance is : ", balance, "$")


def deposite(balance):
    amount = float(input("Enter amount to deposit:"))
    return balance+amount


def withdraw(balance):
    amount = float(input("Enter amount to withdraw:"))
    return balance-amount


def logout(name):
    print("Good Bye, ", name, "!")
