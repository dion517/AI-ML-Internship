import csv
import os

filename = "contacts.csv"


#File Functions

def load_contacts():
    contacts = {}

    if os.path.exists(filename):
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 3:
                    name, phone, email = row
                    contacts[name] = {
                        "Phone": phone,
                        "Email": email
                    }

    return contacts


def save_contacts():
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        for name, data in contacts.items():
            writer.writerow([name, data["Phone"], data["Email"]])


contacts = load_contacts()

# Functions

def add_contact():
    name = input("Enter Name: ")

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email
    }

    save_contacts()
    print("Contact Added Successfully.")


def search_contact():
    name = input("Enter Name: ")

    if name in contacts:
        print("Name :", name)
        print("Phone :", contacts[name]["Phone"])
        print("Email :", contacts[name]["Email"])
    else:
        print("Contact Not Found.")


def update_contact():
    name = input("Enter Name: ")

    if name in contacts:
        phone = input("Enter New Phone Number: ")
        email = input("Enter New Email: ")

        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email

        save_contacts()

        print("Contact Updated Successfully.")
    else:
        print("Contact Not Found.")


def delete_contact():
    name = input("Enter Name: ")

    if name in contacts:
        del contacts[name]

        save_contacts()

        print("Contact Deleted Successfully.")
    else:
        print("Contact Not Found.")


def display_contacts():
    if len(contacts) == 0:
        print("No Contacts Found.")
        return

    for name, data in contacts.items():
        print("-----------------------")
        print("Name :", name)
        print("Phone :", data["Phone"])
        print("Email :", data["Email"])


# ---------------- Main Menu ----------------

while True:

    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        display_contacts()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")