from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


"          === Automated Teller Machine ===          "

name = input("Enter name to register: ")
pin = int(input("Enter PIN: "))
balance = 0
print(name, " has been registered with the starting balance of ", balance, "$.")
while True:
    name_to_validate = input("Enter name :")
    pin_to_validate = int(input("Enter PIN :"))

    if (name == name_to_validate and pin == pin_to_validate):
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:

    atm_menu(name)
    option = int(input("Choose an option: "))
    if option == 1:
        account.show_balance(balance)

    elif option == 2:
        newbalance = account.deposite(balance)
        balance = newbalance
        account.show_balance(balance)
    elif option == 3:
        newbalance = account.withdraw(balance)
        balance = newbalance
        account.show_balance(balance)

    else:
        account.logout(name)
        break
