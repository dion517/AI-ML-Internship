employees = {}

# Functions 

def add_employee():
    emp_id = input("Enter Employee ID: ")

    if emp_id in employees:
        print("Employee already exists.")
        return

    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    hra = basic * 0.20
    da = basic * 0.10
    tax = basic * 0.05
    net_salary = basic + hra + da - tax

    employees[emp_id] = {
        "Name": name,
        "Basic Salary": basic,
        "HRA": hra,
        "DA": da,
        "Tax": tax,
        "Net Salary": net_salary
    }

    print("Employee Added Successfully.")


def view_employees():
    if len(employees) == 0:
        print("No Employee Records.")
        return

    for emp_id, data in employees.items():
        print("------------------------------")
        print("Employee ID :", emp_id)
        print("Name :", data["Name"])
        print("Basic Salary :", data["Basic Salary"])
        print("HRA :", data["HRA"])
        print("DA :", data["DA"])
        print("Tax :", data["Tax"])
        print("Net Salary :", data["Net Salary"])


def search_employee():
    emp_id = input("Enter Employee ID: ")

    if emp_id in employees:
        data = employees[emp_id]

        print("Employee ID :", emp_id)
        print("Name :", data["Name"])
        print("Basic Salary :", data["Basic Salary"])
        print("HRA :", data["HRA"])
        print("DA :", data["DA"])
        print("Tax :", data["Tax"])
        print("Net Salary :", data["Net Salary"])
    else:
        print("Employee Not Found.")


def delete_employee():
    emp_id = input("Enter Employee ID: ")

    if emp_id in employees:
        del employees[emp_id]
        print("Employee Deleted Successfully.")
    else:
        print("Employee Not Found.")


# Main Menu

while True:

    print("\n===== Employee Payroll System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")