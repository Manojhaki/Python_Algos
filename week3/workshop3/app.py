from donations_pkg import homepage
from donations_pkg.homepage import donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""


while True:

    homepage.show_homepage()
    if not authorized_user:
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)
    response = int(input("Choose an option:"))
    if response == 1:
        username = input("Username: ")
        password = input("password: ")

        authorized_user = login(database, username, password)
    elif response == 2:
        username = input("Username: ")
        password = input("password: ")
        authorized_user = register(database, username)
        if not authorized_user:
            database[username] = password
    elif response == 3:
        if not authorized_user:
            print("You are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)

    elif response == 4:
        show_donations(donations)
    elif response == 5:
        print("Good Bye")
        break
