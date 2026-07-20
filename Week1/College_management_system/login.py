def login():

    USERNAME = "admin"
    PASSWORD = "1234"

    attempts = 3

    while attempts > 0:

        print("\n===== LOGIN =====")

        username = input("Enter Username : ")
        password = input("Enter Password : ")

        if username == USERNAME and password == PASSWORD:
            print("\nLogin Successful!\n")
            return True

        else:
            attempts -= 1
            print("Invalid Username or Password")

            if attempts > 0:
                print("Attempts Left :", attempts)

    print("\nToo many failed attempts.")
    print("Program Closed.")
    return False