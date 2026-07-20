import csv
import os


FILE_NAME = "students.csv"



# Add Student

def add_student():

    try:
        sid = input("Enter Student ID : ")
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        dept = input("Enter Department : ")

        print("\nEnter Marks in 5 Subjects")

        m1 = int(input("Subject 1 : "))
        m2 = int(input("Subject 2 : "))
        m3 = int(input("Subject 3 : "))
        m4 = int(input("Subject 4 : "))
        m5 = int(input("Subject 5 : "))

        total = m1 + m2 + m3 + m4 + m5
        average = total / 5

        file = open(FILE_NAME, "a", newline="")
        writer = csv.writer(file)

        writer.writerow([
            sid,
            name,
            age,
            dept,
            m1,
            m2,
            m3,
            m4,
            m5,
            total,
            average
        ])

        file.close()

        print("\nStudent Added Successfully!")

    except ValueError:
        print("Invalid Input! Please enter numbers correctly.")



# Display Students

def display_students():

    if not os.path.exists(FILE_NAME):
        print("No data file found.")
        return

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    rows = list(reader)

    if len(rows) <= 1:
        print("\nNo Student Records Found.")
        file.close()
        return

    print("\n================ STUDENT DETAILS ================\n")

    for row in rows:
        print(row)

    file.close()
# ------------------------------
# Search Student
# ------------------------------
def search_student():

    sid = input("Enter Student ID to Search : ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    found = False

    for row in reader:

        if len(row) > 0 and row[0] == sid:
            print("\nStudent Found")
            print(row)
            found = True
            break

    if found == False:
        print("Student Not Found.")

    file.close()

# ------------------------------
# Update Student
# ------------------------------
def update_student():

    sid = input("Enter Student ID to Update : ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    students = list(reader)

    file.close()

    found = False

    for i in range(1, len(students)):

        if students[i][0] == sid:

            print("\nEnter New Details")

            students[i][1] = input("Name : ")
            students[i][2] = input("Age : ")
            students[i][3] = input("Department : ")

            m1 = int(input("Subject 1 : "))
            m2 = int(input("Subject 2 : "))
            m3 = int(input("Subject 3 : "))
            m4 = int(input("Subject 4 : "))
            m5 = int(input("Subject 5 : "))

            total = m1 + m2 + m3 + m4 + m5
            average = total / 5

            students[i][4] = m1
            students[i][5] = m2
            students[i][6] = m3
            students[i][7] = m4
            students[i][8] = m5
            students[i][9] = total
            students[i][10] = average

            found = True
            break

    if found:

        file = open(FILE_NAME, "w", newline="")
        writer = csv.writer(file)

        writer.writerows(students)

        file.close()

        print("\nStudent Updated Successfully.")

    else:
        print("Student Not Found.")

# ------------------------------
# Delete Student
# ------------------------------
def delete_student():

    sid = input("Enter Student ID to Delete : ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    students = list(reader)

    file.close()

    new_students = []

    found = False

    for row in students:

        if len(row) > 0 and row[0] == sid:
            found = True

        else:
            new_students.append(row)

    if found:

        file = open(FILE_NAME, "w", newline="")
        writer = csv.writer(file)

        writer.writerows(new_students)

        file.close()

        print("\nStudent Deleted Successfully.")

    else:
        print("Student Not Found.")




# ------------------------------
# Student Menu
# ------------------------------
def student_menu():

    while True:

        print("\n========== STUDENT MODULE ==========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        try:

            choice = int(input("\nEnter Choice : "))

            if choice == 1:
                add_student()

            elif choice == 2:
                display_students()

            elif choice == 3:
                search_student()

            elif choice == 4:
                update_student()

            elif choice == 5:
                delete_student()

            elif choice == 6:
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please Enter Numbers Only.")