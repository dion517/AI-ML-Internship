expenses = []

# Functions

def add_expense():
    date = input("Enter Date: ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    amount = float(input("Enter Amount: "))

    expense = {
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount
    }

    expenses.append(expense)
    print("Expense Added Successfully.")


def view_expenses():
    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    for expense in expenses:
        print("----------------------------")
        print("Date :", expense["Date"])
        print("Category :", expense["Category"])
        print("Description :", expense["Description"])
        print("Amount :", expense["Amount"])


def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense["Amount"]

    print("Total Expense :", total)


def highest_expense():
    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["Amount"] > highest["Amount"]:
            highest = expense

    print("Highest Expense")
    print("Date :", highest["Date"])
    print("Category :", highest["Category"])
    print("Description :", highest["Description"])
    print("Amount :", highest["Amount"])


def lowest_expense():
    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    lowest = expenses[0]

    for expense in expenses:
        if expense["Amount"] < lowest["Amount"]:
            lowest = expense

    print("Lowest Expense")
    print("Date :", lowest["Date"])
    print("Category :", lowest["Category"])
    print("Description :", lowest["Description"])
    print("Amount :", lowest["Amount"])


def category_summary():
    if len(expenses) == 0:
        print("No Expenses Found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["Category"]
        amount = expense["Amount"]

        if category in summary:
            summary[category] = summary[category] + amount
        else:
            summary[category] = amount

    print("Category-wise Expense Summary")

    for category, amount in summary.items():
        print(category, ":", amount)


#  Main Menu 

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Highest Expense")
    print("5. Lowest Expense")
    print("6. Category-wise Expense Summary")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        highest_expense()

    elif choice == "5":
        lowest_expense()

    elif choice == "6":
        category_summary()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")