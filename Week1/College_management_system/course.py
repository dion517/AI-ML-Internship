import csv
import os

FILE_NAME = "courses.csv"


# ------------------------------
# Add Course
# ------------------------------
def add_course():

    cid = input("Enter Course ID : ")
    cname = input("Enter Course Name : ")

    file = open(FILE_NAME, "a", newline="")
    writer = csv.writer(file)

    writer.writerow([cid, cname, "Not Assigned"])

    file.close()

    print("\nCourse Added Successfully.")


# ------------------------------
# Assign Faculty
# ------------------------------
def assign_faculty():

    cid = input("Enter Course ID : ")

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    courses = list(reader)

    file.close()

    found = False

    for i in range(1, len(courses)):

        if courses[i][0] == cid:

            faculty = input("Enter Faculty Name : ")

            courses[i][2] = faculty

            found = True
            break

    if found:

        file = open(FILE_NAME, "w", newline="")
        writer = csv.writer(file)

        writer.writerows(courses)

        file.close()

        print("\nFaculty Assigned Successfully.")

    else:
        print("Course Not Found.")

# ------------------------------
# Display Courses
# ------------------------------
def display_courses():

    if not os.path.exists(FILE_NAME):
        print("Course File Not Found.")
        return

    file = open(FILE_NAME, "r")
    reader = csv.reader(file)

    rows = list(reader)

    file.close()

    if len(rows) <= 1:
        print("\nNo Courses Found.")
        return

    print("\n========== COURSE DETAILS ==========\n")

    for row in rows:
        print(row)

# ------------------------------
# Course Menu
# ------------------------------
def course_menu():

    while True:

        print("\n========== COURSE MODULE ==========")
        print("1. Add Course")
        print("2. Assign Faculty")
        print("3. Display Courses")
        print("4. Back")

        try:

            choice = int(input("\nEnter Choice : "))

            if choice == 1:
                add_course()

            elif choice == 2:
                assign_faculty()

            elif choice == 3:
                display_courses()

            elif choice == 4:
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please Enter Numbers Only.")