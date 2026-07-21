import pandas as pd

# Read the CSV file
df = pd.read_csv("Week2/Day2/dfstudents.csv")

# Sort by Marks (Ascending)
print("Students Sorted by Marks (Ascending):")
print(df.sort_values(by="Marks"))

# Sort by Marks (Descending)
print("\nStudents Sorted by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))

# Sort by Age (Ascending)
print("\nStudents Sorted by Age:")
print(df.sort_values(by="Age"))