def display_students(df):
    print(df)

def search_by_id(df):
    sid = int(input("Enter Student ID: "))
    print(df[df["StudentID"] == sid])

def search_by_name(df):
    name = input("Enter Name: ")
    print(df[df["Name"].str.lower() == name.lower()])

def filter_department(df):
    dept = input("Enter Department: ")
    print(df[df["Department"].str.upper() == dept.upper()])