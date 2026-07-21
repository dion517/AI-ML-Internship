import pandas as pd

# Read the CSV file
df = pd.read_csv("Week2/Day2/dfstudents.csv")

# Students scoring above 80
print("Students Scoring Above 80")
print(df[df["Marks"] > 80])

# Students scoring below 40
print("\nStudents Scoring Below 40")
print(df[df["Marks"] < 40])

# Students scoring between 60 and 80
print("\nStudents Scoring Between 60 and 80")
print(df[(df["Marks"] >= 60) & (df["Marks"] <= 80)])