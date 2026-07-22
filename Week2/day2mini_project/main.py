from utils import load_data

from operations import (
display_students,
search_by_id,
search_by_name,
filter_department
)

from reports import (
top_students,
bottom_students,
department_average,
pass_percentage,
fail_percentage,
export_report
)

df = load_data(r"C:\Users\DionneJudeNunez\Documents\AI-ML-Internship\Week2\day2mini_project\student.csv")

while True:

    print("\n===== Student Performance Analyzer =====")
    print("1. Display All Students")
    print("2. Search by ID")
    print("3. Search by Name")
    print("4. Filter by Department")
    print("5. Top 5 Students")
    print("6. Bottom 5 Students")
    print("7. Department-wise Average")
    print("8. Pass Percentage")
    print("9. Fail Percentage")
    print("10. Export Report")
    print("11. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_students(df)

    elif choice == "2":
        search_by_id(df)

    elif choice == "3":
        search_by_name(df)

    elif choice == "4":
        filter_department(df)

    elif choice == "5":
        top_students(df)

    elif choice == "6":
        bottom_students(df)

    elif choice == "7":
        department_average(df)

    elif choice == "8":
        pass_percentage(df)

    elif choice == "9":
        fail_percentage(df)

    elif choice == "10":
        export_report(df)

    elif choice == "11":
        print("Thank You")
        break

    else:
        print("Invalid Choice")