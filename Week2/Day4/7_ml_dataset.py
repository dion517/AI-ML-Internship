import pandas as pd

# Load dataset
df = pd.read_csv("week2/Day4/titanic.csv")

# 1. Handle Missing Values

# Fill Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill Embarked with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column
if "Cabin" in df.columns:
    df.drop("Cabin", axis=1, inplace=True)

# 2. Remove Duplicate Records

df.drop_duplicates(inplace=True)

# 3. Encode Categorical Columns

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    df[column] = df[column].astype("category").cat.codes

# 4. Scale Numerical Columns

numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

for column in numerical_columns:
    mean = df[column].mean()
    std = df[column].std()

    if std != 0:
        df[column] = (df[column] - mean) / std

# 5. Save Dataset

df.to_csv("ml_ready_dataset.csv", index=False)

print("ML Ready Dataset Created Successfully!")
print(df.head())