students = {}

#function

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists.")
        return

    name = input("Enter Name: ")

    marks = []

    for i in range(1, 6):
        mark = int(input(f"Enter Marks of Subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    students[roll] = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade
    }
 
    print("Student Added Successfully.")


def view_students():
    if len(students) == 0:
        print("No Student Records.")
        return

    for roll, data in students.items():
        print("----------------------------")
        print("Roll Number :", roll)
        print("Name :", data["Name"])
        print("Marks :", data["Marks"])
        print("Total :", data["Total"])
        print("Average :", data["Average"])
        print("Grade :", data["Grade"])


def search_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        data = students[roll]

        print("Name :", data["Name"])
        print("Marks :", data["Marks"])
        print("Total :", data["Total"])
        print("Average :", data["Average"])
        print("Grade :", data["Grade"])
    else:
        print("Student Not Found.")


def update_marks():
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student Not Found.")
        return

    marks = []

    for i in range(1, 6):
        mark = int(input(f"Enter New Marks of Subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    students[roll]["Marks"] = marks
    students[roll]["Total"] = total
    students[roll]["Average"] = average
    students[roll]["Grade"] = grade

    print("Marks Updated Successfully.")


def delete_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        del students[roll]
        print("Student Deleted Successfully.")
    else:
        print("Student Not Found.")


#main menu

while True:

    print("\n===== Student Grade Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()
  
    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")