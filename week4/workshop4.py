class User():
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self):
        name = "name"
        print(name)

    def change_pin(self):
        pin = 321
        print(pin)

    def change_password(self):
        password = "newpassword"
        print(password)


""" Driver Code for Task 1 """

user = User("Bod", 123, "password")

print(user.name)
print(user.pin)
print(user.password)

""" Driver Code for Task 2 """
user = User("Bod", 123, "password")

user.change_name()
user.change_pin()
user.change_password()


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has the balance of :", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(self.name, "has deposited the amount of :", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print(self.name, "has withdrawn the amount of :", amount)

    def transfer_money(self, amount):
        print("jimmy:", self.pin)
        checkpin = input("Enter your PIN: ")

        if (self.pin == checkpin):
            self.balance -= amount
            return True
        else:
            print("Unsuccessful Tansfer.")
            return False

    def request_money(self,):
        checkpin = input("Enter sender's PIN: ")

        checkpass = input("Enter your Password: ")


bankuser = BankUser("bank", 123, "banks")
print(bankuser.name)
print(bankuser.pin)
print(bankuser.password)
print(bankuser.balance)


""" Driver Code for Task 4"""
bankuser = BankUser("bank", 123, "banks")
bankuser.show_balance()

bankuser.deposit(500)
bankuser.show_balance()

bankuser.withdraw(200)
bankuser.show_balance()

""" Driver Code for Task 5"""
king = BankUser("King", 123, "kings")
queen = BankUser("queen", 321, "queens")

queen.deposit(5000)
queen.show_balance()
king.show_balance()


if queen.transfer_money(500) == True:
    king.deposit(500)
    king.show_balance()
