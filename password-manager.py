from cryptography.fernet import Fernet


''' this function is used to generate a key and save it in a file
def generateKey():
    key=Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
generateKey()
'''

def loadKey():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key =loadKey()
fer=Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print(f"User: {user} | Password: {fer.decrypt(password.encode()).decode()}")

def add():
    with open("passwords.txt", "a") as f:
        userName = input("Enter username: ")
        pwd = input("Enter password: ")
        f.write(userName + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones? (view, add) or enter q to quit: "
    ).lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please enter view, add, or q to quit, try again.")
