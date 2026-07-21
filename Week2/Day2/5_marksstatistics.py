import pandas as pd

# Read the CSV file
df = pd.read_csv("Week2/Day2/dfstudents.csv")

# Highest Marks
print("Highest Marks:", df["Marks"].max())

# Lowest Marks
print("Lowest Marks:", df["Marks"].min())

# Average Marks
print("Average Marks:", df["Marks"].mean())

# Median Marks
print("Median Marks:", df["Marks"].median())

# Total Students
print("Total Students:", df["StudentID"].count())