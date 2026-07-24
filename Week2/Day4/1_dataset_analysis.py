import pandas as pd

# Load dataset
df = pd.read_csv("Week2/Day4/titanic.csv")  

# Number of rows and columns
print("Rows and Columns:", df.shape)

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate records
print("\nDuplicate Records:", df.duplicated().sum())