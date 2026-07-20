import random

# Password Generator 

def generate_password():

    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special = "!@#$%^&*"

    characters = ""

    length = int(input("Enter Password Length: "))

    choice = input("Include Uppercase Letters? (yes/no): ")
    if choice.lower() == "yes":
        characters = characters + upper

    choice = input("Include Lowercase Letters? (yes/no): ")
    if choice.lower() == "yes":
        characters = characters + lower

    choice = input("Include Numbers? (yes/no): ")
    if choice.lower() == "yes":
        characters = characters + numbers

    choice = input("Include Special Characters? (yes/no): ")
    if choice.lower() == "yes":
        characters = characters + special

    if characters == "":
        print("Please select at least one option.")
        return

    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    print("Generated Password :", password)


# Password Validator

def validate_password():

    password = input("Enter Password to Validate: ")

    upper = False
    lower = False
    digit = False
    special = False

    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        return

    for ch in password:

        if ch >= 'A' and ch <= 'Z':
            upper = True

        elif ch >= 'a' and ch <= 'z':
            lower = True

        elif ch >= '0' and ch <= '9':
            digit = True

        else:
            special = True

    if upper and lower and digit and special:
        print("Strong Password")
    else:
        print("Weak Password")

        if not upper:
            print("- Missing Uppercase Letter")

        if not lower:
            print("- Missing Lowercase Letter")

        if not digit:
            print("- Missing Number")

        if not special:
            print("- Missing Special Character")


# Main Menu

while True:

    print("\n===== Password Generator & Validator =====")
    print("1. Generate Password")
    print("2. Validate Password")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        generate_password()

    elif choice == "2":
        validate_password()

    elif choice == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")