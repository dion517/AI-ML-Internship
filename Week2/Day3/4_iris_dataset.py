# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Convert to DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add species names
df["species"] = iris.target
df["species"] = df["species"].map({
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
})

print("First 5 rows of the dataset:")
print(df.head())

# 1. Pair Plot

sns.pairplot(df, hue="species")
plt.suptitle("Pair Plot of Iris Dataset", y=1.02)
plt.show()

# 2. Heatmap

plt.figure(figsize=(8,6))
sns.heatmap(df.drop("species", axis=1).corr(),
            annot=True,
            cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 3. Histogram

plt.figure(figsize=(8,5))
sns.histplot(df["sepal length (cm)"], bins=10, kde=True)
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot

plt.figure(figsize=(8,6))
sns.scatterplot(
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="species",
    data=df
)
plt.title("Scatter Plot of Sepal Length vs Petal Length")
plt.show()