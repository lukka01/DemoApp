def account_exists(username):
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                stored_name, _ = line.strip().split(",")
                if stored_name == username:
                    return True
    except FileNotFoundError:
        return False
    return False


def create_account():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    if account_exists(name):
        print("An account with this username already exists.")
        return

    with open("accounts.txt", "a") as file:
        file.write(f"{name},{password}\n")

    print("Account created successfully")


def login(username, password):
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                stored_name, stored_password = line.strip().split(",")
                if stored_name == username and stored_password == password:
                    return True
    except FileNotFoundError:
        print("No such account exists, please register first.")
    return False



@staticmethod
def sign_in():
    action = input("Do you want to login or register? ").strip().lower()

    if action == "register":
        create_account()
        return False  # registration, no login yet
    elif action == "login":
        uname = input("Username: ")
        pwd = input("Password: ")
        if login(uname, pwd):
            print("Login successful!")
            return True
        else:
            print("Login failed.")
            return False
    else:
        print("Invalid option.")
        return False




