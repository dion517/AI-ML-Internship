import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv("Week2/Day3/automobile_dataset.csv")

# Set graph style
sns.set_style("whitegrid")

# 1. Selling Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Selling_Price"], bins=30, kde=True)
plt.title("Distribution of Selling Price")
plt.show()

# 2. Selling Price by Fuel Type
plt.figure(figsize=(8,5))
sns.boxplot(x="Fuel_Type", y="Selling_Price", data=df)
plt.title("Selling Price by Fuel Type")
plt.show()

# 3. Number of Cars by Make
plt.figure(figsize=(10,6))
sns.countplot(y="Make", data=df, order=df["Make"].value_counts().index)
plt.title("Cars by Manufacturer")
plt.show()

# 4. Mileage vs Selling Price
plt.figure(figsize=(8,5))
sns.scatterplot(x="Mileage", y="Selling_Price", data=df)
plt.title("Mileage vs Selling Price")
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 6. Average Selling Price by Year
plt.figure(figsize=(10,5))
sns.barplot(x="Year", y="Selling_Price", data=df, estimator="mean", errorbar=None)
plt.title("Average Selling Price by Year")
plt.xticks(rotation=45)
plt.show()

# 7. Horsepower vs Selling Price
plt.figure(figsize=(8,5))
sns.scatterplot(x="Horsepower", y="Selling_Price", data=df)
plt.title("Horsepower vs Selling Price")
plt.show()

# 8. Body Type Distribution
body = df["Body_Type"].value_counts()
plt.figure(figsize=(7,7))
plt.pie(body, labels=body.index, autopct="%1.1f%%", startangle=90)
plt.title("Body Type Distribution")
plt.show()

# 9. Transmission Type Count
plt.figure(figsize=(6,5))
sns.countplot(x="Transmission", data=df)
plt.title("Transmission Types")
plt.show()

# 10. Fuel Efficiency by Drivetrain
plt.figure(figsize=(8,5))
sns.boxplot(x="Drivetrain", y="Fuel_Efficiency", data=df)
plt.title("Fuel Efficiency by Drivetrain")
plt.show()