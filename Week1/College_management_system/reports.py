import csv
import os

FILE_NAME = "students.csv"

# ------------------------------
# Student Report Card
# ------------------------------
def student_report():

    sid = input("Enter Student ID : ")

    if not os.path.exists(FILE_NAME):
        print("Student File Not Found.")
        return

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    found = False

    for row in reader:

        if len(row) > 0 and row[0] == sid:

            print("\n========== REPORT CARD ==========")
            print("Student ID :", row[0])
            print("Name       :", row[1])
            print("Age        :", row[2])
            print("Department :", row[3])
            print("Marks      :", row[4:9])
            print("Total      :", row[9])
            print("Average    :", row[10])

            found = True
            break

    if not found:
        print("Student Not Found.")

    file.close()

# ------------------------------
# Department-wise Student Count
# ------------------------------
def department_count():

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    next(reader)

    dept = {}

    for row in reader:

        department = row[3]

        if department in dept:
            dept[department] += 1
        else:
            dept[department] = 1

    file.close()

    print("\nDepartment-wise Student Count\n")

    for d in dept:
        print(d, ":", dept[d])

# ------------------------------
# Top 5 Students
# ------------------------------
def top_students():

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    next(reader)

    students = []

    for row in reader:
        students.append(row)

    file.close()

    students.sort(key=lambda x: int(x[9]), reverse=True)

    print("\n========== TOP 5 STUDENTS ==========\n")

    for student in students[:5]:
        print(student[0], student[1], "Total:", student[9])

# ------------------------------
# Failed Students
# ------------------------------
def failed_students():

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    next(reader)

    print("\n========== FAILED STUDENTS ==========\n")

    found = False

    for row in reader:

        average = float(row[10])

        if average < 40:

            print(row[0], row[1], "Average:", average)
            found = True

    if not found:
        print("No Failed Students.")

    file.close()

# ------------------------------
# Overall Average
# ------------------------------
def overall_average():

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    next(reader)

    total = 0
    count = 0

    for row in reader:

        total += float(row[10])
        count += 1

    file.close()

    if count > 0:
        print("\nOverall Average =", total / count)
    else:
        print("No Records Found.")

# ------------------------------
# Rank List
# ------------------------------
def rank_list():

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    next(reader)

    students = []

    for row in reader:
        students.append(row)

    file.close()

    students.sort(key=lambda x: int(x[9]), reverse=True)

    print("\n========== RANK LIST ==========\n")

    rank = 1

    for student in students:

        print(rank, ".", student[1], "-", student[9])

        rank += 1

# ------------------------------
# Reports Menu
# ------------------------------
def reports_menu():

    while True:

        print("\n========== REPORTS ==========")

        print("1. Student Report Card")
        print("2. Department-wise Student Count")
        print("3. Top 5 Students")
        print("4. Failed Students")
        print("5. Overall Average")
        print("6. Rank List")
        print("7. Back")

        try:

            choice = int(input("\nEnter Choice : "))

            if choice == 1:
                student_report()

            elif choice == 2:
                department_count()

            elif choice == 3:
                top_students()

            elif choice == 4:
                failed_students()

            elif choice == 5:
                overall_average()

            elif choice == 6:
                rank_list()

            elif choice == 7:
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please Enter Numbers Only.") 