import pandas as pd

# Read the CSV file
df = pd.read_csv("Week2/Day2/dfstudents.csv")

# Create duplicate records (duplicate first 3 rows)
duplicate_rows = df.iloc[:3]

# Add duplicates to the DataFrame
df_duplicate = pd.concat([df, duplicate_rows], ignore_index=True)

print("Before Removing Duplicates:")
print(df_duplicate)

# Remove duplicate records
df_no_duplicates = df_duplicate.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df_no_duplicates)