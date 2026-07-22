import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

print("First 5 rows of the dataset:")
print(df.head())

# 1. Passenger Class
plt.figure(figsize=(6,5))
sns.countplot(x="class", data=df)
plt.title("Passenger Class Distribution")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.show()

# 2. Age Distribution

plt.figure(figsize=(8,5))
sns.histplot(df["age"], bins=20, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 3. Survival Count

plt.figure(figsize=(6,5))
sns.countplot(x="survived", data=df)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.show()

# 4. Gender Distribution

plt.figure(figsize=(6,5))
sns.countplot(x="sex", data=df)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.show()

# 5. Survival by Gender

plt.figure(figsize=(6,5))
sns.countplot(x="sex", hue="survived", data=df)
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()