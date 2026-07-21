import pandas as pd

# Read the CSV file
df = pd.read_csv("Week2/Day2/dfstudents.csv")

# Create the report
department_report = df.groupby("Department").agg(
    Average_Marks=("Marks", "mean"),
    Highest_Marks=("Marks", "max"),
    Lowest_Marks=("Marks", "min"),
    Student_Count=("StudentID", "count")
)

# Display the report
print("Department Report")
print(department_report)

# Save the report as a CSV file
department_report.to_csv("Week2/Day2/department_report.csv", index=True)

print("\nReport saved successfully as 'department_report.csv'")