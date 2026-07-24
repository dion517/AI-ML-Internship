import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("week2/Day4/cleaned_dataset.csv")

# Convert 'Sex' to numerical values for correlation
df["Sex"] = df["Sex"].map({"male": 1, "female": 0})

# Select only numerical columns
numeric_df = df.select_dtypes(include=["int64", "float64"])

# Correlation Matrix
correlation = numeric_df.corr()

print("Correlation Matrix:")
print(correlation)

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Matrix Heatmap")
plt.show()