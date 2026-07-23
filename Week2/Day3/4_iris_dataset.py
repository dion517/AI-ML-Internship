import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from CSV
df = pd.read_csv("Week2/Day3/Iris.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display column names
print("\nColumn Names:")
print(df.columns)

# ---------------------------------------------------
# Find the species column automatically
# ---------------------------------------------------
species_col = None

for col in df.columns:
    if col.lower() in ["species", "variety", "class"]:
        species_col = col
        break

if species_col is None:
    print("Species column not found!")
    exit()

# ---------------------------------------------------
# Pair Plot
# ---------------------------------------------------
sns.pairplot(df, hue=species_col)
plt.suptitle("Pair Plot of Iris Dataset", y=1.02)
plt.show()

# ---------------------------------------------------
# Heatmap
# ---------------------------------------------------
plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include="number")

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

# ---------------------------------------------------
# Histogram
# ---------------------------------------------------
plt.figure(figsize=(8,5))

first_numeric = numeric_df.columns[0]

sns.histplot(
    df[first_numeric],
    bins=10,
    kde=True
)

plt.title(f"Histogram of {first_numeric}")
plt.xlabel(first_numeric)
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Scatter Plot
# ---------------------------------------------------
plt.figure(figsize=(8,6))

x_col = numeric_df.columns[0]
y_col = numeric_df.columns[2]

sns.scatterplot(
    x=x_col,
    y=y_col,
    hue=species_col,
    data=df
)

plt.title(f"{x_col} vs {y_col}")
plt.show()