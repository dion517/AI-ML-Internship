import pandas as pd

# Read the CSV file
df = pd.read_csv("Week2/Day2/dfstudents.csv")

# 1. Dataset Shape
print("1. Dataset Shape:")
print(df.shape)

# 2. Number of Columns
print("\n2. Number of Columns:")
print(len(df.columns))

# 3. Missing Values
print("\n3. Missing Values:")
print(df.isnull().sum())

# 4. Duplicate Records
print("\n4. Duplicate Records:")
print(df.duplicated().sum())

# 5. Highest Marks
print("\n5. Highest Marks:")
print(df["Marks"].max())

# 6. Lowest Marks
print("\n6. Lowest Marks:")
print(df["Marks"].min())

# 7. Average Marks
print("\n7. Average Marks:")
print(df["Marks"].mean())

# 8. Department-wise Average Marks
print("\n8. Department-wise Average Marks:")
print(df.groupby("Department")["Marks"].mean())

# 9. Top 10 Students
print("\n9. Top 10 Students:")
print(df.sort_values(by="Marks", ascending=False).head(10))

# 10. Bottom 10 Students
print("\n10. Bottom 10 Students:")
print(df.sort_values(by="Marks").head(10))