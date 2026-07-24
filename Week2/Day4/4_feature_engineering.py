import pandas as pd

df = pd.read_csv("Week2/Day4/cleaned_dataset.csv")

# Label Encoding

df["Sex"] = df["Sex"].map({"male": 1, "female": 0})

# One-Hot Encoding

# Convert Embarked column into multiple binary columns

df = pd.get_dummies(df, columns=["Embarked"], dtype=int)

# Display first 5 rows
print(df.head())

# Save the transformed dataset
df.to_csv("feature_engineered_dataset.csv", index=False)

print("\nFeature engineered dataset saved successfully.")