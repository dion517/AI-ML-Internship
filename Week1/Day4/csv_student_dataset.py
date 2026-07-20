import csv
import os

print(os.getcwd())
print(os.listdir())

file = open("Week1/Day4/students.csv", "r")
reader = csv.DictReader(file)

students = []

for row in reader:
    row["Age"] = int(row["Age"])
    row["Marks"] = int(row["Marks"])
    students.append(row)

file.close()

print("\n===== STUDENT DETAILS =====\n")

for student in students:
    print(student)

highest = students[0]["Marks"]
topper = students[0]

for student in students:
    if student["Marks"] > highest:
        highest = student["Marks"]
        topper = student

print("\nHighest Marks :", highest)
print("Student Name :", topper["Name"])

lowest = students[0]["Marks"]
low_student = students[0]

for student in students:
    if student["Marks"] < lowest:
        lowest = student["Marks"]
        low_student = student

print("\nLowest Marks :", lowest)
print("Student Name :", low_student["Name"])

total = 0

for student in students:
    total = total + student["Marks"]

average = total / len(students)

print("\nAverage Marks :", average)

count = 0

for student in students:
    if student["Marks"] > 80:
        count = count + 1

print("\nStudents Scoring Above 80 :", count)

count = 0

for student in students:
    if student["Marks"] < 40:
        count = count + 1

print("Students Scoring Below 40 :", count)

sid = input("\nEnter Student ID : ")

found = False

for student in students:
    if student["Student ID"] == sid:
        print("\nStudent Found")
        print(student)
        found = True

if found == False:
    print("Student Not Found.")

name = input("\nEnter Student Name : ")

found = False

for student in students:
    if student["Name"].lower() == name.lower():
        print("\nStudent Found")
        print(student)
        found = True

if found == False:
    print("Student Not Found.")

department = {}

for student in students:
    dept = student["Department"]

    if dept in department:
        department[dept] = department[dept] + 1
    else:
        department[dept] = 1

print("\nDepartment-wise Student Count\n")

for dept in department:
    print(dept, ":", department[dept])