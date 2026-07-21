from login import login
from student import student_menu
from faculty import faculty_menu
from course import course_menu
from reports import reports_menu


if login():

    while True:

        print("\n===================================")
        print("   COLLEGE MANAGEMENT SYSTEM")
        print("===================================")

        print("1. Student Module")
        print("2. Faculty Module")
        print("3. Course Module")
        print("4. Reports")
        print("5. Exit")

        try:

            choice = int(input("\nEnter your choice : "))

            if choice == 1:
                student_menu()

            elif choice == 2:
                faculty_menu()

            elif choice == 3:
                course_menu()

            elif choice == 4:
                reports_menu()

            elif choice == 5:
                print("\nThank you for using the system.")
                break

            else:
                print("Invalid Choice!")

        except ValueError:
            print("Please enter numbers only.") 