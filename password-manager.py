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

masterPwd = input("Enter your master password: ")

key =loadKey() +masterPwd.encode()
fer=Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print(f"User: {user} | Password: {pwd}")

def add():
    with open("passwords.txt", "a") as f:
        user = input("Enter username: ")
        pwd = input("Enter password: ")
        f.write(user + "|" + pwd + "\n")


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
