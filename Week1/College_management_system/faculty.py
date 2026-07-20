import csv
import os

FILE_NAME = "faculty.csv"


# ------------------------------
# Add Faculty
# ------------------------------
def add_faculty():

    fid = input("Enter Faculty ID : ")
    name = input("Enter Faculty Name : ")
    dept = input("Enter Department : ")
    subject = input("Enter Subject : ")

    file = open(FILE_NAME, "a", newline="")
    writer = csv.writer(file)

    writer.writerow([fid, name, dept, subject])

    file.close()

    print("\nFaculty Added Successfully.")


# ------------------------------
# Display Faculty
# ------------------------------
def display_faculty():

    if not os.path.exists(FILE_NAME):
        print("Faculty File Not Found.")
        return

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    rows = list(reader)

    if len(rows) <= 1:
        print("No Faculty Records Found.")
    else:
        print("\n========== FACULTY DETAILS ==========\n")
        for row in rows:
            print(row)

    file.close()


# ------------------------------
# Search Faculty
# ------------------------------
def search_faculty():

    fid = input("Enter Faculty ID : ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    found = False

    for row in reader:

        if len(row) > 0 and row[0] == fid:
            print("\nFaculty Found")
            print(row)
            found = True
            break

    if not found:
        print("Faculty Not Found.")

    file.close()


# ------------------------------
# Update Faculty
# ------------------------------
def update_faculty():

    fid = input("Enter Faculty ID : ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    faculty = list(reader)

    file.close()

    found = False

    for i in range(1, len(faculty)):

        if faculty[i][0] == fid:

            faculty[i][1] = input("Enter Name : ")
            faculty[i][2] = input("Enter Department : ")
            faculty[i][3] = input("Enter Subject : ")

            found = True
            break

    if found:

        file = open(FILE_NAME, "w", newline="")
        writer = csv.writer(file)

        writer.writerows(faculty)

        file.close()

        print("\nFaculty Updated Successfully.")

    else:
        print("Faculty Not Found.")

# ------------------------------
# Delete Faculty
# ------------------------------
def delete_faculty():

    fid = input("Enter Faculty ID : ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    faculty = list(reader)

    file.close()

    new_list = []

    found = False

    for row in faculty:

        if len(row) > 0 and row[0] == fid:
            found = True
        else:
            new_list.append(row)

    if found:

        file = open(FILE_NAME, "w", newline="")
        writer = csv.writer(file)

        writer.writerows(new_list)

        file.close()

        print("\nFaculty Deleted Successfully.")

    else:
        print("Faculty Not Found.")

# ------------------------------
# Faculty Menu
# ------------------------------
def faculty_menu():

    while True:

        print("\n========== FACULTY MODULE ==========")
        print("1. Add Faculty")
        print("2. Display All Faculty")
        print("3. Search Faculty")
        print("4. Update Faculty")
        print("5. Delete Faculty")
        print("6. Back")

        try:

            choice = int(input("\nEnter Choice : "))

            if choice == 1:
                add_faculty()

            elif choice == 2:
                display_faculty()

            elif choice == 3:
                search_faculty()

            elif choice == 4:
                update_faculty()

            elif choice == 5:
                delete_faculty()

            elif choice == 6:
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please Enter Numbers Only.")