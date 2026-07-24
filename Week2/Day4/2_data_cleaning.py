import pandas as pd

df = pd.read_csv("week2/Day4/titanic.csv")

df = df.drop_duplicates()

# Fill missing numerical values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing categorical values with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column because it has many missing values
df = df.drop(columns=["Cabin"])

# Verify cleaned dataset
print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully.")