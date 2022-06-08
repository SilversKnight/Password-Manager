from cryptography.fernet import Fernet

master_pwd = input("Insert the master password:")

def write_key():
    try:
        f = open("key.key")
        f.close()
    except IOError:
        print("Creating encryption key...")
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        
def load_key():
    write_key()
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() + master_pwd.encode()
fer = Fernet(key)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ").encode()

    with open('passwords.txt','a') as file:
        file.write(name + "," + fer.encrypt(pwd).decode() + "\n")

def view():
    with open('passwords.txt','r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user,pwd = data.split(",")
            pwdenc = pwd.encode()
            print("User:",user, "Password:", fer.decrypt(pwdenc))
            
while True:
    mode = input("Select one of the options by inserting the corresponding number.\n1. Add new password\n2. View stored passwords\n3. Quit\n")

    if mode == "1":
        add()
    elif mode == "2":
        view()
    elif mode == "3":
        break
    else:
        print("Invalid input. Please select a valid option.")
        continue
