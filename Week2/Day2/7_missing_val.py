import pandas as pd

# Create a DataFrame with missing values
data = {
    "StudentID": [101, 102, 103, 104, 105],
    "Name": ["Aarav", "Diya", "Rohan", "Meera", None],
    "Age": [18, 19, None, 18, 20],
    "Department": ["CSE", "ECE", "IT", None, "CIVIL"],
    "Marks": [85, None, 78, 88, 90]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Check for missing values
print("\nMissing Values (isnull):")
print(df.isnull())

# Fill missing values
filled_df = df.fillna({
    "Name": "Unknown",
    "Age": 0,
    "Department": "Not Assigned",
    "Marks": 0
})

print("\nDataFrame after fillna():")
print(filled_df)

# Remove rows with missing values
dropped_df = df.dropna()

print("\nDataFrame after dropna():")
print(dropped_df)