import pandas as pd

# Read the CSV file
df = pd.read_csv("Week2/Day2/dfstudents.csv")

# Group by Department and calculate statistics
result = df.groupby("Department").agg({
    "Marks": ["mean", "max", "min"],
    "StudentID": "count"
})

# Rename the column names
result.columns = ["Average Marks", "Highest Marks", "Lowest Marks", "Student Count"]

# Display the result
print(result)