books = {}

# Functions 

def add_book():
    book_id = input("Enter Book ID: ")

    if book_id in books:
        print("Book already exists.")
        return

    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    books[book_id] = {
        "Book Name": name,
        "Author": author,
        "Status": "Available"
    }

    print("Book Added Successfully.")


def search_book():
    book_id = input("Enter Book ID: ")

    if book_id in books:
        data = books[book_id]

        print("Book ID :", book_id)
        print("Book Name :", data["Book Name"])
        print("Author :", data["Author"])
        print("Status :", data["Status"])
    else:
        print("Book Not Found.")


def issue_book():
    book_id = input("Enter Book ID: ")

    if book_id in books:
        if books[book_id]["Status"] == "Available":
            books[book_id]["Status"] = "Issued"
            print("Book Issued Successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book Not Found.")


def return_book():
    book_id = input("Enter Book ID: ")

    if book_id in books:
        if books[book_id]["Status"] == "Issued":
            books[book_id]["Status"] = "Available"
            print("Book Returned Successfully.")
        else:
            print("Book is already available.")
    else:
        print("Book Not Found.")


def display_books():
    if len(books) == 0:
        print("No Books Available.")
        return

    for book_id, data in books.items():
        print("---------------------------")
        print("Book ID :", book_id)
        print("Book Name :", data["Book Name"])
        print("Author :", data["Author"])
        print("Status :", data["Status"])


#  Main Menu

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        display_books()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")