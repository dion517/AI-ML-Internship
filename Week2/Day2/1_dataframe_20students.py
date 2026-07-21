import pandas as pd

# Create data for 20 students
data = {
    "Student ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 116, 117, 118, 119, 120],

    "Name": ["Aarav", "Diya", "Rohan", "Meera", "Karan",
             "Ananya", "Vikram", "Sneha", "Rahul", "Priya",
             "Arjun", "Neha", "Ishaan", "Kavya", "Aditya",
             "Pooja", "Nikhil", "Aisha", "Varun", "Riya"],

    "Age": [18, 19, 20, 18, 21, 19, 20, 18, 21, 19,
            20, 18, 19, 20, 21, 18, 19, 20, 21, 18],

    "Department": ["CSE", "ECE", "IT", "MECH", "CIVIL",
                   "CSE", "ECE", "IT", "MECH", "CIVIL",
                   "CSE", "ECE", "IT", "MECH", "CIVIL",
                   "CSE", "ECE", "IT", "MECH", "CIVIL"],

    "Marks": [85, 90, 78, 88, 76, 91, 82, 79, 95, 87,
              84, 80, 89, 77, 92, 86, 81, 93, 75, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Student DataFrame:")
print(df)

# First 5 students
print("\nFirst 5 Students:")
print(df.head())

# Last 5 students
print("\nLast 5 Students:")
print(df.tail())

# Number of rows
print("\nNumber of Rows:", df.shape[0])

# Number of columns
print("Number of Columns:", df.shape[1])