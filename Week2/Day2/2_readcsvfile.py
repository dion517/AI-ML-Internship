import pandas as pd


df = pd.read_csv("Week2/Day2/dfstudents.csv")
# Display the first 5 rows
print("Head:")
print(df.head())

# Display the last 5 rows
print("\nTail:")
print(df.tail())

# Display the shape (rows, columns)
print("\nShape:")
print(df.shape)

# Display the column names
print("\nColumns:")
print(df.columns)

# Display the data types of each column
print("\nData Types:")
print(df.dtypes)