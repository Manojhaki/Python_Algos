def login(databse, username, password):
    if (username, password) in databse.items():
        print("Welcome, ", username)
        return username
    else:
        return ""


def register(database, username):
    if username in database.keys():
        print("Username already registered.")
        return ""
    else:
        print(username, " has been registered")
        return username
